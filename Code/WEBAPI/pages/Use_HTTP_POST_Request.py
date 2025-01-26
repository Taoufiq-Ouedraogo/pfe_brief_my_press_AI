import streamlit as st
import requests
import threading
import os
import signal
import sys
from flask import Flask, request, jsonify

# URL for the Flask API (Replace with your production URL)
url = "https://brief-my-press-ai.streamlit.app/Use_HTTP_POST_Request"
MEDIAS = ['bmp_media1', 'bmp_media22']


# Flask API
app = Flask(__name__)


@app.route('/Use_HTTP_POST_Request', methods=['POST'])
def Use_HTTP_POST_Request():
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
        'abstractiveSummary': 'abstractiveSummary',
        'extractiveAudioBuffer': 'extractiveAudioBuffer',
        'abstractiveAudioBuffer': 'abstractiveAudioBuffer'
    })










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




# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Documentation pour l'intégration Python</h2>", unsafe_allow_html=True)
st.markdown("---")



# API REST
st.header("🌐 Utilisation de l'API REST")


st.markdown(""" 
            
Cette page vous guide sur la manière d'utiliser notre API pour transformer vos articles en résumés et 
fichiers audio en utilisant des requêtes HTTP POST. 
            
-----""")

            
#####################

# Start Flask API in a separate thread
def run_flask_app():
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=8000)


# Run Flask API in the background
#flask_thread = threading.Thread(target=run_flask_app)
#flask_thread.daemon = True  # Allow the thread to exit when the main program exits
#flask_thread.start()


st.markdown(""" 
### Lancez/Stoppez le serveur

""")

if st.button("Lancer le serveur"):
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()
    st.success("Le serveur Flask est lancé à http://127.0.0.1:8000/")

###############################



st.markdown(""" 
----
### Fonctionnement de l'API REST
            
Envoyez une requête HTTP POST avec un article à résumer. L'API vous renverra :
- 1 Résumé extractif: Points clés extraits directement du texte original.
- 1 Résumé abstractif: Version reformulée et synthétique du contenu.
- 2 Fichiers audio: Résumés convertis au format MP3.   

----
""")
            


st.markdown(""" 

#### URL de l'API

Pour utiliser notre API, envoyez une requête POST à :
            
`http://127.0.0.1:8000/Use_HTTP_POST_Request`
            
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

    get_response_from_rest_api(text, id, url)

    """)



with right:
    st.subheader("📦 Structure de la réponse")
    st.write("La fonction retourne un dictionnaire contenant les champs suivants :")
    st.code("""
{
    "extractiveSummary": "Résumé extractif...",
    "abstractiveSummary": "Résumé abstrait...",
    "extractiveAudioBuffer": "<buffer>",
    "abstractiveAudioBuffer": "<buffer>"
}
    """, language="json")
    st.write("""
    **Détails des champs :**
    - `extractiveSummary` : Points clés extraits directement du texte original.
    - `abstractiveSummary` : Version reformulée et synthétique du contenu.
    - `extractiveAudioBuffer` : Audio (MP3) du résumé extractif.
    - `abstractiveAudioBuffer` : Audio (MP3) du résumé abstrait.

    ✅ Les fichiers audio peuvent être enregistrés ou directement utilisés dans des playlists.
    """)




# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 35px;'> 🚀 Commencez à intégrer l'API dans vos médias dès aujourd'hui ! </p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 BMP Media AI - Tous droits réservés</p>", unsafe_allow_html=True)


