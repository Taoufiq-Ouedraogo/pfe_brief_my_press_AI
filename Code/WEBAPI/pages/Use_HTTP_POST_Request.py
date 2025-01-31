import streamlit as st
import requests
from flask import Flask, request, jsonify


 


# Streamlit ###############################
st.set_page_config(
    page_title="HTTP POST Request",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


# Logo
st.sidebar.image("Code/WEBAPI/ressources/logo black.png", width=350, use_container_width=True) 
 

st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous. ")


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
    #if st.sidebar.button(a):
        #st.switch_page(page_dico[a])
        
  




MEDIAS = ['bmp_media1', 'bmp_media22']

def BmP_API_HTTP():
    print('------------------------------------------------------------------------', request.url)
    # Vérifier le token dans les en-têtes
    token = request.headers.get("id")
    
    if token not in MEDIAS:  # You can validate the token here
        return jsonify({"error": "Unauthorized"}), 401
    
    # Check if the text is provided
    data = request.json
    article = data.get("text")
    
    if not article:
        return jsonify({"error": "Text is required"}), 400
    
    return jsonify({
        'extractiveSummary': 'extractiveSummary',
        'abstractiveSummary': 'abstractiveSummary'
    })


print("-################################### Serveur Flask ok  ######################################@")








# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Documentation pour l'intégration Python</h2>", unsafe_allow_html=True)
st.markdown("---")



# API REST
st.header("🌐 Utilisation de l'API REST")


st.markdown(""" 
            
Cette page vous guide sur la manière d'utiliser notre API pour transformer vos articles en résumés en utilisant des requêtes HTTP POST. 
            
-----""")

st.success("Le serveur est lancé")






# 
st.markdown(""" 
----
#### ⚙️ Fonctionnement de l'API REST
            
Envoyez une requête HTTP POST avec un article à résumer. L'API vous renverra :
- 1 Résumé extractif: Points clés extraits directement du texte original.
- 1 Résumé abstractif: Version reformulée et synthétique du contenu.

----
""")
            


st.markdown(""" 

####  🔗 URL de l'API

Pour utiliser notre API, envoyez une requête POST à :
            
`http://127.0.0.1:8000/BmP_API_HTTP`
            
----
""")



st.markdown(""" 
#### 🔑 Authentification

Ajoutez un token (id) dans l'en-tête de la requête :
            
----
""")


# Deux colonnes
left, right = st.columns(2)

with left:
    
    # exemple requete
    st.markdown(""" #### 🔧 Exemple de requête""")

    st.code("""

    import requests
    import json


    def get_response_from_rest_api(text, id, url):
        # Contenu de l'article à résumer
        data = {"text": text}
            
        # Token d'authentification dans les headers
        headers = {"id": "bmp_media1"}

        # Faire la requête POST
        response = requests.post(url=url, json=data, headers=headers)
        print(response)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print("Erreur:", response.json())
            return None

    """)


    st.code("""

    text = \"""
            Accoudé à un bureau marqué du sceau présidentiel au cœur d’une salle bouillonnante remplie de supporteurs galvanisés, 
            puis dans le bureau Ovale, Donald Trump a savamment mis en scène ses premiers paraphes devant les caméras du monde entier, 
            lundi 20 janvier, au premier jour de son investiture. Réduction drastique de l’immigration, remise en cause du droit du sol 
            et des droits des personnes transgenres, retrait de l’Organisation mondiale de la santé ou encore de l’accord de Paris sur le
            climat… Le 47e président des Etats-Unis a signé une avalanche de décrets marquant une rupture brutale avec l’administration Biden.
            De nombreux juristes et acteurs de la société civile américaine estiment toutefois que plusieurs de ses décisions sortent de la 
            légalité ou seront inapplicables. Les démocrates dénoncent également des mesures menaçant les droits des minorités et l’Etat de droit.
            Cela entraîne, dès le lendemain du retour de Donald Trump au pouvoir, la relance de la bataille judiciaire, qui avait marqué son premier mandat.
    \"""

    id = "bmp_media1"
    url = "http://127.0.0.1:8000/Use_HTTP_POST_Request"

    response = get_response_from_rest_api(text, id, url)
    response['extractiveSummary'], response['abstractiveSummary']
    """)



with right:
    st.subheader("📦 Structure de la réponse")
    st.write("La fonction retourne un dictionnaire contenant les champs suivants :")
    st.code("""
{
    "extractiveSummary": "Résumé extractif...",
    "abstractiveSummary": "Résumé abstractif...", 
}
    """, language="json")
    st.write("""
    **Détails des champs :**
    - `extractiveSummary` : Points clés extraits directement du texte original.
    - `abstractiveSummary` : Version reformulée et synthétique du contenu. 

    ✅ Les fichiers audio peuvent être enregistrés ou directement utilisés dans des playlists.
    """)




# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 35px;'> 🚀 Commencez à intégrer l'API dans vos médias dès aujourd'hui ! </p>", unsafe_allow_html=True)


# Icônes avec liens et noms affichés en dessous
st.markdown("""
            
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

