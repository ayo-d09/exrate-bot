# ExRate Bot 

A live Telegram currency converter bot that converts currencies in real time using the ExchangeRate API.

> This project is based on https://github.com/rajatrawal/currency-converter-bot by (https://github.com/rajatrawal). It has been extended with Prometheus monitoring, Grafana dashboards, Docker Compose, and a CI/CD pipeline.


## Features

-  Telegram bot interface
-  Real-time currency conversion
-  Prometheus metrics scraping
-  Grafana dashboard
-  Docker + Docker Compose
-  Automated deployment via GitHub Actions
-  Hosted on Fly.io


## Try It

<img width="611" height="842" alt="Screenshot 2026-04-24 at 09 17 46" src="https://github.com/user-attachments/assets/4faf96c3-2375-4783-9f9a-b052b4811fad" />

Search **@Get_ExRate_Bot** on Telegram and send (for example):
- 100 USD to NGN
- 50 EUR to GBP
- 200 GBP to JPY


### Grafana Dashboard
![Grafana](https://github.com/user-attachments/assets/b69cf4f3-d8a2-4fa4-bb8a-3e4783da0048)


## Stack

- Python / Flask
- Telegram Bot API
- ExchangeRate API
- Prometheus + Grafana
- Docker + Docker Compose
- GitHub Actions
- Fly.io


## Project Structure
```
exrate-bot/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── fly.toml
├── .env.example
├── .gitignore
├── README.md
└── .github/
└── workflows/
└── fly-deploy.yml
```


## Run Locally

```bash
# clone the repo
git clone https://github.com/ayo-d09/exrate-bot.git
cd exrate-bot

# add your keys
cp .env.example .env
# edit .env with your API keys

# run with Docker Compose
docker-compose up --build
```

- App → `http://localhost:5000`
- Prometheus → `http://localhost:9090`
- Grafana → `http://localhost:3000`


## Environment Variables
- KEY=your-exchangerate-api-key
- TELEGRAM_TOKEN=your-telegram-bot-token


## CI/CD
Every push to `main` automatically deploys to Fly.io via GitHub Actions.
<img width="1440" height="815" alt="Screenshot 2026-04-27 at 09 24 55" src="https://github.com/user-attachments/assets/6d29dfb0-f21f-4920-a0ac-65f1754c79a7" />
