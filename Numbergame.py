import random
import streamlit as st
st.title("Welcome To The Number Guessing Game!")
st.info("the computer will pick a number and you have to guess it!")
userinput=st.text_input("enter a number")
number=random.randint(1,100)
if st.button("Guess"):
	if userinput==random:
		st.success("You Guessed right!")
	else:
		st.info("You Guessed wrong! delete number and try again!")

