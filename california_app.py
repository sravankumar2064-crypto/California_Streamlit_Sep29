import numpy as np
import joblib
import streamlit as st

obj = joblib.load('california.joblib')
model=obj['model']
cols = obj['columns']

st.title('california app')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} value:')
    In.append(v)

if st.button('Predict'):
    out=model.predict([In])
    st.success(f'The median House value is: {out}')