import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt
import time

def display_content_write_stream(conn):
    _LOREM_IPSUM = """
        Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
        nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        """
    def stream_data():
        for word in _LOREM_IPSUM.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button('Stream'):
        st.write_stream(stream_data)

    # st.write_stream(lambda (x + " "): _LOREM_IPSUM.split(" "))

