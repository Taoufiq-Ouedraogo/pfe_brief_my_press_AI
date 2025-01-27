import streamlit as st


st.set_page_config(
    page_title="Main Page",
    layout="wide"
)  


# Logo
st.sidebar.image("Code/WEBAPI/ressources/logo black.png", width=350) 

st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")

page_dico = {
    "🌐 Tester l'API REST": "pages/Use_HTTP_POST_Request.py",
    "🐍 Tester la bibliothèque Python": "pages/Use_Python_API.py",
    "📊 Analytics": "pages/Analytics.py",
    "💵 Nos tarifs": "pages/Pricing.py",
}

for a in page_dico.keys():
    if st.sidebar.button(a):
        st.switch_page(page_dico[a])
  


# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Une solution IA pour simplifier la presse écrite</h2>", unsafe_allow_html=True)

"----------------------------------"


# Introduction
st.markdown("---")
st.markdown("""
### ✨ Bienvenue !
BMP Media AI est une solution intelligente et sur-mesure qui simplifie et enrichit la consommation de contenu de presse écrite. Voici ce que nous proposons :
- **Formats courts et simplifiés** : obtenez des résumés clairs en quelques secondes.
- **Formats diversifiés** : vos articles peuvent être transformés en texte ou audio.
- **Playlists personnalisées** : créez des collections audio de vos résumés préférés.
- **Chatbot interactif** : explorez le contenu avec un chatbot et tirez des insights précis.
""")


# Modes d'accès
st.markdown("---")
st.markdown("### 🛠️ Comment accéder à nos services ?")
st.markdown("""
#### 🔗 Deux modes d'accès sont disponibles :
1. **Bibliothèque Python** : intégrez nos fonctionnalités directement dans vos workflows Python.
2. **Requêtes HTTP POST** : utilisez notre API REST pour une intégration facile sur n'importe quelle plateforme.
""")

 

    

# Fonctionnalités supplémentaires
st.markdown("---")
st.markdown("### 🎯 Fonctionnalités supplémentaires")
st.markdown("""
- **🎵 Playlist personnalisée** : Créez et téléchargez des listes audio basées sur vos résumés préférés.
- **🤖 Chatbot interactif** : Posez des questions et obtenez des informations enrichies sur les articles.
- **📊 Gestion des médias** : Visualisez les rapports d’utilisation et évaluez l’impact des contenus.
""")

   

# Appel à l'action
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>🚀 Commencez dès aujourd'hui à transformer vos contenus !</h2>", unsafe_allow_html=True)
st.success("Cliquez sur les boutons dans la barre latérale pour démarrer avec BMP Media AI.")



""" 
[GitHub Page](https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library)

[Pypi Page](https://pypi.org/project/BmpLib-Ai/)


[API Streamlit du Package Page](https://brief-my-press-ai.streamlit.app/Use_Python_API)
"""

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 BMP Media AI - Tous droits réservés</p>", unsafe_allow_html=True)



