import streamlit as st
import pandas as pd
import random


def display_dataframe(conn):
    a=[[random.randint(0, 5000) for _ in range(30)] for _ in range(2)]

    data = conn.query("""SELECT tl.name as lead_name, tl.webpage, td.name, td.status as status FROM `tabLead` 
        as tl Left Join `tabToDo` as td on tl.name = td.reference_name 
        where td.reference_type = 'Lead' and tl.webpage is not null 
                      limit 2""")
    df = pd.DataFrame(data)
    df['activity']=[[5,3,4],[1,3,4,5,5]]
    df['td_count'] = [90, 100]
    df['views_history']=a
    # status = df.groupby(['lead_name', 'status']).size().unstack(fill_value= 0)
    # status_list = status.reset_index().values.tolist()
    # result_df = df.merge(pd.DataFrame(status_list, columns=['lead_name', 'status'] + status.columns.tolist()), on='lead_name', how='left')
    st.dataframe(df, width=50, height=250, use_container_width=True, hide_index=True, 
                 column_order = ['lead_name','webpage', 'activity', 'td_count', 'views_history'],
                 column_config={
                                "webpage": st.column_config.LinkColumn("webpage"),
                                "td_count": st.column_config.NumberColumn(
                                "td_count",
                                help="Number of stars on GitHub",
                                format="%d ⭐",),
                                "activity": st.column_config.LineChartColumn(
                                    "activity (past 30 days)", y_min=0, y_max=10
                                ),
                                "views_history": st.column_config.LineChartColumn(
                                    "Views (past 30 days)", y_min=0, y_max=5000
                                ),
                            })
    data = conn.query("""SELECT tl.name as lead_name, tl.webpage, COUNT(td.name) as td_count FROM `tabLead` 
        as tl Left Join `tabToDo` as td on tl.name = td.reference_name 
        where td.reference_type = 'Lead' and tl.webpage is not null
        GROUP BY tl.name""")
    
    df1 = pd.DataFrame(data)
    
    st.dataframe(df1, width=50, height=250, use_container_width=True, hide_index=True, 
                 column_order = ['lead_name','webpage', 'td_count'],
                 column_config={
                                "td_count": st.column_config.LineChartColumn(
                                    "td_count (past 30 days)", y_min=0, y_max=20
                                ),
                                })

    