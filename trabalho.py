import streamlit as st
st.set_page_config(page_title="HairBloom", layout="centered")
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False
def reset():
    st.session_state.start_clicked = False
pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
if not st.session_state.start_clicked:
    st.title("🌸 HairBloom - Seu Cronograma Capilar Personalizado")
    st.write("""
    Bem Vinda(o) ao HairBloom! Seu Cabelo, Seu Fio, Seu Cronograma.
    """)
    
    if st.button("Começar"):
        st.session_state.start_clicked = True
else:
    st.header("Primeira Etapa: Descobrir seu tipo de cabelo!")
    textura = st.radio("Qual a textura do seu cabelo?", ["Liso", "Ondulado", "Cacheado", "Crespo"])
    if textura in ["Cacheado", "Crespo"]:
        pontos["nutrição"] += 1
    if st.button("Voltar"):
        reset()

