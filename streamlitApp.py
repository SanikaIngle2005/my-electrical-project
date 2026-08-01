import streamlit as st
import pandas as pd
st.title("Whats on your mind today?")
input_text = st.text_input("Ask anything")


#conditional logic with widgets

name = st .text_input("Enter your name:")
if st. button("Greet"):
   st.success(f"Hello, {name}!")    

upload_file = st.file_uploader("upload a csv",type='csv')
if upload_file:
   df = pd.read_csv(upload_file)
   st.dataframe(df)

st.header("This is a header")   
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, 'Code', [Link (https://stream.io)]")

st.text_input("What's your name?")
st.text_area("Write something ...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("choose a range",0,100)
st.selectbox("Select a fruit", ["Apple","Banana","Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("pick one", ["option A","option B"])
st.checkbox("I agree to the terms")

if st.checkbox("show Details"):
    st.info("Here are more details....")

option = st.radio("Choose view", ["show chart","show Table"])
if option =="Show chart":
      st.write("Chart would appear here")
else:
    st.write("Table would appear here")


with st.form("login_form"):
     uername = st.text_input("Username")
     password = st.text_input("Password", type="password")
     submitted = st.form_submit_button("Login")

     if submitted:
      st.success(f"welcome, {username}")

st.image("https://via.placeholder.com/300", caption="Sample Image")

st.video("https://www.youtube.com/watch?v=VqgUKExPvLY")


