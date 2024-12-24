import streamlit as st
import random

st.title("Word Guessing Game")

if 'word' not in st.session_state:
    words = ['python', 'streamlit', 'hangman', 'challenge', 'programming']
    st.session_state.word = random.choice(words)
    st.session_state.guesses = ''
    st.session_state.turns = 7

word = st.session_state.word
guesses = st.session_state.guesses
turns = st.session_state.turns

display_word = ''.join([char if char in guesses else '_' for char in word])
st.write(f"Word: {display_word}")

guess = st.text_input("Guess a character:", max_chars=1)

if st.button('Submit Guess'):
    if guess:
        st.session_state.guesses += guess
        if guess not in word:
            st.session_state.turns -= 1

    if '_' not in display_word:
        st.success(f"You Win! The word is: {word}")
        st.session_state.word = random.choice(words)
        st.session_state.guesses = ''
        st.session_state.turns = 7
    elif st.session_state.turns == 0:
        st.error(f"You Lose! The word was: {word}")
        st.session_state.word = random.choice(words)
        st.session_state.guesses = ''
        st.session_state.turns = 7
    else:
        st.write(f"Wrong guess. You have {st.session_state.turns} more guesses.")

st.write(f"Guessed characters: {st.session_state.guesses}")