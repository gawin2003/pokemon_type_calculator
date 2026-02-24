import streamlit as st
import json
types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison",
         "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Metal", "Fairy"]
type_chart = {}
for attack in types:
    type_chart[attack] = {}
    for defense in types:
        type_chart[attack][defense] = 1
with open("type_chart.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for attack in data:
    for defense in data[attack]:
        value = data[attack][defense]
        type_chart[attack][defense] = value
st.title("Pokemon Type Calculator")
attacker = st.selectbox("Select Attacker's type:", types)
defender = st.selectbox("Select Defender's type:", types)
if st.button("Calculate!"):
    multiplier = type_chart[attacker][defender]
    st.write(f"**Damage Multiplier: {multiplier}x**")
    if multiplier > 1.0:
        st.success("It's Super Effective!!")
    elif multiplier < 1.0 and multiplier > 0.0:
        st.warning("It's not very effective...")
    elif multiplier == 0.0:
        st.error("It had no effect!")
    else:
        st.info("Normal effectiveness.")
