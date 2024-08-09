import plotly.express as px
import streamlit as st

from backend import get_data

st.title('Weather forecast for the next few days')
st.text_input(label='Place', placeholder='Enter city name...', key='place', help='Enter city name to get forecast')
st.slider(label='Forecast Days', min_value=1, max_value=5, key='days', help='Select number of days between 1 to 5')
st.selectbox(label='Select data to view', options=['Temperature', 'Humidity'], key='types')

place = st.session_state.place
days = st.session_state.days
types = st.session_state.types

if place:
    st.subheader(f'{types} for next {days} day(s) in {place.title()}')
    try:
        data = get_data(place)
        data = data[8 * days]
        if types == 'Temperature':
            temp = [x['main']['temp'] / 10 for x in data]
            dates = [x['dt_txt'] for x in data]
            figure = px.line(x=dates, y=temp, labels={'x': 'Date', 'y': 'Temperature (c)'}, title='Temperature vs Date')
            st.plotly_chart(figure_or_data=figure)
        else:
            sky_conditions = [x['weather'][0]['main'] for x in data]
            paths = []
            for condition in sky_conditions:
                paths.append(f'images/{condition.lower()}.png')
            st.image(image=paths, width=90)
    except KeyError:
        st.write('This place does not exist')
