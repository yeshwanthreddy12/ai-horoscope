# 🔮 The AI Oracle

> *Whispers from the Digital Cosmos*

An immersive, mystical fortune-telling experience powered by AI. Ask the Oracle your deepest questions and receive cryptic prophecies woven from starlight and quantum echoes.

![The AI Oracle](https://img.shields.io/badge/Powered%20by-GPT--4o--mini-purple?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)

---

## ✨ Features

- **🌙 Mystical AI Prophecies** — GPT-4o-mini generates poetic, cryptic fortunes tailored to your questions
- **🎨 Stunning Cosmic UI** — Deep purple nebula gradients, twinkling stars, and ethereal animations
- **👁️ Animated Oracle Eye** — A floating, gazing eye that watches over seekers
- **📱 Fully Responsive** — Beautiful on desktop and mobile devices
- **⚡ Instant Deploy** — One-click deployment to Vercel

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/deploy.git
cd deploy

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Run the development server
uvicorn instant:app --reload --port 8000
```

Visit `http://localhost:8000` to consult the Oracle.

---

## 🌐 Deploy to Vercel

1. **Push to GitHub** (if not already)
2. **Import to Vercel** at [vercel.com/new](https://vercel.com/new)
3. **Add Environment Variable:**
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
4. **Deploy!**

---

## 🎭 How It Works

1. **Ask a Question** — Type your deepest inquiry into the Oracle's portal
2. **The Oracle Perceives** — AI channels cosmic wisdom through various mystical themes:
   - Cosmic whispers from distant galaxies
   - Ancient runes carved in starlight
   - Echoes from the quantum realm
   - Shadows of possible futures intertwining
3. **Receive Your Prophecy** — A beautifully rendered mystical response appears

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance Python web framework |
| **OpenAI GPT-4o-mini** | AI-powered prophecy generation |
| **Vercel** | Serverless deployment platform |
| **Pure CSS** | Animations, gradients, and cosmic effects |

---

## 📁 Project Structure

```
deploy/
├── instant.py       # Main FastAPI application
├── requirements.txt # Python dependencies
├── vercel.json      # Vercel deployment config
└── README.md        # You are here
```

---

## 🎨 Design Philosophy

The Oracle embraces a **cosmic mystical aesthetic**:

- **Colors:** Void black, nebula purple, mystic gold, ethereal cream, accent cyan
- **Typography:** Cinzel Decorative (titles) + Cormorant Garamond (body)
- **Effects:** Floating animations, shimmer gradients, pulsing glows, twinkling stars
- **Mood:** Ancient wisdom meets digital consciousness

---

## 📜 License

MIT License — Feel free to fork, modify, and deploy your own Oracle!

---

<p align="center">
  <em>✦ The stars have aligned. Your destiny awaits. ✦</em>
</p>

