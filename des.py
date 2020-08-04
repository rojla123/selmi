
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import  os
import sqlite3
from pathlib import Path
import pandas as pd
import streamlit as st
import time
import numpy as np
def load_data():
    data=pd.read_csv('ammar.csv')
    return data
df=load_data()
st.sidebar.success("# L ecole nationale des sciences de l informatique")
st.success("# my first app" )
st.success(" # SELMI NIZAR")
st.video("3.Mp4")
# Create a list of possible values and multiselect menu with them in it.
COUNTRIES = df['location'].unique()
se = st.sidebar.multiselect('Select countries', COUNTRIES)
mask = df['location'].isin(se)
df=df[mask]
st.write(" # le nombre maximale de cases ",se ,df["total_cases"].max())
st.write(" # le nombre maximale de deaths ",se ,df["total_deaths"].max())
st.write(df)
if st.button('Say hello'):
  fig2 = px.area(df, x='date', y='total_cases',color='location')
  fig1= px.scatter(df, x='date', y='total_deaths',color='location')
  st.success(" # l volution de la pandemie_19 dans le monde")
  ts_chart = st.plotly_chart(fig2)
  st.success('# l volution de la pandemie_19 dans le monde')
  ts_char= st.plotly_chart(fig1)
  time.sleep(60) # This makes the function take 2s to run
  st.image("ensi.png")
pics = {
    "Cat":"https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg", 
    "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
    "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
}
for i in  list(pics.keys()):

     st.image(pics[i], use_column_width=True, caption=pics[i])
x=st.text_area("your comment")       
ret = st.radio('Select countries', ('help','contact'))   
a=st.slider("choose",1,8) 
a=st.button("valider")
if(st=="valider"):
   st.write("nizar selmi est u fondateur de rhrvgrveytvrygtrygtyrtyrytreytyrgtyrgtyrgtyregtgreytgryegtyregtyergeryyrygtyr") 

v=st.slider('hour',1,4,3)
db_loc = sqlite3.connect('Nizar.db')
cursor = db_loc.cursor()



if(ret=="contact"):
   name=x
   cursor.execute(''' insert into sel (?)''' ,values(name))
   cursor.execute('''SELECT * FROM sel;''')
   first_eleve = cursor.fetchone() # récupère le premier élève
   st.write(first_eleve) 
st.markdown('Streamlit is **_really_ cool**.')
map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)




