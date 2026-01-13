
import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Secret number (session me store hota hai)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Enter a number between 1 and 100", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too Low 🔽")
    elif guess > st.session_state.number:
        st.warning("Too High 🔼")
    else:
        st.success(f"🎉 You Won in {st.session_state.attempts} attempts!")
        
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0

# 🎲 Dice Game – Streamlit
# 🧠 Game idea
# Button dabao → dice roll hogi (1–6)
# Total score add hota rahega
# 6 aane par 🎉 Special win message
# import streamlit as st
# import random8p9

# st.title("🎲 Dice Rolling Game")

# Session state init
if "score" not in st.session_state:
    st.session_state.score = 0

if st.button("Roll Dice"):
    dice = random.randint(1, 6)
    st.write(f"🎯 Dice number: {dice}")

    st.session_state.score += dice

    if dice == 6:
        st.success("🎉 You got a 6! Lucky roll!")

st.write("🏆 Total Score:", st.session_state.score)

if st.button("Reset Game"):
    st.session_state.score = 0
    st.info("Game reset!")


# 🎮 AI Number Guessing Game (with Balloons)
# 🧠 Game Idea
# AI ek secret number (1–20) socheg
# Tum guess karogi
# Correct guess par 👉 🎈 Balloons flying effect
# AI hints dega: Too High / Too Low

# import streamlit as st
# import random

# st.title("🤖 AI Guessing Game")

# st.write("AI has selected a number between 1 and 20")

# # Session state setup
# if "ai_number" not in st.session_state:
#     st.session_state.ai_number = random.randint(1, 20)
#     st.session_state.attempts = 0
#     st.session_state.won = False

# guess = st.number_input(
#     "Enter your guess",
#     min_value=1,
#     max_value=20,
#     step=1
# )

# if st.button("Check"):
#     st.session_state.attempts += 1

#     if guess < st.session_state.ai_number:
#         st.warning("⬇ Too Low")
#     elif guess > st.session_state.ai_number:
#         st.warning("⬆ Too High")
#     else:
#         st.success(f"🎉 You WON in {st.session_state.attempts} attempts!")
#         st.balloons()   # 🎈🎈🎈 Balloons
#         st.session_state.won = True

# if st.button("Play Again"):
#     st.session_state.ai_number = random.randint(1, 20)
#     st.session_state.attempts = 0
#     st.session_state.won = False
#     st.info("New game started!")

# # Rock Paper Scissors (AI Game)
# import streamlit as st
# import random

# st.title("🤖 Rock Paper Scissors - AI Game")

# choices = ["Rock", "Paper", "Scissors"]

# # Session state
# if "user_score" not in st.session_state:
#     st.session_state.user_score = 0
#     st.session_state.ai_score = 0

# user_choice = st.selectbox("Choose your move", choices)

# if st.button("Play"):
#     ai_choice = random.choice(choices)

#     st.write("🧠 AI chose:", ai_choice)

#     if user_choice == ai_choice:
#         st.info("😐 It's a Draw")
#     elif (
#         (user_choice == "Rock" and ai_choice == "Scissors") or
#         (user_choice == "Paper" and ai_choice == "Rock") or
#         (user_choice == "Scissors" and ai_choice == "Paper")
#     ):
#         st.success("🎉 You WON!")
#         st.balloons()   # 🎈 Balloons on win
#         st.session_state.user_score += 1
#     else:
#         st.error("😢 AI WON!")
#         st.session_state.ai_score += 1

# st.write("🏆 Score")
# st.write("You:", st.session_state.user_score)
# st.write("AI:", st.session_state.ai_score)

# if st.button("Reset Game"): 
#     st.session_state.user_score = 0
#     st.session_state.ai_score = 0
#     st.info("Game reset!") 
# email address ((aditishrii2006@gmail).com')