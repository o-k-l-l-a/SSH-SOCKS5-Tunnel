import subprocess
import time
import socket
import json
import psutil
import requests
import os

# ⚙️ Main settings
LOCAL_SOCKS_PORT = 434
CHECK_INTERVAL = 10  # How often to check status in seconds

# 📬 Telegram bot info
BOT_TOKEN = ""
CHAT_ID = ""
LAST_UPDATE_ID = None


# 🧠 Load servers
def load_servers():
    if os.path.exists("servers.json"):
        with open("servers.json", "r") as f:
            return json.load(f)
    return []

servers = load_servers()

# 📡 Check if port is open
def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False

def start_ssh_tunnel(server):
    print(f"⏳ Connecting to SSH at {server['host']}:{server['port']} ...")
    DEFAULT_CIPHERS = "chacha20-poly1305@openssh.com,aes128-ctr"
    ssh_command = [
        "sshpass", "-p", server["pass"],
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "UserKnownHostsFile=/dev/null",
        "-o", "TCPKeepAlive=yes",
        "-o", "ServerAliveInterval=60",
        "-o", "ConnectTimeout=10",
        "-o", f"Ciphers={DEFAULT_CIPHERS}",
        "-o", "CompressionLevel=9",
        "-C",
        "-x",
        "-f", "-D", str(LOCAL_SOCKS_PORT),
        "-q", "-N",
        "-p", str(server["port"]),
        f"{server['user']}@{server['host']}",
    ]
    result = subprocess.run(ssh_command, capture_output=True)
    if result.returncode == 0:
        print(f"✅ SSH tunnel to {server['host']} established.")
        return True
    else:
        print(f"❌ Error connecting to {server['host']}: {result.stderr.decode()}")
        return False


# ✉️ Send message to Telegram
def send_telegram_message(text):
    session = requests.Session()
    session.proxies = {
        "http": f"socks5h://127.0.0.1:{LOCAL_SOCKS_PORT}",
        "https": f"socks5h://127.0.0.1:{LOCAL_SOCKS_PORT}"
    }

    encoded_text = requests.utils.quote(text)
    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        f"?chat_id={CHAT_ID}&text={encoded_text}"
    )

    try:
        resp = session.get(url, timeout=15)
        print(f"📦 Telegram response: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ Error sending Telegram message: {e}")

# 🧾 Get system status
def get_system_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    return (
        f"📊 System Status:\n"
        f"🧠 CPU: {cpu}%\n"
        f"📈 RAM: {ram.percent}% of {round(ram.total / (1024**3), 2)} GB\n"
        f"💾 Disk: {disk.percent}% of {round(disk.total / (1024**3), 2)} GB\n"
        f"📡 Bandwidth:\n"
        f"⬇️ Downloaded: {round(net.bytes_recv / (1024**2), 2)} MB\n"
        f"⬆️ Uploaded: {round(net.bytes_sent / (1024**2), 2)} MB"
    )


# 🆕 Save new server
def save_server(server):
    global servers
    servers.append(server)
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=4)
    send_telegram_message(f"✅ New server added:\n{server['host']}:{server['port']} - {server['user']}")

# 📥 Process /ssh command
def parse_ssh_command(text):
    try:
        parts = text.strip().split()
        data = {}
        for part in parts[1:]:
            key, value = part.split("=")
            data[key] = value
        if all(k in data for k in ("host", "port", "user", "pass")):
            return data
    except:
        pass
    return None

# 📲 Check Telegram bot commands
def check_bot_updates():
    global LAST_UPDATE_ID
    session = requests.Session()
    session.proxies = {
        "http": f"socks5h://127.0.0.1:{LOCAL_SOCKS_PORT}",
        "https": f"socks5h://127.0.0.1:{LOCAL_SOCKS_PORT}"
    }

    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
        if LAST_UPDATE_ID:
            url += f"?offset={LAST_UPDATE_ID + 1}"
        resp = session.get(url, timeout=15)
        data = resp.json()

        for update in data.get("result", []):
            LAST_UPDATE_ID = update["update_id"]
            message = update.get("message", {})
            text = message.get("text", "").strip()
            chat_id = str(message.get("chat", {}).get("id", ""))

            if chat_id != CHAT_ID:
                continue

            if text.lower() == "/status":
                status = get_system_status()
                send_telegram_message(status)

            elif text.lower() == "/list":
                if not servers:
                    send_telegram_message("⚠️ No servers registered.")
                else:
                    msg = "📋 Server list:\n"
                    for i, s in enumerate(servers, 1):
                        msg += f"{i}. {s['host']}:{s['port']} - {s['user']}\n"
                    send_telegram_message(msg)

            elif text.lower().startswith("/ssh"):
                server = parse_ssh_command(text)
                if server:
                    save_server(server)
                else:
                    send_telegram_message("❌ Incorrect command format.\nExample:\n`/ssh host=1.2.3.4 port=22 user=root pass=1234`")

    except Exception as e:
        print(f"❌ Error checking bot commands: {e}")

# 🎯 Main function
def main():
    global servers
    current_server_index = 0
    last_connected_host = None

    while True:
        if not servers:
            print("⚠️ No servers defined, please add a server first.")
            time.sleep(CHECK_INTERVAL)
            continue

        check_bot_updates()

        if not is_port_open("127.0.0.1", LOCAL_SOCKS_PORT):
            print("⚠️ Tunnel is down or inactive.")
            attempts = 0

            while attempts < len(servers):
                server = servers[current_server_index]
                success = start_ssh_tunnel(server)

                if success:
                    if server['host'] != last_connected_host:
                        send_telegram_message(f"✅ SSH tunnel is active:\n🌐 `{server['host']}`")
                        last_connected_host = server['host']
                    break
                else:
                    current_server_index = (current_server_index + 1) % len(servers)
                    attempts += 1
                    time.sleep(2)
        else:
            print(f"✅ Tunnel to {servers[current_server_index]['host']} is active.")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
