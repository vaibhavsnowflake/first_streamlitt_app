

#import snowflake connector and the libraries
import streamlit
import snowflake.connector
import pandas as pd
import requests
#for error handling
from urllib.error import URLError 

streamlit.title('My Parents Healthy Diner') 
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado-toast')
streamlit.text('🍌🥭 Build your own Shake🥝🍇')



my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#allows the user to select from a provided list
fruits_selected = streamlit.multiselect("select a fruit from the list",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the dataframe
streamlit.dataframe(fruits_to_show)

#New Section to display api response
streamlit.header("Fruityvice Fruit Advice!")
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
  
#won't run anything past this
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("This Fruit list contains")
streamlit.dataframe(my_data_rows) 

add_my_fruit_list = streamlit.text_input("what fruit would you like to add in the list")
streamlit.write('The user entered',add_my_fruit_list)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
