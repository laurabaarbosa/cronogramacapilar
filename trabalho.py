import streamlit as st
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False
  def reset():
    st.session_state.start_clicked = False
    if not st.session_state.start_clicked:

st.set_page_config(page_title="HairBloom", layout="centered")
if not st.session_state.start_clicked:
    st.title("🌸 HairBloom - Seu Cronograma Capilar Personalizado")
    st.write("""
    Bem Vinda(o) ao HairBloom! Seu Cabelo, Seu Fio, Seu Cronograma.
    """)
  pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
    if st.button("Começar"):
        st.session_state.start_clicked = True
      else:
    st.header("Primeira Etaoa: Descobrir seu tipo de cabelo!")

textura = st.radio("Qual a textura do seu cabelo?", ["Liso", "Ondulado", "Cacheado", "Crespo"])
if textura in ["Cacheado", "Crespo"]:
    pontos["nutrição"] += 1
