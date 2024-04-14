import urllib
from urllib.request import Request, urlopen
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import datetime
import pytz
from datetime import date

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    india_timezone = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india_timezone).time()
    today = date.today()
    today_name = today.strftime("%A")
    formatted_time = now.strftime("%H:%M:%S %Z")
    def Steps():
        #st.title("Steps to complete election duty peacfully")
        st.markdown(f'<h1 style="color:#D78A1B;font-size:20px;">{"શાંતિપુર્ણરીતે ચુટણી પ્રક્રીયા પુર્ણ કરવા માટે ના પગલા"}</h1>', unsafe_allow_html=True)

        st.image('po.jpg',use_column_width="wide")
        st.image('first_steps.jpg', use_column_width="wide")
        st.image('second_steps.jpg', use_column_width="wide")
        st.image('third_steps.jpg', use_column_width="wide")
        st.image('fourth_steps.jpg', use_column_width="wide")
        st.image('fifth_steps.jpg', use_column_width="wide")
    def Special_events():
        st.markdown(f'<h1 style="color:#A569BD;font-size:20px;">{"ચુંટણી દરમિયાનની ખાસ પરિસ્થિતીઓ મા શું કરવુ ?"}</h1>', unsafe_allow_html=True)
        st.image('special_event_1.jpg', use_column_width="wide")
        st.image('special_event_2.jpg', use_column_width="wide")
    def Receiving_centre():
        st.markdown(f'<h1 style="color:#28B463;font-size:20px;">{"રીસીવીંગ સેન્ટર મા જમા કરાવવાના કવરો ની તૈયારી"}</h1>',unsafe_allow_html=True)
        st.image('counter_1.jpg', use_column_width="wide")
        st.image('counter_2.jpg', use_column_width="wide")
        st.image('counter_3.jpg', use_column_width="wide")
        st.image('counter_4.jpg', use_column_width="wide")
        st.image('counter_5.jpg', use_column_width="wide")
    def Important_forms():
        st.title("Important forms for referance")
    #st.markdown(f'<marquee behavior="scroll" direction="left">Current_Time:{formatted_time},Today:-{today_name},Login_state:-{login_state},User_Name:{user_name}</marquee>', unsafe_allow_html=True)
    col1, col2, col3 ,col4 = st.columns(4)
    with col1:
        st.write(f"Last updated time: {formatted_time}")
    with col2:
        st.write(f"Today is: {today_name}")

    activity = ['Home', 'Election_24']

    # Define submenu options for each main menu option
    submenus = {
        'Home': None,
        'Election_24': ['Steps','Special_events','Receving_centre','Important_forms'],
    }

    # Get the selected main menu option
    selected_main_menu = st.sidebar.selectbox("Main Menu", activity)
    selected_submenu = None

    if selected_main_menu in submenus:
        # Check if submenus[selected_main_menu] is not None
        if submenus[selected_main_menu] is not None:
            selected_submenu = st.sidebar.selectbox("Submenu", submenus[selected_main_menu])
            st.write(f"You selected: {selected_main_menu} -> {selected_submenu}")
        else:
            st.write(f"No submenu options available for {selected_main_menu}")
    else:
        st.write(f"You selected: {selected_main_menu}")


    # Initialize selected_submenu to None
    # If the selected main menu option has submenus, display them


    if selected_main_menu=="Home":
        st_autorefresh(interval=30 * 1000, key="dataframerefresh")
        background_color = """
        <style>
        body {
            background-color: #008080; /* Replace with your desired color code */
        }
        </style>
        """

        st.markdown(background_color, unsafe_allow_html=True)
        st.markdown(f'<h1 style="color:#228b22;font-size:20px;">{"Welcome to Election24 Presiding help desk!!"}</h1>', unsafe_allow_html=True)

        # st.image('stock1.jpg', caption='Market at Home',use_column_width="wide")


    if selected_submenu == "Steps":
        Steps()
    elif selected_submenu == "Special_events":
        Special_events()
    elif selected_submenu == "Receving_centre":
        Receiving_centre()
    elif selected_submenu == "Important_forms":
        Important_forms()

    else:
        st.write(f"You selected: {selected_main_menu}")

if __name__ == "__main__":
    india_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(india_timezone).time()
    current_day = datetime.datetime.today().weekday()
    main()
