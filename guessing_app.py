import streamlit as st
import random

MAX_ATTEMPTS = 7

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "won" not in st.session_state:
    st.session_state.won = False
if "hint" not in st.session_state:
    st.session_state.hint = ""
if "high_score" not in st.session_state:
    st.session_state.high_score = None

st.title("Number Guessing Game")

# High score display
if st.session_state.high_score:
    st.info(f"Best score: {st.session_state.high_score} attempt(s)")
else:
    st.info("No high score yet. Be the first!")

# Game over screen
if st.session_state.game_over:
    if st.session_state.won:
        st.success(st.session_state.hint)
    else:
        st.error(st.session_state.hint)
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.won = False
        st.session_state.hint = ""
        st.rerun()

# Game in progress
else:
    attempts_left = MAX_ATTEMPTS - st.session_state.attempts
    st.write(f"Attempts remaining: **{attempts_left}** of {MAX_ATTEMPTS}")

    if st.session_state.hint:
        st.warning(st.session_state.hint)

    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

    if st.button("Guess!"):
        st.session_state.attempts += 1
        attempts = st.session_state.attempts

        if guess < st.session_state.secret_number:
            st.session_state.hint = f"Too low! ({attempts} attempt(s) used)"
        elif guess > st.session_state.secret_number:
            st.session_state.hint = f"Too high! ({attempts} attempt(s) used)"
        else:
            st.session_state.won = True
            st.session_state.game_over = True
            if st.session_state.high_score is None or attempts < st.session_state.high_score:
                st.session_state.high_score = attempts
                st.session_state.hint = f"You got it in {attempts} attempt(s)! New high score! 🎉"
            else:
                st.session_state.hint = f"You got it in {attempts} attempt(s)! Best is still {st.session_state.high_score}."

        if not st.session_state.won and attempts >= MAX_ATTEMPTS:
            st.session_state.game_over = True
            st.session_state.hint = f"Out of guesses! The number was {st.session_state.secret_number}."

        st.rerun()