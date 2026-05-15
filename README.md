# WhereAreU 🌍

WhereAreU is a simple web-based project that demonstrates how a server can receive basic client information (like IP and optional geolocation) and send it to a configured Discord webhook for **testing and educational purposes only**.

> ⚠️ This project is intended for learning, debugging, and authorized testing only. Do not use it to collect data from users without consent.

---

## 🚀 Features

- Simple Python server (`server.py`)
- Optional Discord webhook integration
- Geolocation prompt (browser-based permission)
- Public tunnel support via Cloudflared
- Lightweight and easy to deploy

---

## 📦 Requirements

- Python 3
- pip
- git
- cloudflared

---

## 📥Installation
git clone https://github.com/Vessel27/WhereAreU.git

cd WhereAreU

nano index.html
change the webhook link, on your own link

python3 server.py

open new terminal and run this
cloudflared tunnel --url http://localhost:8000
