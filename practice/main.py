import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv(filepath_or_buffer='happy.csv')
cols = df.columns.tolist()
updated_cols = [x.replace('_', ' ').title() for x in cols]

st.title('In Search for Happiness')
st.selectbox(label='Select data for X-axis', key='x', options=updated_cols)
st.selectbox(label='Select data for Y-axis', key='y', options=updated_cols)

x = st.session_state.x
index_of_x = updated_cols.index(x)
y = st.session_state.y
index_of_y = updated_cols.index(y)

st.subheader(body=f'{x} and {y}')
figure = px.scatter(data_frame=df, x=cols[index_of_x], y=cols[index_of_y], labels={'x': x, 'y': y})
st.plotly_chart(figure_or_data=figure)
