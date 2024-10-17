import streamlit as st

st.title("Sum of 2 Numbers")

age1 = st.slider("Number", 0, 130, 25)
age2 = st.slider("Number 2", 0, 25)

sum = age2+age1
st.write("sum is", sum)