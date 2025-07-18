
import streamlit as st

st.set_page_config(page_title="AI Агент Недвижимости", layout="centered")

st.title("🏠 AI Агент Недвижимости")
st.write("Здравствуйте! Я виртуальный помощник по недвижимости. Чем могу помочь?")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ваш вопрос:")

if user_input:
    if "квартира" in user_input.lower():
        response = "Вот 3 варианта:\n1. 2-комн. в Аликанте — 185.000€.\n2. 1-комн. в Марбелье — 169.000€.\n3. Апартаменты в Валенсии — 192.000€ с террасой."
    elif "доходность" in user_input.lower() or "инвестиции" in user_input.lower():
        response = "Средняя доходность аренды в Лиссабоне — 5.6% годовых. Хотите PDF с примерами?"
    elif "дом" in user_input.lower():
        response = "Вот один из домов в Андалусии: 3 спальни, бассейн, 310.000€, 12 мин от моря. Нужны ещё?"
    else:
        response = "Спасибо за вопрос! Уточните, пожалуйста, локацию и бюджет — я подберу варианты."

    st.session_state.messages.append(("Вы", user_input))
    st.session_state.messages.append(("AI Агент", response))

for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")
