import streamlit as st
from flask import Flask, request, jsonify


# pip install -r requirements.txt

st.set_page_config(
    page_title="HTTP POST Request",
    layout="wide",  
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")
st.sidebar.button("🌐 Tester l'API REST")
st.sidebar.button("🐍 Tester la bibliothèque Python")
st.sidebar.button("📊 Analytics")
st.sidebar.button("💵 Nos tarifs")




# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Documentation pour l'intégration Python</h2>", unsafe_allow_html=True)

st.markdown("---")


# Bibliothèque Python
st.header("🌐 Utilisation de l'API REST")





# URL de l'API
url = "http://127.0.0.1:6000/bmp_summaries_and_audio_rest_api"
url = "http://localhost:8501"



app = Flask(__name__)

@app.route('/api/summaries_and_audio', methods=['POST'])
def bmp_summaries_and_audio_restapi():
    # Vérifier le token dans les en-têtes
    token = request.headers.get("Authorization")
    
    if token != 'votre_token_attendu':  # Vous pouvez valider le token ici
        return jsonify({"error": "Unauthorized"}), 401
    
    # Vérifier que le texte est fourni
    data = request.json
    article = data.get("text")
    
    if not article:
        return jsonify({"error": "Text is required"}), 400
    
    # Préparer les résumés et les buffers audio (c'est un exemple, vous devez faire le traitement réel ici)
    return jsonify({
        'extractiveSummary': 'extractiveSummary',
        'abstractiveSummary': 'abstractiveSummary',
        'extractiveAudioBuffer': 'extractiveAudioBuffer',
        'abstractiveAudioBuffer': 'abstractiveAudioBuffer'
    })

if __name__ == '__main__':
    pass#app.run(debug=True, port=6000)

