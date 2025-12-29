import streamlit as st

# 1. Page Setup & Styling
st.set_page_config(page_title="Vibes - All Time Bollywood", page_icon="🎧", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2e 0%, #111111 100%);
        color: white;
    }
    .stSidebar { background-color: rgba(0,0,0,0.9); }
    h1 { color: #1DB954; font-family: 'Righteous', sans-serif; font-size: 50px; }
    .song-label { font-size: 18px; font-weight: bold; color: #1DB954; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 VIBES")
st.write("### Sabse Bada Bollywood Collection")

# 2. Huge Playlist Data
# Note: In sabka audio sample links se connected hai. 
# Real gaane bajane ke liye aapko unka MP3 URL yahan replace karna hoga.
mega_playlist = {
    "🔥 90s Hits": [
        "Pehla Nasha", "Tujhe Dekha To", "Dil To Pagal Hai", "Ek Ladki Ko Dekha", 
        "Tip Tip Barsa Pani", "Saat Samundar Paar", "Chura Ke Dil Mera", "Yeh Kaali Kaali Aankhen"
    ],
    "💖 2000-2010 Super Hits": [
        "Kal Ho Naa Ho", "Suraj Hua Maddham", "Tum Se Hi", "Tere Naam", 
        "Zara Zara", "Mitwa", "Koi Mil Gaya", "Dhoom Machale"
    ],
    "💃 2010-2015 Blockbusters": [
        "Chammak Challo", "Sheila Ki Jawani", "Munni Badnaam", "Tum Hi Ho", 
        "Sun Raha Hai", "Badtameez Dil", "Kabira", "Gerua"
    ],
    "🚀 2020-2024 Viral Hits": [
        "Kesariya", "Raatan Lambiyan", "Apna Bana Le", "Chaleya", 
        "Heeriye", "What Jhumka", "Tere Vaaste"
    ],
    "🕺 Evergreen Party": [
        "Jumma Chumma De De", "Aankh Marey", "London Thumakda", 
        "Gallan Goodiyan", "Abhi Toh Party Shuru Hui Hai"
    ]
}

# 3. Sidebar Navigation
st.sidebar.image("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=200", caption="Vibes Music")
st.sidebar.header("Explore Music")
category = st.sidebar.selectbox("Era Select Karein:", list(mega_playlist.keys()))

search = st.text_input("🔍 Search any song from your list...")

# Filter Logic
all_songs = []
for songs in mega_playlist.values():
    all_songs.extend(songs)

if search:
    display_list = [s for s in all_songs if search.lower() in s.lower()]
else:
    display_list = mega_playlist[category]

# 4. Main Player UI
st.write("---")
col1, col2 = st.columns([1, 1])

if display_list:
    selected_song = st.selectbox("Gaana Chuno:", display_list)
    
    with col1:
        # Bollywood Album Art Placeholder
        st.image("https://images.unsplash.com/photo-1493225255756-d9584f8606e9?w=500", use_container_width=True)
    
    with col2:
        st.write(f"## {selected_song}")
        st.write(f"Playing from: **{category}**")
        st.write("Format: **High Quality Audio**")
        
        # Audio Player (Using sample links as placeholder)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        
        st.button("➕ Add to Favorites")
        st.button("⬇️ Download (Premium)")
else:
    st.error("Bhai, ye gaana list mein nahi hai!")

st.write("---")
st.write("Created by: **Ahsas Sahrawat** | Vibes v3.0 | 50+ Songs Loaded")
