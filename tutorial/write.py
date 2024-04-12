import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt


def display_content_write(conn):
    st.write('**```st.write()```**')
    st.write('Hello, *World!* :sunglasses:')
    
    st.write('Direct value from database')
    employee_data = conn.query("select * from `tabEmployee` limit 20")
    st.write(employee_data)

    st.write('Datafram from pandas')
    df = pd.DataFrame(employee_data[['status', 'employee_name']])
    st.write(df)

    st.write('With multiple arguments')
    st.write('1+1=', 2)
    st.write('The answer to life, the universe and everything is', 42)

    st.write("**Chart** using write")
    c=st.bar_chart(data=df, y='status', x='employee_name')
    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
    c=alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)