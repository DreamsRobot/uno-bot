# uno-bot
# 🎮 UNO Telegram Bot

A multiplayer UNO game bot for Telegram with inline card display.  
Supports local PNG images or Telegram stickers for card graphics.  
Works in **group chats** and **private battles**.

---

## 🚀 Features
- Multiplayer lobby system (join, leave, start game)
- Full UNO rules (Skip, Reverse, Draw 2, Wild, Wild Draw 4)
- Card graphics shown via PNG or stickers
- Group + private turn handling
- Works on **Heroku**, **Railway**, **Render**, and **Uptime Server (Ops)**

---

## 📂 Project Structure




---

## 🖥 VPS (Ubuntu/Debian) Installation

Run these commands step by step:

### 1️⃣ Update and upgrade
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-pip ffmpeg -y
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash -
sudo apt-get install nodejs -y
npm i -g npm
git clone https://github.com/yourname/uno-bot.git
cd uno-bot
pip3 install -U -r requirements.txt
vi sample.env
sudo apt install tmux -y && tmux
bash start
