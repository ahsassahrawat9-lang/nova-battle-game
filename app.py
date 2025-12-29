import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Nova Anime Battle", layout="wide")

# 2. Complete Visual Styling (Background & Text)
st.markdown("""
    <style>
    .stApp {
        background: url("https://wallpaperaccess.com/full/5501.jpg");
        background-size: cover;
        background-position: center;
        color: white;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.8) !important;
    }
    .st-emotion-cache-10trblm { color: gold !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Setup (Character & Inventory)
st.sidebar.image("https://www.pngarts.com/files/3/Goku-Transparent-Background-PNG.png", width=200)
st.sidebar.title("👤 Character: Goku (Super Saiyan)")

# Game State Logic
if 'health' not in st.session_state:
    st.session_state.health = 100
    st.session_state.kills = 0

st.sidebar.write("---")
st.sidebar.subheader("🎯 Stats")
st.sidebar.metric("❤️ HP", f"{st.session_state.health}%")
st.sidebar.metric("💀 Kills", st.session_state.kills)

st.sidebar.write("---")
weapon = st.sidebar.selectbox("🔫 Choose Your Weapon:", ["Blue Flame Draco AK47", "MP40 Cobra", "AWM Duke Swallowtail"])

# 4. Main Game Screen
st.title("🏯 Nova Anime x Free Fire Battle")
st.write("### Mission: Bermuda Under Attack!")

# Battle Area Image
st.image("https://i.ytimg.com/vi/W_zF865EwEY/maxresdefault.jpg", caption="Bermuda Warzone", use_container_width=True)

st.write("---")

# 5. Combat System
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Battle Zone")
    location = st.selectbox("Land/Attack at:", ["Clock Tower", "Factory", "Pochinok", "Bimasakti Strip"])
    
    if st.button(f"🔥 ATTACK WITH {weapon.split()[0]}!"):
        enemy_pos = random.choice(["Clock Tower", "Factory", "Pochinok", "Bimasakti Strip"])
        
        if location == enemy_pos:
            st.balloons()
            st.success(f"💥 HEADSHOT! You eliminated the enemy at {location} using {weapon}!")
            st.session_state.kills += 1
        else:
            st.error(f"❌ Missed! The enemy was hiding at {enemy_pos}. They hit you back!")
            st.session_state.health -= 25

with col2:
    st.subheader("🛡️ Battle Log")
    if st.session_state.health <= 0:
        st.error("💀 ELIMINATED! Your soul has left the battle.")
        if st.button("REDEPLOY (Respawn)"):
            st.session_state.health = 100
            st.session_state.kills = 0
            st.rerun()
    else:
        st.info(f"Keep fighting, {weapon.split()[0]} is ready!")

st.write("---")
st.write("Developed by: **Ahsas Rawat** | Engine: **Nova-Anime-v3**")


      
