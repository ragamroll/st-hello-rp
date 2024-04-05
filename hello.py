import streamlit as st

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header[data-testid="stHeader"] {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

placeholder = st.empty()

actual_email = "email"
actual_password = "tBUqpHD5r8rZNjt"

_LOGIN=False
# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    #st.success("Login successful")
    _LOGIN=True
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass

if _LOGIN:
    st.write("Hello")
