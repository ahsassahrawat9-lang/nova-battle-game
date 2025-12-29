import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Vibes Online", page_icon="🎧")

# 2. Spotify Dark Theme Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #282828;
        color: white;
        border-radius: 10px;
    }
    h1 { color: #1DB954; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 VIBES - Online Streaming")

# 3. Online Search Feature
st.write("### 🔍 Duniya ka koi bhi gaana dhoondo")
search_query = st.text_input("Gaane ka naam likho (e.g. Kesariya Lofi, Arijit Singh hits)...")

if search_query:
    st.write(f"Searching for: **{search_query}**")
    
    # Ye part aapke search query ko YouTube ke link mein badal deta hai
    search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
    
    st.info(f"Bhai, abhi hum is search ko filter kar rahe hain. Niche diye gaye player mein apni pasand ka link paste karke online suno!")

    # Online Link Input (Streamlit limitation ki wajah se direct search play ke liye ye best hai)
    online_link = st.text_input("YouTube ya MP3 link yahan paste karein:")
    
    if online_link:
        st.video(online_link) # Streamlit video player audio bhi support karta hai
        st.success("Enjoying the Vibes! ✨")

# 4. Default Online Hits (Always Working)
st.write("---")
st.write("### 🚀 Trending Online")
trending_songs = {
    "Kesariya (Official)": "https://www.youtube.com/watch?v=BddP6PYo2gs",
    "Heeriye": "https://www.youtube.com/watch?v=RLzC55ai0eo",
    "Apna Bana Le": "https://www.youtube.com/watch?v=EL7vshZ_Oos"
}

selection = st.selectbox("Trending se chuno:", list(trending_songs.keys()))
st.video(trending_songs[selection])

st.write("---")
st.write("Created by: **Ahsas Rawat** | Vibes Online v5.0")

Attachments area
Preview YouTube video Kesariya - Brahmāstra | Ranbir Kapoor, Alia Bhatt | Pritam | Arijit Singh | Amitabh Bhattacharya| 4KPreview YouTube video Kesariya - Brahmāstra | Ranbir Kapoor, Alia Bhatt | Pritam | Arijit Singh | Amitabh Bhattacharya| 4K

Preview YouTube video Heeriye (Official Video) Jasleen Royal ft Arijit Singh| Dulquer Salmaan| Aditya Sharma |Taani TanvirPreview YouTube video Heeriye (Official Video) Jasleen Royal ft Arijit Singh| Dulquer Salmaan| Aditya Sharma |Taani Tanvir

