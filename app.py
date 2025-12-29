import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Vibes - Music for You", page_icon="🎧")

# 2. Spotify-inspired Dark Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #1db954, #121212);
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #282828;
        color: white;
        border-radius: 20px;
    }
    h1 {
        font-family: 'Arial Black';
        text-shadow: 2px 2px #000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. App Header
st.title("🎧 VIBES")
st.subheader("Your Playlist, Your Rules")

# 4. Search Bar
search_query = st.text_input("🔍 Search for a song or artist (e.g., Arijit Singh, Sidhu Moose Wala)...")

# 5. Music Data (Aap yahan aur links add kar sakte hain)
# Note: In links ko aap baad mein badal bhi sakte hain
songs = {
    "Vibe Check (Lofi)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Night Drive": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "Summer High": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    "Soulmate": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
}

# 6. Sidebar & Player Logic
st.sidebar.title("🎵 Vibes Library")
if search_query:
    st.write(f"Showing results for: **{search_query}**")
    # Yahan hum search results dikha rahe hain
    filtered_songs = [s for s in songs.keys() if search_query.lower() in s.lower()]
else:
    filtered_songs = list(songs.keys())

if filtered_songs:
    selected_song = st.sidebar.radio("Select to Play:", filtered_songs)
    
    # Player Interface
    st.write("---")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=500", caption="Now Playing", use_container_width=True)
    
    with col2:
        st.write(f"## {selected_song}")
        st.write("Artist: **Vibes Original**")
        st.audio(songs[selected_song])
        st.success("Gaana baj raha hai... Enjoy the vibes! ✨")
else:
    st.warning("Oops! Ye gaana abhi library mein nahi hai.")

st.write("---")
st.write("Created by: **Ahsas Sahrawat** | 🎵 Powered by Vibes Engine")
