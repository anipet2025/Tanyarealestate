
import streamlit as st

st.set_page_config(page_title="AI Агент Недвижимости", layout="centered")

st.title("🏠 AI Агент Недвижимости")
st.write("Здравствуйте! Я виртуальный помощник по недвижимости. Чем могу помочь?")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ваш вопрос:")

if user_input:
    if "калаонда" in user_input.lower() or "эстепон" in user_input.lower():
        response = """Вот несколько актуальных вариантов с рынка:

1. **Calahonda, 2-комн. апартаменты**
   €329 000 • 87 м² • 400 м от моря  
   🌴 Урбанизация с бассейном и парковкой  
   [idealista.com/inmueble/123456](https://www.idealista.com/inmueble/123456)

2. **Elviria, 1-комн. с террасой**
   €289 000 • 70 м² • 2-й этаж, вид на море  
   🏖 До пляжа 5 мин, меблирована  
   [idealista.com/inmueble/123457](https://www.idealista.com/inmueble/123457)

3. **Estepona, 3-комн. в новом ЖК**
   €345 000 • 96 м² • с парковкой и охраной  
   🏢 ЖК 2021 года постройки  
   [idealista.com/inmueble/123458](https://www.idealista.com/inmueble/123458)

📩 Могу отправить PDF с подборкой на email или Telegram. Хотите?
"""
    else:
        response = "Спасибо за вопрос! Уточните, пожалуйста, локацию и бюджет — я подберу варианты."

    st.session_state.messages.append(("Вы", user_input))
    st.session_state.messages.append(("AI Агент", response))

for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")
