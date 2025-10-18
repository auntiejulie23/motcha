import streamlit as st

import random

st.set_page_config(page_title="MoodBot 💬", page_icon="💬", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #f6f8fa;
    }
    .chat-bubble-user {
        background-color: #DCF8C6;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 80%;
        align-self: flex-end;
    }
    .chat-bubble-bot {
        background-color: #fff;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 80%;
        align-self: flex-start;
        border: 1px solid #ddd;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

quotes = {
    "sadness": [
        "🌙 Stars can’t shine without darkness.",
        "💙 You’ve survived 100% of your worst days.",
        "🌧️ Every storm runs out of rain."
    ],
    "anxiety": [
        "🌿 You don’t have to control your thoughts — just stop letting them control you.",
        "🫶 Breathe. You’re doing better than you think.",
        "☁️ One day at a time. You’ve got this."
    ],
    "fatigue": [
        "🌅 Even the sun takes a break every night.",
        "💤 Rest is productive too.",
        "🕯️ You don’t have to burn to keep others warm."
    ],
    "confidence": [
        "🔥 Act as if what you do makes a difference — it does.",
        "💪 You’ve got this — you always do.",
        "🌻 The version of you you’re becoming deserves your effort."
    ]
}

def get_emotion(text):
    text = text.lower()
    if any(word in text for word in ["sad", "down", "lonely", "depressed"]):
        return "sadness"
    elif any(word in text for word in ["anxious", "worried", "nervous", "stressed"]):
        return "anxiety"
    elif any(word in text for word in ["tired", "exhausted", "drained", "burnt"]):
        return "fatigue"
    elif any(word in text for word in ["happy", "confident", "excited", "motivated"]):
        return "confidence"
    else:
        return random.choice(list(quotes.keys()))

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hey there 👋 How are you feeling right now?"}
    ]

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-bubble-user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-bot">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

    if prompt := st.chat_input("How are you feeling right now?"):

if prompt.strip():
st.session_state.messages.append({"role": "user", "text": prompt})
emotion = get_emotion(prompt)
        quote = random.choice(quotes[emotion])
if emotion in QUOTES:
        st.session_state.messages.append({"role": "bot", "text": quote})
