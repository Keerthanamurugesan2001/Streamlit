import streamlit as st
import numpy as np
import pandas as pd 
import altair as alt
import time

def display_text_element():
    st.title("title from Text Element")
    st.header('This is a header with a divider', divider='rainbow')
    st.subheader('Yep, the subheader :blue[cool]', anchor=False, help='Abc help', divider='orange')

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].
                
        Here's a bouquet &mdash;\
        :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:
        
                
        If you end a line with two spaces,
        a soft return is used for the next line.

        Two (or more) newline characters in a row will result in a hard return.''')
    
    md = st.text_area('Type your markdown string', """Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
            nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                 :hatched_chick::horse::bird::milky_way:
    """)
    st.markdown(md)

    st.caption("A <h1>Caption</h1>  fsfjdk :hatched_chick:", unsafe_allow_html=False, help=None)
    st.caption("A <h1>Caption</h1> fsfjdk :hatched_chick:", unsafe_allow_html=True, help=None)


    st.code("""
            #python
            print('hello world')""", language="python", line_numbers=False)
    st.code("""
            // javascript
            console.log('hello world')""", language="javascript", line_numbers=False)
    st.code("""
            // php
            echo('hello world')""", language="php")
    st.code("""
            // C
            #include <stdio.h>
            int main() {
            printf("Hello, World!");
            return 0;
            }""", language="c", line_numbers=True)
    st.code("""
            // JAVA
        class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!"); 
            }
        }""", language="java", line_numbers=True)
    st.divider()

    st.write("""Sometimes you want your Streamlit app to contain both your usual Streamlit graphic elements and the code that generated those elements. That's where st.echo() comes in.


             Ok so let's say you have the following file, and you want to make its app a little bit more self-explanatory by making that middle section visible in the Streamlit app""")
    with st.echo():
        def get_puncation():
            return '!!!'
        st.write(get_puncation())
        st.slider("This is a slider", 0, 100, (15))
        st.slider("This is a slider", 0, 100, (15,45))

    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

    st.text('This is some text.')