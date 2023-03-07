import streamlit

streamlit.title('My Parents Healthy Diner') 
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado-toast')
streamlit.text('🍌🥭 Build your own Shake🥝🍇')


import pandas as pd

my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#allows the user to select from a provided list
streamlit.multiselect("select a fruit from the list",list(my_fruit_list.index),['Avacado','Strawberries'])

#display the dataframe
streamlit.dataframe(my_fruit_list)
