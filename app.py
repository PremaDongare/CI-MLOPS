import streamlit as st

# Streamlit UI
st.title("Power calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input

n=st.number_input("Enter an integer", value=1, step=1)

# calculate the result

square=n**2
cube=n**3
fifth_power = n**5

# Display

st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth_power of {n} is: {fifth_power}")