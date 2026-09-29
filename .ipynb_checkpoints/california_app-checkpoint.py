import numpy as np
import joblib
import streamlit as st

obj = joblib.load('california.joblib')
model=obj['model']
columns = obj['columns']

st.title('californai app')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} value:')
    In.append(v)

if st.button('click'):
    st.success(In)