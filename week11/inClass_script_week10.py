# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my app!')

st.header('Header')
st.subheader('subheader')

# add in images
st.subheader('Images')
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da', 
         width=200, 
         caption='A thinly veiled excuse for a derpy corgi.')

import numpy as np
img_data = np.random.random((200,200))
st.image(img_data, caption='random data')

st.header('Altair in Streamlit')

import altair as alt

mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

brush = alt.selection_interval(encodings=['x','y'])

chart1 = alt.Chart(mobility_url).mark_rect().encode(
    alt.X("Student_teacher_ratio:Q", bin=alt.Bin(maxbins=10)),
    alt.Y("State:O"),
    alt.Color("count()")
).properties(
   height=400
).add_selection(
        brush
)

chart2 = alt.Chart(mobility_url).mark_bar().encode(
    alt.X("Mobility:Q", bin=True,axis=alt.Axis(title='Mobility Score')),
    alt.Y('count()', axis=alt.Axis(title='Mobility Score Distribution'))
).transform_filter(
    brush
)

chart = (chart1.properties(width=300) | chart2.properties(width=300))

#chart

tab1, tab2 = st.tabs(['Mobility interactive', 'Other stuff'])

with tab1:
    st.altair_chart(chart, theme=None, use_container_width=True)


scatters = alt.Chart(mobility_url).mark_point().encode(
    x='Mobility:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q', scale=alt.Scale(scheme='sinebow'), bin=alt.Bin(maxbins=5))
)
#scatters
with tab2:
    st.altair_chart(scatters, theme=None, use_container_width=True)