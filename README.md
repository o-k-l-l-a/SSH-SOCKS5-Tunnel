````markdown
# 🚀 SSH-SOCKS5-Tunnel

A robust Python-based SSH SOCKS5 proxy tunnel manager with Telegram bot integration.  
Automatically establishes and monitors SSH SOCKS5 tunnels through multiple servers, sends system status updates, and accepts remote commands via Telegram.

---

## ✨ Features

- 🔄 **Automatic SSH SOCKS5 Tunnel Management**  
  Connects to multiple SSH servers with dynamic port forwarding (SOCKS5 proxy), automatically reconnects on failure.

- 🤖 **Telegram Bot Integration**  
  Receive system status and control your tunnel setup via Telegram commands.

- 🌐 **Multi-Server Support**  
  Load, save, and cycle through multiple SSH servers with password or key authentication.

- 📊 **System Monitoring**  
  CPU, RAM, Disk, and network bandwidth stats delivered on demand via Telegram.

- 🛑 **Graceful Shutdown Handling**  
  Proper cleanup of SSH tunnels on exit or termination signals.

---

## ⚙️ Prerequisites

- 🐧 Linux-based OS (tested on Ubuntu/Debian)  
- 🐍 Python 3.6+  
- 🔐 SSH client tools installed (`ssh`, `sshpass`)  
- 🤖 Telegram Bot Token & Chat ID  

---

## 🛠️ Installation

1. **Clone this repository:**

```bash
git clone https://github.com/o-k-l-l-a/SSH-SOCKS5-Tunnel.git
cd SSH-SOCKS5-Tunnel
````

2. **Run the setup script to install dependencies:**

```bash
chmod +x setup.sh
./setup.sh
```

---

## ⚙️ Configuration

* Add your SSH servers to `servers.json` using the Telegram bot command `/ssh` or manually edit the file with entries like:

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

* Set your Telegram bot token and chat ID in the Python script variables:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## ▶️ Usage

Run the main Python script:

```bash
python3 script.py
```

The bot will:

* 🔐 Maintain a persistent SSH SOCKS5 tunnel on port `4343` by default.
* 🔄 Monitor tunnel status and reconnect if necessary.
* 💬 Listen for Telegram commands to provide status, list servers, or add new SSH servers.

---

## 💬 Telegram Commands

* `/status` — Get current system status (CPU, RAM, Disk, Network).
* `/list` — List all registered SSH servers.
* `/ssh host=IP port=22 user=username pass=password` — Add a new SSH server.
* Supports key-based authentication as well: `/ssh host=IP port=22 user=username key=/path/to/key`

---

## 🛠 Troubleshooting

* ✅ Make sure `sshpass` is installed and available in your PATH.
* 🔑 Verify your SSH keys and passwords are correct.
* 🚪 The bot uses port `4343` locally for the SOCKS5 proxy; ensure this port is free.
* 🔍 Check Telegram bot token and chat ID correctness.
* 📜 Logs are printed to console; monitor for errors.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

---

## 📫 Contact

Created by [o-k-l-l-a](https://github.com/o-k-l-l-a)
For support or questions, open an issue or contact via Telegram.

```
```
