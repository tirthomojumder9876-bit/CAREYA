import streamlit as st



def render_login_page():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("🏋️ Your Personal GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start. ")

    with st.form("login_form", clear_on_submit=False):
        username =st.text_input("Name (unique)", placeholder="unique name e.g. Tirtho")
        submit_button = st.form_submit_button("Start session", width="stretch")

    if submit_button:
        if not username:
            st.error("Please enter a valid username.")
            return False

        st.session_state["user_name"] = username
        st.session_state["user_id"] = "1"

        st.rerun()
            




    return False