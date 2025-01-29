import streamlit as st


st.set_page_config(
    page_title="Main Page",
    layout="wide", 
)  


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


# Logo
st.sidebar.image("Code/WEBAPI/ressources/logo black.png", width=350) 
 

st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")

page_dico = {
    "🏠 Accueil": "Main_Page.py",
    "💵 Nos tarifs": "pages/Pricing.py",
    "📈 Analytics": "pages/Analytics.py",
    "🌐 Tester l'API REST": "pages/Use_HTTP_POST_Request.py",
    "🐍 Tester la bibliothèque Python": "pages/Use_Python_API.py",
}


for page_name, filepath in page_dico.items():
    st.sidebar.page_link(filepath, label=page_name)
    #if st.sidebar.button(a):
        #st.switch_page(page_dico[a])



# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Une solution IA pour simplifier la presse écrite</h2>", unsafe_allow_html=True)

"----------------------------------"


# Introduction
st.markdown("---")
st.markdown("""
### ✨ Bienvenue !
            
Brief My Press.AI est un outil IA sur-mesure conçue pour enrichir et adapter le contenu de presse écrite et ainsi favoriser sa consommation. 
        
Notre solution:
- Est destinée aux entreprises médiatiques (presses, revues scientifiques/spécialisées, ...)
- S’intègre facilement aux plateformes médias pour transformer la consommation de contenu
- Propose des **formats courts et simplifiés** (avec des résumés d’articles)
- Propose des **formats diversifiés** (texte, audio) pour les articles de presse écrite
""")


# Fonctionnalités
st.markdown("---")
st.markdown("### 🎯 Nos Fonctionnalités")

st.markdown("""
- **📝 Génération automatique de résumés d’articles de presse écrite** :  
    - 📌 **Résumé extractif** : extrait directement les points clés du texte original  
    - ✍️ **Résumé abstractif** : reformule et synthétise le contenu pour une compréhension claire et adaptée à chaque audience  

<br>

- **🔊 Génération automatique d’audios** : facilitant l’accès au contenu pour les utilisateurs qui préfèrent l’écoute  

<br>

- **🎵 Playlist personnalisable** : avec les audios des résumés pour une expérience continue et engageante  

<br>

- **🤖 Chatbot interactif** : pour tirer des connaissances plus précises sur les contenus  

<br>

- **📈 Suivi des performances des contenus** : incluant des statistiques sur l’impact des contenus et l’engagement utilisateur (temps d’écoute, articles consultés, ...)  
""", unsafe_allow_html=True)



# Modes d'accès
st.markdown("---")
st.markdown("### 🛠️ Comment accéder à nos services ? 2 méthodes")
st.markdown("""
1. **Bibliothèque Python** : intégrez nos fonctionnalités directement dans vos workflows Python.
2. **Requêtes HTTP POST** : utilisez notre API REST pour une intégration facile sur n'importe quelle plateforme.
""")

 

    



   

# Appel à l'action
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>🚀 Commencez dès aujourd'hui à transformer vos contenus !</h2>", unsafe_allow_html=True)
st.success("Cliquez sur les boutons dans la barre latérale pour démarrer avec BMP Media AI.")




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



