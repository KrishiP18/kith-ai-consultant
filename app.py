import streamlit as st
import openai

st.title("🧠 Kith AI Shopping Assistant")
st.write("Type what you're looking for — sneakers, hoodies, accessories, etc.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

query = st.text_input("What are you shopping for today?")

if query:
    with st.spinner("Searching for you..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Kith shopping assistant."},
                {"role": "user", "content": query}
            ]
        )
        st.write(response['choices'][0]['message']['content'])