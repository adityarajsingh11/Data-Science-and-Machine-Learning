import streamlit as st
import pandas as pd

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

options = ["Python", "JavaScript", "C++", "Java"]
favorite_language = st.selectbox("Select your favorite programming language:", options)
st.write(f"Your favorite programming language is {favorite_language}.")

if name:
    st.write(f"Hello, {name}!")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
