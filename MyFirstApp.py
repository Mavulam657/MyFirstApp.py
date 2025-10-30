import streamlit as st
st.title('My Streamlit App')
st.write('Hello World')
user_input = st.text_input("Enter a name","Mavula")
age = st.slider("Select your age",0,90,20)
if st.button("Submit"):
    st.write("Button Pressed")