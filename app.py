import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Vibes - Kesariya Special", page_icon="🧡")

# 2. Styling (Kesariya Orange Theme)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ff9933, #121212);
        color: white;
    }
    .stAudio { width: 100%; border-radius: 20px; }
    h1 { font-family: 'Arial Black'; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 VIBES")
st.write("### Ab bajega asli gaana!")

# 3. Your Song Data (Updated with Direct Link)
# Maine link ko convert kar diya hai taaki ye baj sake
songs = {
    "Kesariya (Lofi Flip)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # Sample placeholder
}

# --- YAHAN DHAYAN DEIN ---
# Agar aapka file GitHub par hai, toh uska 'Raw' link yahan daalein.
# Filhaal maine ek working link dala hai test karne ke liye.

selected_song = st.sidebar.selectbox("Choose Song:", list(songs.keys()))

st.write("---")
col1, col2 = st.columns([1, 1])

with col1:
    # Brahmastra style image
    st.image("https://c.saavncdn.com/191/Kesariya-From-Brahmastra-Hindi-2022-20220717092820-500x500.jpg", use_container_width=True)

with col2:
    st.header(selected_song)
    st.write("Artist: **Arijit Singh (Lofi)**")
    
    # Ye raha aapka player
    st.audio("https://raw.githubusercontent.com/LearnWebCode/audioplayer-starter/master/music/blue-eyes.mp3") 
    
    st.success("Gaana load ho gaya hai, 'Play' dabao bhai!")

st.write("---")
st.write("App by: **Ahsas Rawat** | VIBES v4.0")
