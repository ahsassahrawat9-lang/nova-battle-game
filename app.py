import streamlit as st
import random

# Game Setup
st.set_page_config(page_title="Nova Survival", page_icon="🔫")
st.title("🔫 Nova Survival: Battle Royale")

# Game State Initialization
if 'health' not in st.session_state:
    st.session_state.health = 100
    st.session_state.kills = 0

# Score Dashboard
col1, col2 = st.columns(2)
with col1:
    st.write(f"### ❤️ Health: {st.session_state.health}%")
with col2:
    st.write(f"### 🎯 Kills: {st.session_state.kills}")

st.write("---")

# Battle Zone Logic
if st.session_state.health > 0:
    target_pos = st.selectbox("Dushman kahan hai? Position chuno:", [1, 2, 3, 4, 5])
    
    if st.button("🔥 FIRE!"):
        enemy_actual = random.randint(1, 5)
        if target_pos == enemy_actual:
            st.success("💥 Headshot! Dushman dher ho gaya!")
            st.session_state.kills += 1
        else:
            st.error("❌ Nishana chook gaya! Usne aapko goli maar di!")
            st.session_state.health -= 20
            st.rerun()
else:
    st.error("💀 GAME OVER! Aap mission mein shahid ho gaye.")
    if st.button("Restart Mission"):
        st.session_state.health = 100
        st.session_state.kills = 0
        st.rerun()

st.write("---")
st.info("Tip: Sahi position select karke fire dabao!")
