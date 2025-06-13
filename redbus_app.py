import pandas as pd
import numpy as np
import streamlit as st
from sqlalchemy import create_engine
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# create SQLAlchemy engine
engine = create_engine('postgresql://postgres:V%40risu18@localhost:5432/red_bus_off')

# query data from mysql database
query = "SELECT * FROM Bus"
data = pd.read_sql(query, engine)

# convert column to numeric datatype
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['seat_availability'] = pd.to_numeric(data['seat_availability'], errors='coerce')
data['star_rating'] = pd.to_numeric(data['star_rating'], errors='coerce')

# Main streamlit program
st.set_page_config(
    page_title="Redbus",
    page_icon=":redbus:",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FFFFFF;
        margin-right: 20px;
        border-right: 2px solid #F0F0F0
    }
</style>
""", unsafe_allow_html=True)

st.title(":red[RED BUS]") 
st.header("Best online ticket booking app")
st.text("EASY TO BOOK TICKET AND EASY TO TRAVEL AND HASSEL FREE JOURNEY")

# sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home', 'Search_Bus'],
        icons=['house-door-fill', 'search'],
        menu_icon='truck-front-fill',
        default_index=0,
        styles={
            "container": {'padding': '5!important', 'background-color': '#FAF9F6'},
            "icon": {'color': "#000000", "font-size": "23px"},
            "nav-link": {'font-size': '16px', 'text-align': 'left', 'margin': '0px', '--hover-color': '#EDEADE', 'font-weight': 'bold'},
            "nav-link-selector": {'background-color': '#E6E6FA', 'font-weight': 'bold'}
        }
    )

# home page
if selected == 'Home':
    st.subheader("India's No 1 online Bus Booking site ")
    st.markdown("""
    redBus is India's largest brand for online bus ticket booking and offers an easy-to-use online bus and 
    with over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, 
    redBus makes road journeys super convenient for travellers. A leading platform for booking bus tickets,
    redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.
    redBus offers bus tickets from some of the top private bus operators, such as Orange Travels, VRL Travels, SRS Travels, Chartered Bus, 
    and Praveen Travels, and state government bus operators, such as APSRTC, TSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, and more. With redBus, 
    customers can easily book bus tickets for different bus types, such as AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses, and more.
    """)
    st.image("https://newsroompost.com/wp-content/uploads/2020/05/redb.jpg",use_column_width=True)

# search Bus page 
if selected == "Search_Bus":
    # Initialize filters
    bustype_filter = st.multiselect('Select Bus Type:', options=data['bus_type'].unique())
    select_route = st.multiselect('Select Route:', options=data['route_name'].unique())
    price = st.slider('Select Price Range:', min_value=int(data['price'].min()), max_value=int(data['price'].max()), value=(int(data['price'].min()), int(data['price'].max())))
    star_filter = st.slider('Select Star Rating Range:', min_value=float(data['star_rating'].min()), max_value=float(data['star_rating'].max()), value=(float(data['star_rating'].min()), float(data['star_rating'].max())))
    availability = st.slider('Select Seat Availability Range:', min_value=int(data['seat_availability'].min()), max_value=int(data['seat_availability'].max()), value=(int(data['seat_availability'].min()), int(data['seat_availability'].max())))

    # filter data based on user inputs
    filter_data = data.copy() 

    if bustype_filter:
        filter_data = filter_data[filter_data['bus_type'].isin(bustype_filter)]

    if select_route:
        filter_data = filter_data[filter_data['route_name'].isin(select_route)]

    filter_data = filter_data[(filter_data['price'] >= price[0]) & (filter_data['price'] <= price[1])]
    filter_data = filter_data[(filter_data['star_rating'] >= star_filter[0]) & (filter_data['star_rating'] <= star_filter[1])]
    filter_data = filter_data[(filter_data['seat_availability'] >= availability[0]) & (filter_data['seat_availability'] <= availability[1])]

    # display filtered data
    st.write('Filtered Data:')
    st.dataframe(filter_data)

    # add a download button to export the filtered data
    if not filter_data.empty:
        st.download_button(
            label="Download Filtered Data",
            data=filter_data.to_csv(index=False),
            file_name="filter_data.csv",
            mime="text/csv"
        )
    else:
        st.warning("No data available with the selected filters.")