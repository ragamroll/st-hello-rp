import streamlit as st

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header[data-testid="stHeader"] {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.write("Hello RP")

with st.form(key="my_form"):
  username = st.text_input("Username")
  password = st.text_input("Password")
  st.form_submit_button("Login")

if 'user' not in st.session_state:
    st.session_state['user'] = username
if 'user' not in st.session_state:
    st.session_state['pass'] = password

st.write(st.session_state.user)
