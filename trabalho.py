import streamlit as st

st.set_page_config(page_title="HairBloom", layout="centered")

# Inicializar estados
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False
if 'pontos' not in st.session_state:
    st.session_state.pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
if 'widget_key' not in st.session_state:
    st.session_state.widget_key = 0

def reset():
    st.session_state.start_clicked = False
    st.session_state.pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
    st.session_state.widget_key += 1  # Incrementa para forçar recriação dos widgets
    st.rerun()  # Força o reload da página

def calcular_pontos(textura, espessura, oleosidade, quimica, estado, frequencia, calor, objetivo):
    """Calcula os pontos baseado nas respostas"""
    pontos = {"hidratação": 0, "nutrição": 0, "reconstrução": 0}
    
    # Textura
    if textura in ["Cacheado", "Crespo"]:
        pontos["nutrição"] += 1
    
    # Espessura
    if espessura == "Finos":
        pontos["reconstrução"] += 1
    elif espessura == "Grossos": 
        pontos["nutrição"] += 1 
    
    # Oleosidade
    if oleosidade == "Seco":
        pontos["hidratação"] += 1 
    elif oleosidade == "Oleoso":
        pontos["nutrição"] -= 1 
    
    # Química
    if quimica == "Sim":
        pontos["reconstrução"] += 2 
    
    # Estado do cabelo
    if "Opaco e sem brilho" in estado:
        pontos["hidratação"] += 2 
    if "Embaraça fácil ou com frizz" in estado:
        pontos["nutrição"] += 2
    if "Quebradiço, pontas ralas" in estado:
        pontos["reconstrução"] += 2 
    if "Caindo ou quebrando com facilidade" in estado:
        pontos["reconstrução"] += 2 
    if "Elástico ao molhar" in estado:
        pontos["reconstrução"] += 3
    
    # Frequência de lavagem
    if frequencia == "Todos os dias":
        pontos["hidratação"] += 2
    elif frequencia == "Dia sim Dia não": 
        pontos["hidratação"] += 1 
    
    # Uso de calor
    if calor == "Todos os dias":
        pontos["reconstrução"] += 2
        pontos["nutrição"] += 1 
    elif calor == "Algumas vezes por semana":
        pontos["reconstrução"] += 1 
    
    # Objetivos
    if "Hidratar e dar brilho" in objetivo:
        pontos["hidratação"] += 2
    if "Reduzir o frizz" in objetivo:
        pontos["nutrição"] += 2
    if "Recuperar cabelo danificado" in objetivo:
        pontos["reconstrução"] += 2 
    if "Fortalecer e evitar quebra" in objetivo:
        pontos["reconstrução"] += 2
    if "Estimular crescimento" in objetivo: 
        pontos["reconstrução"] += 1 
        pontos["nutrição"] += 1 
    if "Definir cachos" in objetivo:
        pontos["nutrição"] += 1
        pontos["hidratação"] += 1 
    
    return pontos

if not st.session_state.start_clicked:
    st.title("🌸 HairBloom - Seu Cronograma Capilar Personalizado")
    st.write("Bem Vinda(o) ao HairBloom! Seu Cabelo, Seu Fio, Seu Cronograma.")
    if st.button("Começar"):
        st.session_state.start_clicked = True
        st.rerun()

else:
    st.header("Primeira Etapa: Descobrir Seu Tipo de Cabelo!")
    
    textura = st.radio(
        "Qual a textura do seu cabelo?", 
        ["Liso", "Ondulado", "Cacheado", "Crespo"],
        key=f"textura_{st.session_state.widget_key}"
    )
    
    espessura = st.radio(
        "Qual a espessura dos seus fios?", 
        ["Finos", "Médios", "Grossos"],
        key=f"espessura_{st.session_state.widget_key}"
    ) 
    
    oleosidade = st.radio(
        "Qual o nível de oleosidade do seu cabelo?", 
        ["Oleoso", "Seco", "Misto", "Normal"],
        key=f"oleosidade_{st.session_state.widget_key}"
    )
    
    quimica = st.radio(
        "Você tem química no cabelo?", 
        ["Sim", "Não"],
        key=f"quimica_{st.session_state.widget_key}"
    ) 
    
    st.header("Segunda Etapa: Entender o Estado do Seu Cabelo")
    estado = st.multiselect(
        "Selecione os sintomas que você percebe:", 
        [
            "Opaco e sem brilho",
            "Embaraça fácil ou com frizz",
            "Quebradiço, pontas ralas", 
            "Caindo ou quebrando com facilidade", 
            "Elástico ao molhar"
        ],
        key=f"estado_{st.session_state.widget_key}"
    )
    
    st.header("Terceira Etapa: Seus Hábitos")
    frequencia = st.radio(
        "Com que frequência você lava seu cabelo?", 
        ["Todos os dias", "Dia sim Dia não", "2 a 3 vezes por semana", "1 vez por semana"],
        key=f"frequencia_{st.session_state.widget_key}"
    ) 
    
    calor = st.radio(
        "Você usa fontes de calor? (chapinha, secador, babyliss)?", 
        ["Todos os dias", "Algumas vezes por semana", "Raramente", "Nunca"],
        key=f"calor_{st.session_state.widget_key}"
    ) 
    
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
        ],
        key=f"objetivo_{st.session_state.widget_key}"
    )
    
    st.header("Quinta Etapa: Orçamento") 
    orcamento = st.radio(
        "Até quanto você está disposto a investir no tratamento?", 
        ["Até R$ 100,00", "Entre R$ 100,00 e R$ 500,00", "Entre R$ 500,00 e R$ 1.000,00", "Mais de R$ 1.000,00"],
        key=f"orcamento_{st.session_state.widget_key}"
    )
    
    # Calcular pontos apenas uma vez baseado nas respostas atuais
    pontos_calculados = calcular_pontos(textura, espessura, oleosidade, quimica, estado, frequencia, calor, objetivo)
    
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
    
    if orcamento == "Até R$ 100,00":
        faixa = "baixo"
    elif orcamento == "Entre R$ 100,00 e R$ 500,00": 
        faixa = "medio"
    else: 
        faixa = "alto"
    
    st.header("Resultado do Seu Cronograma Personalizado") 
    
    etapas_ordenadas = sorted(pontos_calculados.items(), key=lambda x: x[1], reverse=True) 
    
    st.subheader("Prioridades do seu cabelo:") 
    for etapa, valor in etapas_ordenadas: 
        st.write(f"{etapa.capitalize()}: {valor} ponto(s)") 
    
    dias = ["Segunda", "Quarta", "Sexta"] 
    cronograma = {dia: etapas_ordenadas[i % 3][0] for i, dia in enumerate(dias)} 
    
    st.subheader("Cronograma Capilar Semanal:") 
    for dia, etapa in cronograma.items(): 
        st.write(f"{dia}: {etapa.capitalize()}") 
    
    st.subheader("Produtos Recomendados:") 
    for etapa in ["hidratação", "nutrição", "reconstrução"]: 
        st.write(f"**{etapa.capitalize()}:**")
        for produto in produtos[etapa][faixa]: 
            st.write(f"• {produto}") 
    
    st.divider()
    if st.button("Recomeçar", type="primary"):
        reset()
