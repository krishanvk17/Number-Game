import random
import streamlit as st
number1=random.randint(1,100)
number=str(number1)
st.title("Welcome To The Number Guessing Game!")
st.info("the computer will pick a number and you have to guess it!")
st.info(number1)
userinput=st.text_input("enter a number")

if st.button("Guess"):
	if userinput==number:
		st.success("You Guessed right!")
	else:
		st.info("You Guessed wrong! delete number and try again!")
		if userinput<number:
			st.info("The number is higher than yours")
		else:
			st.info("The number is lower than yours")

