import streamlit as st
import pandas as pd
import numpy as np


## Title of the Application
st.title("My First Streamlit App")

## Display a Simple Text
st.write("This is a simple text")

## create a simple Dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

## Display the Dataframe
st.write("Here is a simple DataFrame:")
st.write(df)

## Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)