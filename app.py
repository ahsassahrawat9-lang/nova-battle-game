import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Free Fire Nova Edition", layout="wide")

# 2. Background Graphics (Bermuda Map Look)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpaperaccess.com/full/1213560.jpg");
background-size: cover;
}
[data-testid="stSidebar"] {
background-color: rgba(0, 0, 0, 0.7);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 3. Sidebar - Player & Weapon Skin
st.sidebar.image("https://pngimg.com/uploads/free_fire/free_fire_PNG53.png", caption="Character: ALOK")
st.sidebar.title("🎒 Inventory")
weapon = st.sidebar.selectbox("Gun Skin Chuno:", ["MP40 (Digital Infernus)", "AWM (Duke Swallowtail)", "AK47 (Blue Flame Draco)"])
st.sidebar.write(f"**Equipped:** {weapon}")

# Game Logic State
if 'health' not in st.session_state:
    st.session_state.health = 100
    st.session_state.kills = 0

st.sidebar.metric("❤️ HP", f"{st.session_state.health}%")
st.sidebar.metric("🎯 Kills", st.session_state.kills)

# 4. Main Game Screen
st.title("🔥 NOVA BATTLE ROYALE")
st.write(f"### Current Mission: Bermuda Survival")

# Map Graphics
st.image("https://i.ytimg.com/vi/W_zF865EwEY/maxresdefault.jpg", caption="Bermuda Map Locations", use_container_width=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 📍 Enemy Spotted!")
    target = st.radio("Kahan Fire karna hai?", ["Clock Tower", "Factory", "Pochinok", "Mars Electric"], horizontal=True)
    
    if st.button("🔥 SHOOT WITH " + weapon.split()[0]):
        enemy_hideout = random.choice(["Clock Tower", "Factory", "Pochinok", "Mars Electric"])
        
        if target == enemy_hideout:
            st.balloons()
            st.success(f"💥 BOOM! Headshot with {weapon} at {target}!")
            st.session_state.kills += 1
        else:
            st.error(f"❌ Miss ho gaya! Dushman {enemy_hideout} par tha.")
            st.session_state.health -= 25

with col2:
    st.write("### 🛡️ Status")
    if st.session_state.health <= 0:
        st.error("💀 ELIMINATED!")
        if st.button("RE-DEPLOY"):
            st.session_state.health = 100
            st.session_state.kills = 0
            st.rerun()
    else:
        st.info("Dhyan se! Zone chota ho raha hai.")

st.write("---")
st.write("Game created by: **Ahsas Sahrawat**")
