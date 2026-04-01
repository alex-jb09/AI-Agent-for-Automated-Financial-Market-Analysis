<div align="center">

# Orallexa

### AI-Powered Capital Intelligence Engine

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js)](https://nextjs.org)
[![Claude](https://img.shields.io/badge/Claude_AI-Sonnet_4-cc785c?style=flat-square)](https://anthropic.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**Multi-agent AI trading research system with real-time signal generation, adversarial debate reasoning, and autonomous daily market intelligence.**

[English](#overview) | [中文](README_CN.md)

---

<img src="assets/screenshots/dashboard_preview.png" alt="Orallexa Dashboard" width="800">

*Art Deco-inspired trading intelligence dashboard with real-time analysis*

</div>

---

## Overview

Orallexa is an AI-powered trading intelligence platform that combines technical analysis, machine learning models, and multi-agent Claude AI reasoning to generate actionable trade signals. It features a full-stack architecture with a React dashboard, Python analysis engine, and desktop AI coach.

### Key Differentiators

- **Multi-Agent Adversarial Debate** — Bull and Bear analysts argue, a Judge synthesizes the final call
- **Volume Spike Detection** — Automatically detects unusual institutional activity across 50+ tickers
- **Daily Market Intel** — Autonomous morning brief with AI-generated social media threads
- **Probability-First UI** — Polymarket-inspired design with large probability displays and progressive disclosure

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Orallexa Platform                         │
├──────────────┬──────────────────┬───────────────────────────┤
│  React UI    │   FastAPI Server │   Desktop Agent           │
│  (Next.js)   │   (Python)       │   (Tkinter + TTS)         │
│              │                  │                           │
│  ┌────────┐  │  ┌────────────┐  │  ┌──────────────┐        │
│  │Signal  │◄─┼──│ /api/      │  │  │ Bull Coach   │        │
│  │  View  │  │  │  analyze   │  │  │ Voice + Chat │        │
│  ├────────┤  │  ├────────────┤  │  └──────────────┘        │
│  │Intel   │◄─┼──│ /api/      │  │                           │
│  │  View  │  │  │ daily-intel│  │                           │
│  └────────┘  │  ├────────────┤  │                           │
│              │  │ /api/      │  │                           │
│              │  │ deep-      │  │                           │
│              │  │ analysis   │  │                           │
│              │  └─────┬──────┘  │                           │
│              │        │         │                           │
│              │  ┌─────▼──────┐  │                           │
│              │  │Trading     │  │                           │
│              │  │  Engine    │  │                           │
│              │  │            │  │                           │
│              │  │ Technical  │  │                           │
│              │  │ ML Models  │  │                           │
│              │  │ Sentiment  │  │                           │
│              │  │ AI Debate  │  │                           │
│              │  │ Risk Mgmt  │  │                           │
│              │  └────────────┘  │                           │
└──────────────┴──────────────────┴───────────────────────────┘
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
        yfinance    Claude AI   scikit-learn
        (market)    (reasoning) (ML signals)
```

---

## Features

### Signal Analysis Engine
| Feature | Description |
|---------|-------------|
| **3 Trading Modes** | Scalp (5min), Intraday (15min/1H), Swing (1D) |
| **7 Technical Strategies** | Double MA, MACD, Bollinger, RSI, Volume, ADX, Factor |
| **ML Models** | Random Forest, XGBoost, Logistic Regression |
| **Bull/Bear Debate** | Adversarial AI reasoning with 3 Claude calls (Bull → Bear → Judge) |
| **Claude AI Overlay** | Optional single-call signal refinement via Haiku (~$0.0005) |
| **Risk Management** | Dynamic position sizing, stop-loss, take-profit, R:R calculation |
| **Investment Plans** | AI-generated entry/exit strategy with key risks |

### Daily Market Intelligence
| Feature | Description |
|---------|-------------|
| **Top Movers Scan** | 50+ tickers scanned in parallel for price changes |
| **Volume Spike Detection** | Flags unusual activity (2x+ average volume) |
| **Sector Heatmap** | 13 sector ETFs with rotation analysis |
| **AI Morning Brief** | 300-400 word Sonnet-powered market summary |
| **AI Picks** | 3-5 "worth watching" tickers with catalyst and thesis |
| **Orallexa Thread** | Ready-to-post social media thread with copy buttons |

### Dashboard (Next.js)
| Feature | Description |
|---------|-------------|
| **Art Deco UI** | Gold-accented dark theme with Poiret One / DM Mono typography |
| **Signal / Intel Toggle** | Switch between analysis and daily intelligence views |
| **Watchlist Scan** | Multi-ticker parallel scan with compact signal cards |
| **Live Price Refresh** | 30-second auto-refresh with price flash animations |
| **Breaking Alerts** | Polymarket-style banners for probability shifts |
| **Mobile Responsive** | Collapsible sidebars, stacked layout on mobile |
| **Bilingual** | Full EN / ZH support with one-click toggle |

### Desktop Agent
| Feature | Description |
|---------|-------------|
| **Bull Coach** | Floating AI trading coach with voice input/output |
| **Screenshot Analysis** | Ctrl+Shift+S to analyze any chart via Claude Vision |
| **Decision Card** | Risk management display with entry/stop/target |
| **System Tray** | Quick ticker/mode switching from tray icon |

---

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+
- [Anthropic API Key](https://console.anthropic.com/)

### 1. Clone & Setup

```bash
git clone https://github.com/YOUR_USERNAME/orallexa.git
cd orallexa

# Python dependencies
pip install -r requirements.txt

# Environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 2. Start the API Server

```bash
python api_server.py
# Server running at http://localhost:8002
```

### 3. Start the Dashboard

```bash
cd orallexa-ui
npm install
npm run dev
# Dashboard at http://localhost:3000
```

### 4. (Optional) Docker

```bash
# Copy your .env first
docker compose up --build
# API: http://localhost:8002
# UI:  http://localhost:3000
```

---

## Project Structure

```
orallexa/
├── api_server.py              # FastAPI server (all REST endpoints)
├── docker-compose.yml         # One-click Docker deployment
├── Dockerfile                 # API container
├── requirements.txt           # Python dependencies
│
├── core/
│   ├── brain.py               # OrallexaBrain — central analysis orchestrator
│   ├── loop.py                # Strategy optimization loop
│   ├── settings.py            # User preferences persistence
│   └── logger.py              # Logging infrastructure
│
├── engine/
│   ├── multi_agent_analysis.py # 5-agent pipeline (Market + News + ML + Debate + Risk)
│   ├── daily_intel.py         # Daily market intelligence generator
│   ├── breaking_signals.py    # Probability shift detection
│   ├── strategies.py          # 7 rule-based trading strategies
│   ├── ml_signal.py           # RF / XGBoost / LR models
│   ├── sentiment.py           # FinBERT / VADER sentiment analysis
│   └── backtest.py            # Backtesting engine
│
├── llm/
│   ├── claude_client.py       # Claude API (dual-tier: Haiku + Sonnet)
│   ├── debate.py              # Bull/Bear adversarial debate
│   ├── ui_analysis.py         # UI-facing analysis prompts
│   └── call_logger.py         # LLM cost tracking
│
├── models/
│   ├── decision.py            # DecisionOutput dataclass
│   ├── confidence.py          # Confidence scaling + edge guards
│   └── card_formatter.py      # Human-readable output formatting
│
├── skills/
│   ├── scalping.py            # 5-min scalp signal detection
│   ├── prediction.py          # Swing/daily probability forecast
│   ├── risk_management.py     # Position sizing + stop/target
│   ├── market_data.py         # yfinance data wrapper
│   └── news.py                # News headline fetching
│
├── orallexa-ui/               # Next.js 16 + React 19 + Tailwind 4
│   ├── app/page.tsx           # Main dashboard (Signal + Intel views)
│   ├── app/globals.css        # Art Deco theme + animations
│   └── Dockerfile             # Frontend container
│
├── desktop_agent/             # Tkinter desktop AI coach
│   ├── main.py                # Entry point
│   ├── chat_popover.py        # Floating chat window
│   ├── character_window.py    # Bull character avatar
│   ├── brain_bridge.py        # Trading engine bridge
│   ├── tts_handler.py         # Text-to-speech (OpenAI)
│   ├── voice_handler.py       # Voice input (Whisper)
│   └── i18n.py                # Internationalization
│
└── bot/
    ├── behavior.py            # Trade tracking + aggressiveness adaptation
    ├── paper_trading.py       # Paper trading simulator
    └── alerts.py              # Price alert system
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 16, React 19, Tailwind CSS 4 |
| **Backend** | FastAPI, Python 3.11 |
| **AI** | Claude Sonnet 4 (reasoning), Claude Haiku 4.5 (fast) |
| **ML** | scikit-learn, XGBoost |
| **Market Data** | yfinance (real-time + historical) |
| **NLP** | FinBERT, VADER, TextBlob |
| **Desktop** | Tkinter, OpenAI Whisper + TTS |
| **Deploy** | Docker, Docker Compose |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/analyze` | Fast signal analysis (scalp/intraday/swing) |
| POST | `/api/deep-analysis` | Multi-agent deep analysis with debate |
| POST | `/api/chart-analysis` | Screenshot chart analysis via Claude Vision |
| POST | `/api/watchlist-scan` | Parallel multi-ticker scan |
| GET | `/api/daily-intel` | Daily market intelligence (cached) |
| POST | `/api/daily-intel/refresh` | Force regenerate daily intel |
| GET | `/api/live/{ticker}` | Live price + last signal |
| GET | `/api/news/{ticker}` | News headlines + sentiment |
| GET | `/api/breaking-signals` | Recent probability shifts |
| GET | `/api/profile` | Trader behavior profile |
| GET | `/api/journal` | Decision execution log |

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude AI API key |
| `OPENAI_API_KEY` | Desktop only | Whisper + TTS for voice features |
| `CORS_ORIGINS` | Production | Comma-separated allowed origins |
| `NEXT_PUBLIC_API_URL` | Production | API server URL for frontend |

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

See [CHANGELOG.md](CHANGELOG.md) for recent development history.

---

## Acknowledgments

- [Anthropic Claude](https://anthropic.com) — AI reasoning engine
- [yfinance](https://github.com/ranaroussi/yfinance) — Market data
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — Multi-agent trading inspiration
- [Polymarket](https://polymarket.com) — Probability-first UI design inspiration

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**If you find this useful, please give it a star!**

Built with Claude AI by the Orallexa Team

</div>
