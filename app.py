import streamlit as st

# 1. App ka Basic Setup
st.set_page_config(page_title="Vibes - Online Music", page_icon="🎵")

# 2. Design (Spotify Style)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #1DB954; }
    .stAudio { width: 100%; border-radius: 50px; }
    h1 { font-family: 'Trebuchet MS'; font-size: 45px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 VIBES")
st.write("---")

# 3. Gaano ki List (Yahan humne asli online links dale hain)
# Bhai, ye links maine check kiye hain, ye bajne chahiye.
songs = {
    "Kesariya (Lofi)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Sample Bollywood": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "Test Track": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
}

# Gaana choose karne ke liye menu
selected = st.selectbox("Apna Favorite Gaana Chuno:", list(songs.keys()))

# 4. Music Player Area
st.write(f"### 🎵 Abhi baj raha hai: {selected}")
st.image("

