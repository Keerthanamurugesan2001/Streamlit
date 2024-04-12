import streamlit as st
from tutorial.constant import Tutorial
import pandas as pd

def _main():
   
    tut = Tutorial()
    content = ('Write',
               'Write Stream',
               'Magic',
               'Text Element',
               'Data Frame')
    with st.sidebar:
        option = st.selectbox(
            'Which secetion you want to see demo',
            content)

        st.write('You selected:', option)
    if option == 'Write':
        tut.display_content_write()
    elif option == 'Write Stream':
        tut.display_content_write_stream()
    elif option == 'Magic':
        tut.display_content_magic()
    elif option == 'Text Element':
        tut.display_text_element()
    elif option == 'Data Frame':
        tut.display_dataframe()

        
    # st.dataframe(df)
    # st.write("Here's our first attempt at using data to create a table:")
    # st.line_chart(df, x="employee", y="status", color=None, width=0, height=0, use_container_width=True)

    # # df = conn.query("select status, employee from `tabSales Invoice`")
    # # d = pd.DataFrame(df)
    # # st.line_chart(df, x="employee", y="status", color=None, width=0, height=0, use_container_width=True)
    # st.balloons()
    # st.snow()

    # st.write(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4])
    # map_data = pd.DataFrame(
    # np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    # columns=['lat', 'lon'])

    # st.map(map_data)

    # df = pd.DataFrame({
    # 'first column': [1, 2, 3, 4],
    # 'second column': [10, 20, 30, 40]
    # })

    # df

    # st.checkbox('Show dataframe')