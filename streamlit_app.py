#My app for streamlit thinngys

import streamlit
import pandas as pd

streamlit.title("Smackkkkkkk bro")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header("Here we have my header")
streamlit.text("here we have some text")
streamlit.text("here we have another text")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
