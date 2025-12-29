   import streamlit as st
import random
import time

st.set_page_config(page_title="Nova Survival", page_icon="🔫")

# Game Styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 50px; font-size: 20px; }
    .status-box { padding: 10px; border-radius: 5px; text-align: center; color: white; }
    </style>
    """, unsafe_allow_name=True)

st.title("🔫 Nova Survival: Battle Zone")
st.write("---")

# Game State Initialization
if 'health' not in st.session_state:
    st.session_state.health = 100
    st.session_state.kills = 0
    st.session_state.enemy_pos = random.randint(1, 5)
    st.session_state.game_over = False

# Game Over Screen
if st.session_state.health <= 0:
    st.error(f"GAME OVER! Aapne {st.session_state.kills} enemies maare.")
    if st.button("Restart Mission"):
        st.session_state.health = 100
        st.session_state.kills = 0
        st.session_state.game_over = False
        st.rerun()
    st.stop()

# Battle Interface
col1, col2 = st.columns(2)
with col1:
    st.metric("❤️ Your Health", f"{st.session_state.health}%")
with col2:
    st.metric("🎯 Kills", st.session_state.kills)

# The "Battlefield"
battle_map = ["🌲", "🌲", "🌲", "🌲", "🌲"]
battle_map[st.session_state.enemy_pos - 1] = "🥷" # Enemy icon
st.header(f"Zone: {' '.join(battle_map)}")

st.write("---")
st.subheader("Action Karo!")

# Shooting Controls
pos = st.radio("Target Position select karo:", [1, 2, 3, 4, 5], horizontal=True)

if st.button("🔥 FIRE!"):
    if pos == st.session_state.enemy_pos:
        st.success("Badiya Shot! Enemy khatam! 💥")
        st.session_state.kills += 1
        st.session_state.enemy_pos = random.randint(1, 5) # New enemy spawns
    else:
        st.error("Nishana chook gaya! Enemy ne aap par goli chala di! 😵‍💫")
        st.session_state.health -= 20
        st.session_state.enemy_pos = random.randint(1, 5) # Enemy moves

# Instructions
with st.sidebar:
    st.header("How to Play")
    st.write("1. 🥷 Is icon ko dhoondo.")
    st.write("2. Uska position number select karo.")
    st.write("3. FIRE dabao!")
    st.write("4. Health 0 hone se pehle jitne mar sako maaro!")

