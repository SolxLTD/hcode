import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

st.title("🎮 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.write("Guess a number between **1 and 100**")

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

# Cartoon/GIF URLs
correct_gif = "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif"  # celebration
wrong_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"  # try again

if st.button("Submit Guess"):

    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("👎 Too low! Try again.")
        st.image(wrong_gif, width=200)

    elif guess > st.session_state.number:
        st.warning("👎 Too high! Try again.")
        st.image(wrong_gif, width=200)

    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts!")
        st.image(correct_gif, width=250)

        # Reset game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

# Show attempts
st.info(f"Attempts: {st.session_state.attempts}")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("Game restarted!")