---

# 🚀 SSH-SOCKS5-Tunnel

Python-based SSH SOCKS5 proxy tunnel manager with Telegram bot integration.
Automatically creates and monitors SSH tunnels through multiple servers, sends system info, and accepts remote commands via Telegram.

---

## ✨ Features

* 🔄 Automatic SSH SOCKS5 Tunnel Management (dynamic port forwarding, auto-reconnect)
* 🤖 Telegram Bot Integration for remote control and status updates
* 🌐 Support for multiple SSH servers with password or key authentication
* 📊 On-demand system monitoring: CPU, RAM, Disk, Network stats
* 🛑 Graceful shutdown and cleanup on exit or kill signals

---

## ⚙️ Prerequisites

* 🐧 Linux (Ubuntu/Debian recommended)
* 🐍 Python 3.6+
* 🔐 Installed SSH client tools: `ssh`, `sshpass`
* 🤖 Telegram Bot Token and Chat ID

---

## 🛠️ Installation

1. Clone the repo:

```bash
git clone https://github.com/o-k-l-l-a/SSH-SOCKS5-Tunnel.git
cd SSH-SOCKS5-Tunnel
```

2. Run setup script to install dependencies:

```bash
chmod +x setup.sh
./setup.sh
```

---

## ⚙️ Configuration

Add your SSH servers in `servers.json`. You can either use the Telegram bot command `/ssh` or manually edit the file like this:

```json
[
  {
    "host": "1.2.3.4",
    "port": 22,
    "user": "root",
    "pass": "yourpassword"
  },
  {
    "host": "5.6.7.8",
    "port": 22,
    "user": "ubuntu",
    "key": "/path/to/private/key"
  }
]
```

Then set your Telegram bot token and chat ID inside the Python script:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## ▶️ Usage

Run the main script:

```bash
python3 ssh_bot.py
```

The bot will:

* Maintain a SOCKS5 proxy on port `4343`
* Auto-reconnect tunnels if disconnected
* Listen for Telegram commands (`/status`, `/list`, `/ssh ...`)

---

## 💬 Telegram Commands

* `/status` — Show current system stats (CPU, RAM, Disk, Network)
* `/list` — List saved SSH servers
* `/ssh host=IP port=22 user=username pass=password` — Add new server (supports `key=` too)

---

## 🛠 Troubleshooting

* Ensure `sshpass` is installed and in your PATH
* Verify SSH keys and passwords
* Confirm port `4343` is free locally
* Double-check Telegram bot token and chat ID
* Watch console logs for errors

---

## 📄 License

MIT License. See [LICENSE](LICENSE) file.

---

## 🤝 Contributing & Contact

Open issues or PRs on GitHub.
Created by [o-k-l-l-a](https://github.com/o-k-l-l-a).
For help, open an issue or message via Telegram.

---

اگر دوست داری، می‌تونم نسخه Markdown فایلش رو هم برات آماده کنم تا سریع آپلود کنی.
