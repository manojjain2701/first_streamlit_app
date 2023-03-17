import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣Oatmeal and resin Bread')
streamlit.text('🥗Kale Spinach and Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pickup Some Fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
