import random
import streamlit as st
st.title("Welcome To The Number Guessing Game!")
st.info("the computer will pick a number and you have to guess it!")
userinput=st.text_input("enter a number")
number1=random.randint(1,10)
number=str(number1)
if st.button("Guess"):
	if userinput==number:
		st.success("You Guessed right!")
	else:
		st.info("You Guessed wrong! delete number and try again!")

