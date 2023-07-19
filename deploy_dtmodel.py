import streamlit as st
import pickle

# Load the pickled model
with open('dt_regressor.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Diamond Price Model")

st.sidebar.header("This is a web app")

carat = float(st.number_input("Enter carat"))
cut = st.slider("Select cut to get yhat", 0, 4)
color = st.slider("Select color to get yhat", 0, 6)
clarity = st.slider("Select clarity to get yhat", 0, 7)



yhat_test = model.predict([[carat,cut,color,clarity]])


st.write("yhat test is", yhat_test)
