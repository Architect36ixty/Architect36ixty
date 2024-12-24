import random
import streamlit as st

st.title("Number Guessing Game")
st.write("Hi, welcome to the game! This is a number guessing game. You have 7 chances to guess the number. Let's start the game!")

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randrange(100)
    st.session_state.chances = 7
    st.session_state.guess_counter = 0

guess = st.number_input('Please Enter your Guess:', min_value=0, max_value=100, step=1)

if st.button('Submit Guess'):
    st.session_state.guess_counter += 1
    if guess == st.session_state.number_to_guess:
        st.success(f'The number is {st.session_state.number_to_guess} and you found it right in the {st.session_state.guess_counter} attempt!')
        st.session_state.number_to_guess = random.randrange(100)
        st.session_state.chances = 7
        st.session_state.guess_counter = 0
    elif st.session_state.guess_counter >= st.session_state.chances:
        st.error(f'Oops sorry, The number is {st.session_state.number_to_guess}. Better luck next time!')
        st.session_state.number_to_guess = random.randrange(100)
        st.session_state.chances = 7
        st.session_state.guess_counter = 0
    elif guess > st.session_state.number_to_guess:
        st.warning('Your guess is higher.')
    elif guess < st.session_state.number_to_guess:
        st.warning('Your guess is lesser.')