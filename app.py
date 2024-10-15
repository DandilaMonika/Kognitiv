import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

st.title("Welcome to Kognitiv")

df = pd.DataFrame({
  'ID Number': ['2200030118',
'2200030122',
'2200030329',
'2200030615',
'2200030730',
'2200030907',
'2200030970',
'2200030998',
'2200031093',
'2200031005',
'2200031176',
'2200031234',
'2200031331',
'2200031493',
'2200032689',
'2200080137',],
  'Name': ['T. Chandrika',
'G.Anusha',
'K.Sree Lekha',
'V.Sahithi',
'N Sri Venkata Sai Krishna',
'M. Venkata Sai Vamshi',
'Karthika Padala',
'Pulipati Yashakeerthi lasya',
'Monika Dandila',
'Sravan Kumar', 
'Rohini Reddy Ganta',
'Muppala Surya Theja',
'Penmetsa Mourya varma', 
'ADITYA VARDHAN',
'Mahi',
'Aravind Anubothu',
]
})

df