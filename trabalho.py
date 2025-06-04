import streamlit as st
st.set_page_config(page_title="HairBloom", layout="centered")
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False
if 'pontos' not in st.session_state:
    st.session_state.pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
def reset():
    st.session_state.start_clicked = False
    st.session_state.pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
if not st.session_state.start_clicked:
    st.title("🌸 HairBloom - Seu Cronograma Capilar Personalizado")
    st.write("Bem Vinda(o) ao HairBloom! Seu Cabelo, Seu Fio, Seu Cronograma.")
    if st.button("Começar"):
        st.session_state.start_clicked = True
else:
    st.header("Primeira Etapa: Descobrir Seu Tipo de Cabelo!")
    textura = st.radio("Qual a textura do seu cabelo?", ["Liso", "Ondulado", "Cacheado", "Crespo"])
    if textura in ["Cacheado", "Crespo"]:
        st.session_state.pontos["nutrição"] += 1
    st.write("Pontos atuais:", st.session_state.pontos) 
    if st.button("Voltar"):
        reset()

    espessura = st.radio("Qual a espessura dos seus fios?", ["Finos", "Médios", "Grossos"]) 
    if espessura in ["Finos"]:
        st.session_state.pontos["reconstrução"] +=  1
    elif espessura in ["Grossos"]: 
        st.session_state.pontos["nutrição"] += 1 

   
oleosidade = st.radio("Qual o nível de oleosidade do seu cabelo?", ["Oleoso", "Seco", "Misto", "Normal"])
if oleosidade == "Seco":
    st.session_state.pontos["hidratação"] += 1 
elif oleosidade == "Oleoso":
    st.session_state.pontos["nutrição"] -= 1 


quimica = st.radio("Você tem química no cabelo?", ["Sim", "Não"]) 
if quimica == "Sim":
    st.session_state.pontos["reconstrução"] += 2 

st.header("Segunda Etapa: Entender o Estado do Seu Cabelo")

estado = st.multiselect(
    "Selecione os sintomas que você percebe:", 
    [
        "Opaco e sem brilho",
        "Embaraça fácil ou com frizz",
        "Quebradiço, pontas ralas", 
        "Caindo ou quebrando com facilidade", 
        "Elástico ao molhar"
    ]
)

if "Opaco e sem brilho" in estado:
    st.session_state.pontos["hidratação"] += 2 

if "Embaraça fácil ou com frizz" in estado:
    st.session_state.pontos["nutrição"] += 2

if "Quebradiço, pontas ralas" in estado:
    st.session_state.pontos["reconstrução"] += 2 

if "Caindo ou quebrando com facilidade" in estado:
    st.session_state.pontos["reconstrução"] += 2 

if "Elástico ao molhar" in estado:
    st.session_state.pontos["reconstrução"] += 3


st.header("Terceira Etapa: Seus Hábitos")

frequencia = st.radio("Com que frequência você lava seu cabelo?", ["Todos os dias", "Dia sim Dia não", "2 a 3 vezes por semana", "1 vez por semana"]) 
if frequencia == "Todos os dias":
    st.session_state.pontos["hidratação"] += 2
elif frequencia == "Dia sim Dia não": 
    st.session_state.pontos["hidratação"] += 1 

calor = st.radio("Você usa fontes de calor? (chapinha, secador, babyliss)?", ["Todos os dias", "Algumas vezes por semana", "Raramente", "Nunca"]) 
if calor == "Todos os dias":
    st.session_state.pontos["reconstrução"] += 2
    st.session_state.pontos["nutrição"] += 1 
elif calor == "Algumas vezes por semana":
    st.session_state.pontos["reconstrução"] += 1 


st.header("Quarta Etapa: Seu Objetivo")

objetivo = st.multiselect(
    "Selecione os seus objetivos com o tratamento:",
    [
        "Hidratar e dar brilho", 
        "Reduzir o frizz",
        "Recuperar cabelo danificado",
        "Fortalecer e evitar quebra", 
        "Estimular crescimento",
        "Definir cachos"
    ]
)

if "Hidratar e dar brilho" in objetivo:
    st.session_state.pontos[hidratação] += 2
elif "Reduzir o frizz" in objetivo:
    st.session_state.pontos[nutrição] += 2
elif "Recuperar cabelo danificado" in objetivo:
    st.session_state.pontos[reconstrução] += 2 
elif "Fortalecer e evitar quebra" in objetivo:
    st.session_state.pontos[reconstrução] += 2
elif "Estimular crescimento" in objetivo: 
    st.session_state.pontos[reconstrução] += 1 
    st.session_state.pontos[nutrição] += 1 
elif "Definir cachos" in objetivo:
    st.session_state.pontos[nutrição] += 1
    st.session_state.pontos[hidratação] += 1 


st.header("Quinta Etapa: Orçamento") 
orcamento = st.radio("Até quanto você está disposto a investir no tratamento?", [
    "Até R$100,00", "Entre R$100 e R$500", "Entre R$500 e R$1000", "Mais de R$1000"
])

produtos = { 
    "hidratação": {
        "baixo": ["Máscara Skala Babosa", "Yamasterol Hidratação"],
        "medio": ["Lola Dream Cream", "Aussie Hidratação"],
        "alto": ["Kérastase Nutritive", "Moroccanoil Hydrating"] 

    },

    "nutrição": {
        "baixo": ["Óleo de coco Salon Line", "Skala Óleo de Rícino"], 
        "medio": ["Elseve Óleo Extraordinário", "Novex Óleo de Argan"],
        "alto": ["L'Oréal Absolut Repair", "Kérastase Elixir Ultime"]
    },

    "reconstrução": {
        "baixo": ["Gota Dourada Queratina", "Novex Queratina"],
        "medio": ["Lola Argan Oil", "Aussie Reconstructor"], 
        "alto": ["Joico K-Pak", "Kérastase Resistance"] 

    }
}

if orcamento == "Até R$100,00":
    faixa = "baixo"
elif orcamento == "Entre R$100 e R$500": 
    faixa = "medio"
else: 
    faixa = "alto"


st.header("Resultado do Seu Cronograma Personalizado") 
etapas_ordenadas = sorted(pontos.items(), key=lambda x: x[1], reverse=True) 

st.suheader("Prioridades do seu cabelo:") 
for etapa, valor in etapas_ordenadas: 
    st.write(f"**{etapa.capitalize()}**: {valor} ponto(s)") 


dias = ["Segunda", "Quarta", "Sexta"] 
cronograma = {dia: etapas_ordenadas[i % 3][0] for i, dia in enumerate(dias)} 

st.subheader("Cronograma Capilar Semanal:") 
for dia, etapa in cronograma.items(): 
    st.write(f"**{dia}**: {etapa.capitalize()}") 

st.subheader("Produtos Recomendados:") 
for etapa in ["hidratação", "nutrição", "reconstrução"]: 
    st.write(f***{etapa.capitalize()}**:") 
    for produto in produtos[etapa][faixa]: 
    st.write(f" {produto}") 
    



 
