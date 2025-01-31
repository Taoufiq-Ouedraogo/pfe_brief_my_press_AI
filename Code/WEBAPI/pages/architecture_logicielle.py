import streamlit as st


st.set_page_config(
    page_title="Architecture Logicielle",
    layout="wide", 
)  


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


# Logo use_container_width
st.sidebar.image("Code/WEBAPI/ressources/logo black.png", width=350, use_container_width=True) 
 

st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")

page_dico = {
    "🏠 Accueil": "Main_Page.py",
    "💵 Nos tarifs": "pages/Pricing.py",
    "📈 Analytics": "pages/Analytics.py",
    "🌐 Tester l'API REST": "pages/Use_HTTP_POST_Request.py",
    "🐍 Tester la bibliothèque Python": "pages/Use_Python_API.py",
    "🖥️ Architecture logicielle": "pages/architecture_logicielle.py",
}


for page_name, filepath in page_dico.items():
    st.sidebar.page_link(filepath, label=page_name)






# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Architecture Logicielle (BMP AI & Client)</h2>", unsafe_allow_html=True)

"----------------------------------"



st.image("Code/WEBAPI/ressources/archi_logicielle.png", use_container_width=True, width=2000)



# Icônes avec liens et noms affichés en dessous
st.markdown("""
-----
            
### 🌍 Retrouvez-nous sur :

<table style="width:100%; text-align:center;">
    <tr>
        <td>
            <a href="https://pypi.org/project/BmpLib-Ai/" target="_blank">
                <img src="https://fs.buttercms.com/resize=width:885/bswz3NJzT6WvKJHUc0Ii" alt="PyPI" width="200">
            </a><br>
            <a href="https://pypi.org/project/BmpLib-Ai/" target="_blank"><strong>PyPI</strong></a>
        </td>
        <td>
            <a href="https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="100">
            </a><br>
            <a href="https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library" target="_blank"><strong>GitHub</strong></a>
        </td>
        <td>
            <a href="https://brief-my-press-ai.streamlit.app/Use_Python_API" target="_blank">
                <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit" width="200">
            </a><br>
            <a href="https://brief-my-press-ai.streamlit.app/Use_Python_API" target="_blank"><strong>Streamlit</strong></a>
        </td>
    </tr>
</table>
""", unsafe_allow_html=True)


# Footer
st.markdown("<br><p style='text-align: center; font-size: 12px;'>© 2025 BMP Media AI - Tous droits réservés</p>", unsafe_allow_html=True)
