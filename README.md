حتماً! در ادامه یک نسخه‌ی کامل‌تر و دقیق‌تر از `README.md` رو می‌بینی که با جزئیات بیشتر نحوه نصب، اجرا، و استفاده از ربات رو توضیح می‌ده. این نسخه برای یک کاربر نیمه‌تخصصی هم کاملاً قابل فهمه و می‌تونه خیلی راحت پروژه رو راه بندازه و ازش استفاده کنه:

---

### 📝 `README.md` کامل و دقیق:

````markdown
# 🤖 Telegram-Controlled SSH Tunnel Manager

This is a Python project that allows you to **create and monitor an SSH SOCKS5 proxy tunnel**, controlled entirely via a **Telegram bot**.

You can:
- Add SSH servers remotely via Telegram
- Automatically reconnect SSH tunnels if they drop
- Monitor system resources (CPU, RAM, Disk, Network)
- Use the tunnel to route Telegram messages

---

## 🚀 Features

- 🔄 Automatically reconnects dropped SSH tunnels
- 🔐 Creates a local SOCKS5 proxy (default port: 434)
- 🧠 Add new SSH servers via `/ssh` command from Telegram
- 📈 Check system resource usage via `/status`
- 📋 List saved SSH servers via `/list`
- 💬 All communication (commands/responses) goes through Telegram

---

## 📦 Requirements

### ✅ OS Dependencies (Linux-based systems)

Make sure these are installed:

```bash
sudo apt update
sudo apt install sshpass openssh-client
````

> `sshpass` is used to connect to SSH servers using a password.

---

### ✅ Python Dependencies

You need Python 3.6+ installed. Then install required libraries:

```bash
pip install psutil requests
```

You can also use a `requirements.txt` like:

```text
psutil
requests
```

Then install with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Open `bot.py` and set your **Telegram bot token** and **chat ID** at the top of the script:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
```

> 💡 To get your chat ID, send a message to your bot and use a tool like [@userinfobot](https://t.me/userinfobot) to find your ID.

You can also customize:

```python
LOCAL_SOCKS_PORT = 434        # Port for the local SOCKS5 proxy
CHECK_INTERVAL = 10           # Tunnel check interval (in seconds)
```

---

## ▶️ Running the Bot

After setting up everything, just run the script:

```bash
python bot.py
```

Leave it running — the bot will:

* Monitor the SSH tunnel every `CHECK_INTERVAL` seconds
* Automatically reconnect if it's down
* Respond to your Telegram commands

---

## 📲 Telegram Bot Commands

| Command                                              | Description                            |
| ---------------------------------------------------- | -------------------------------------- |
| `/status`                                            | Show CPU, RAM, disk, and network usage |
| `/list`                                              | List all saved SSH servers             |
| `/ssh host=IP port=PORT user=USERNAME pass=PASSWORD` | Add new SSH server                     |

### Example:

```
/ssh host=1.2.3.4 port=22 user=root pass=secret123
```

> ⚠️ Be careful with sending passwords over Telegram — only use this in a secure, private bot.

---

## 💾 Server Storage

All added servers are stored in `servers.json` in this format:

```json
[
  {
    "host": "1.2.3.4",
    "port": 22,
    "user": "root",
    "pass": "yourpassword"
  }
]
```

You can edit this file manually too.

---

## 🔐 Security Notice

* ❌ Do **NOT** publish your bot token, chat ID, or server passwords on GitHub or anywhere public.
* ✅ Use a `.env` file or environment variables for production deployment.
* 🛡 Best for **personal use**, VPS automation, or secure LAN environments.

---

## 🔄 Example Use Case

* You have multiple SSH servers.
* This script ensures one is always connected via a local SOCKS5 proxy.
* You manage everything (add servers, monitor system, etc.) via Telegram — even from your phone.

---

## 🧑‍💻 Author

Made with ❤️ by \o-k-l-l-a

---
