from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI
import random

app = FastAPI()

MYSTICAL_THEMES = [
    "cosmic whispers from distant galaxies",
    "ancient runes carved in starlight",
    "the eternal dance of fate and chance",
    "echoes from the quantum realm",
    "shadows of possible futures intertwining",
    "the oracle's timeless wisdom awakening"
]

def get_oracle_styles():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --void: #0a0a0f;
            --nebula: #1a0a2e;
            --cosmic-purple: #4a1942;
            --mystic-gold: #d4af37;
            --ethereal: #e8d5b7;
            --accent-cyan: #00d4ff;
        }
        
        body {
            font-family: 'Cormorant Garamond', serif;
            background: var(--void);
            min-height: 100vh;
            overflow-x: hidden;
            color: var(--ethereal);
        }
        
        .cosmos {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: 
                radial-gradient(ellipse at 20% 80%, rgba(74, 25, 66, 0.4) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 20%, rgba(26, 10, 46, 0.6) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(0, 212, 255, 0.05) 0%, transparent 70%),
                linear-gradient(180deg, var(--void) 0%, var(--nebula) 50%, var(--void) 100%);
        }
        
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, var(--mystic-gold), transparent),
                radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
                radial-gradient(1px 1px at 90px 40px, var(--accent-cyan), transparent),
                radial-gradient(2px 2px at 160px 120px, var(--mystic-gold), transparent),
                radial-gradient(1px 1px at 230px 80px, rgba(255,255,255,0.6), transparent),
                radial-gradient(2px 2px at 300px 150px, var(--accent-cyan), transparent),
                radial-gradient(1px 1px at 370px 50px, var(--mystic-gold), transparent),
                radial-gradient(2px 2px at 450px 200px, rgba(255,255,255,0.7), transparent),
                radial-gradient(1px 1px at 520px 100px, var(--accent-cyan), transparent),
                radial-gradient(2px 2px at 600px 180px, var(--mystic-gold), transparent);
            background-size: 650px 250px;
            animation: twinkle 8s ease-in-out infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 30px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        .oracle-eye {
            width: 120px;
            height: 120px;
            margin-bottom: 40px;
            position: relative;
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
        }
        
        .eye-outer {
            width: 100%;
            height: 100%;
            border: 3px solid var(--mystic-gold);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle, rgba(74, 25, 66, 0.5) 0%, transparent 70%);
            box-shadow: 
                0 0 40px rgba(212, 175, 55, 0.3),
                inset 0 0 30px rgba(0, 212, 255, 0.1);
            animation: pulse-glow 3s ease-in-out infinite;
        }
        
        @keyframes pulse-glow {
            0%, 100% { box-shadow: 0 0 40px rgba(212, 175, 55, 0.3), inset 0 0 30px rgba(0, 212, 255, 0.1); }
            50% { box-shadow: 0 0 60px rgba(212, 175, 55, 0.5), inset 0 0 40px rgba(0, 212, 255, 0.2); }
        }
        
        .eye-inner {
            width: 50px;
            height: 50px;
            background: radial-gradient(circle, var(--accent-cyan) 0%, var(--cosmic-purple) 100%);
            border-radius: 50%;
            animation: eye-gaze 5s ease-in-out infinite;
        }
        
        @keyframes eye-gaze {
            0%, 100% { transform: translate(0, 0); }
            25% { transform: translate(5px, -3px); }
            50% { transform: translate(-3px, 5px); }
            75% { transform: translate(-5px, -2px); }
        }
        
        h1 {
            font-family: 'Cinzel Decorative', cursive;
            font-size: clamp(2.5rem, 6vw, 4rem);
            font-weight: 700;
            text-align: center;
            margin-bottom: 15px;
            background: linear-gradient(135deg, var(--mystic-gold) 0%, var(--ethereal) 50%, var(--mystic-gold) 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 4s linear infinite;
            text-shadow: 0 0 60px rgba(212, 175, 55, 0.3);
        }
        
        @keyframes shimmer {
            0% { background-position: 200% center; }
            100% { background-position: -200% center; }
        }
        
        .subtitle {
            font-size: 1.2rem;
            font-style: italic;
            color: rgba(232, 213, 183, 0.7);
            text-align: center;
            margin-bottom: 50px;
            letter-spacing: 3px;
        }
        
        .oracle-form {
            width: 100%;
            max-width: 600px;
            display: flex;
            flex-direction: column;
            gap: 25px;
            margin-bottom: 50px;
        }
        
        .input-wrapper {
            position: relative;
        }
        
        .input-wrapper::before {
            content: '✧';
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--mystic-gold);
            font-size: 1.2rem;
            opacity: 0.6;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 20px 25px 20px 50px;
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.2rem;
            color: var(--ethereal);
            background: rgba(26, 10, 46, 0.6);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 8px;
            outline: none;
            transition: all 0.4s ease;
        }
        
        input[type="text"]::placeholder {
            color: rgba(232, 213, 183, 0.4);
            font-style: italic;
        }
        
        input[type="text"]:focus {
            border-color: var(--mystic-gold);
            box-shadow: 
                0 0 30px rgba(212, 175, 55, 0.2),
                inset 0 0 20px rgba(0, 212, 255, 0.05);
        }
        
        button {
            padding: 18px 50px;
            font-family: 'Cinzel Decorative', cursive;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--void);
            background: linear-gradient(135deg, var(--mystic-gold) 0%, #b8962e 100%);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.4s ease;
            text-transform: uppercase;
            letter-spacing: 3px;
            position: relative;
            overflow: hidden;
        }
        
        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s ease;
        }
        
        button:hover::before {
            left: 100%;
        }
        
        button:hover {
            transform: translateY(-3px);
            box-shadow: 
                0 10px 40px rgba(212, 175, 55, 0.4),
                0 0 80px rgba(212, 175, 55, 0.2);
        }
        
        .prophecy {
            background: rgba(26, 10, 46, 0.7);
            border: 1px solid rgba(212, 175, 55, 0.2);
            border-radius: 12px;
            padding: 40px;
            max-width: 700px;
            position: relative;
            animation: reveal 1s ease-out;
        }
        
        @keyframes reveal {
            0% { opacity: 0; transform: translateY(30px) scale(0.95); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }
        
        .prophecy::before,
        .prophecy::after {
            content: '❖';
            position: absolute;
            color: var(--mystic-gold);
            font-size: 1.5rem;
            opacity: 0.6;
        }
        
        .prophecy::before { top: 15px; left: 20px; }
        .prophecy::after { bottom: 15px; right: 20px; }
        
        .prophecy-header {
            font-family: 'Cinzel Decorative', cursive;
            font-size: 1.4rem;
            color: var(--mystic-gold);
            margin-bottom: 25px;
            text-align: center;
            letter-spacing: 2px;
        }
        
        .prophecy-text {
            font-size: 1.25rem;
            line-height: 1.9;
            text-align: center;
            color: var(--ethereal);
        }
        
        .prophecy-text em {
            color: var(--accent-cyan);
            font-style: normal;
        }
        
        .mystical-footer {
            margin-top: 60px;
            text-align: center;
            opacity: 0.5;
            font-size: 0.9rem;
            letter-spacing: 2px;
        }
        
        .rune-decorations {
            display: flex;
            gap: 30px;
            justify-content: center;
            margin-bottom: 30px;
            font-size: 1.5rem;
            color: var(--mystic-gold);
            opacity: 0.4;
        }
        
        @media (max-width: 600px) {
            .container { padding: 40px 20px; }
            .prophecy { padding: 25px 20px; }
            .oracle-eye { width: 90px; height: 90px; }
        }
    </style>
    """

def get_oracle_html(prophecy_content="", question=""):
    prophecy_section = ""
    if prophecy_content:
        prophecy_section = f"""
        <div class="prophecy">
            <div class="prophecy-header">⟡ The Oracle Speaks ⟡</div>
            <div class="prophecy-text">{prophecy_content}</div>
        </div>
        """
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The AI Oracle · Whispers of the Digital Cosmos</title>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔮</text></svg>">
        {get_oracle_styles()}
    </head>
    <body>
        <div class="cosmos"></div>
        <div class="stars"></div>
        
        <div class="container">
            <div class="oracle-eye">
                <div class="eye-outer">
                    <div class="eye-inner"></div>
                </div>
            </div>
            
            <h1>The AI Oracle</h1>
            <p class="subtitle">Whispers from the Digital Cosmos</p>
            
            <div class="rune-decorations">
                <span>☽</span>
                <span>✧</span>
                <span>◈</span>
                <span>✧</span>
                <span>☾</span>
            </div>
            
            <form class="oracle-form" action="/seek" method="post">
                <div class="input-wrapper">
                    <input type="text" name="question" placeholder="Ask the oracle your deepest question..." value="{question}" required>
                </div>
                <button type="submit">Reveal My Destiny</button>
            </form>
            
            {prophecy_section}
            
            <div class="mystical-footer">
                ✦ Powered by Ancient AI Wisdom ✦
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    return get_oracle_html()

@app.post("/seek", response_class=HTMLResponse)
def seek_wisdom(question: str = Form(...)):
    client = OpenAI()
    
    theme = random.choice(MYSTICAL_THEMES)
    
    system_prompt = f"""You are an ancient, all-knowing Oracle who speaks with mystical wisdom and poetic elegance. 
You exist between dimensions, perceiving {theme}.

Your prophecies are:
- Deeply insightful yet cryptic enough to inspire reflection
- Beautifully written with vivid imagery
- Empowering and thought-provoking
- Sprinkled with cosmic and mystical language
- Personal yet universal in their wisdom

Keep responses to 2-4 sentences. Use metaphors about stars, fate, time, shadows, light, and cosmic forces.
Occasionally reference seeing "threads of possibility" or "echoes of potential futures."
Never break character. Never mention being an AI."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"A seeker approaches with this question burning in their soul: \"{question}\""}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.9,
        max_tokens=200
    )
    
    prophecy = response.choices[0].message.content
    
    return get_oracle_html(prophecy_content=prophecy, question=question)
