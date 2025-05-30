# 🌆 Sydney Events Scraper 🎟️

[![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)  
[![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)  


---

## ✨ Overview

Welcome to **Sydney Events Scraper**, a clean and minimalistic web app built with **Streamlit** that scrapes and displays the latest events happening in **Sydney, Australia**.  
Browse upcoming events effortlessly, get details, and secure your tickets with ease — all in one place.

---

## 🎯 Features

- 🏙️ **Live event scraping:** Automatically fetches events from popular Sydney event sites  
- 🗓️ **Detailed info:** Event name, location, date & time, and brief description  
- 📧 **Email capture:** User email opt-in before ticket redirects  
- 🔄 **Auto-refresh:** Event list updates as new events are published  
- 🎨 **Elegant & sober UI:** Clean layout focused on usability  
- ⚡ **Powered by Streamlit:** Fast, interactive, and easy to deploy  

---

## 🚀 Live Demo

Check out the live app here:  
👉 [Sydney Events Scraper - Live on Streamlit](https://sydscrap-c6cuibjrqzqqfp5xuehxgx.streamlit.app/)  
Experience real-time event browsing and ticket reservations for Sydney events!

---

## 🖼️ Screenshots

![Homepage](docs/screenshot-home.png)  
*Simple, clear event listing with easy navigation*

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.9 or higher  
- `pip` package manager

### Installation

```bash
git clone https://github.com/yourusername/sydney-events-scraper.git
cd sydney-events-scraper
pip install -r requirements.txt
````

### Run Locally

```bash
streamlit run main.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
.
├── app.py             # Main Streamlit application
├── email_handler.py   # Handles email opt-ins and storage
├── event_data.json    # Sample or cached event data
├── requirements.txt   # Dependencies
└── README.md          # Project documentation (this file)
```

---

## ⚙️ How It Works

1. Events are loaded from `event_data.json` (or scraped live if extended).
2. Each event shows title, location, date/time, and description.
3. Clicking **Get Tickets** prompts the user to enter their email and consent.
4. Upon submission, the email is stored and user is redirected to the original event page.

> *Tip:* You can enhance the scraper module to pull live data dynamically.

---

## 🤝 Contributing

Contributions are always welcome!
Feel free to open issues, submit pull requests, or suggest improvements.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgments & Contact

Made with ❤️ by [Whisplnspace](https://github.com/whisplnspace)


---

> *"The best way to predict the future is to create it."* – Peter Drucker




