import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Vitrine Ciclo de Vendas",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menu lateral (Sidebar) - nomes curtos e padronizados
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Navegue pelas opções:",
    [
        "Dashboard",
        "Clientes",
        "Produtos",
        "Propostas",
        "Pedidos",        # Menu padronizado e curto
        "Relatórios",
        "Configurações"
    ]
)

# Conteúdo dinâmico conforme o menu selecionado
if menu == "Dashboard":
    st.title("Bem-vindo ao Vitrine Ciclo de Vendas")
    st.success("Tudo centralizado para sua gestão comercial.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=120)
    st.info("Selecione um módulo no menu lateral para começar.")

elif menu == "Clientes":
    st.title("Cadastro e Consulta de Clientes")
    st.warning("Aqui futuramente você poderá cadastrar, editar e buscar clientes.")

elif menu == "Produtos":
    st.title("Catálogo de Produtos")
    st.warning("Em breve: gestão e atualização do portfólio de produtos.")

elif menu == "Propostas":
    st.title("Geração e Gestão de Propostas")
    st.success("Crie, edite, envie e acompanhe propostas comerciais de forma profissional.")

elif menu == "Pedidos":
    st.title("Geração e Gestão de Pedidos")   # Aqui sim, nome completo!
    st.success("Cadastre, edite e acompanhe todos os seus pedidos com agilidade e clareza.")
    st.write("Aqui você terá acesso à criação de novos pedidos, edição, filtros por status, relatórios e muito mais.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Pedidos Recentes")
        st.info("Tabela de pedidos será exibida aqui.")
    with col2:
        st.subheader("Novo Pedido")
        if st.button("Cadastrar Novo Pedido"):
            st.warning("Formulário de cadastro de pedido será exibido aqui.")

elif menu == "Relatórios":
    st.title("Relatórios e Indicadores")
    st.warning("Veja seus dados, indicadores e exporte relatórios.")

elif menu == "Configurações":
    st.title("Configurações")
    st.warning("Ajuste preferências, integrações e personalize o sistema.")

# Rodapé visual
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Vitrine Ciclo de Vendas • Acesse de qualquer dispositivo"
    "</div>",
    unsafe_allow_html=True
)
