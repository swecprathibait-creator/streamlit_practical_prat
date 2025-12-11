import streamlit as st
import google.generativeai as genai
st.title("Meal Planner")
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (cm):")
location = st.text_input("Enter your location (city):")
constraints = st.text_area("Enter any dietary constraints (e.g., vegetarian, gluten-free):")
prompt = f"create a meal planner for a age {age}years old person and his weight is {weight}kg and height is {height} cm and he lives in {location} and he is {constraints}. you have to create a response as a table"
if st.button("Generate Meal Plan"):
    genai.configure(api_key = "AIzaSyALyms3r8_UzMWSgOli35W1qnVMUYIMr4M")
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    st.write(response.text)
