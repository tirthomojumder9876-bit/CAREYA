import streamlit as st

from services.auth.login_page import render_login_page



def main():
    st.set_page_config(
        page_icon="🏋️" ,
        page_title="YOUR PERSONAL GYM COACH",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    if not render_login_page():
        return

    st.write("Hello")

if __name__ == "__main__":
    main()