import streamlit as st
import requests
import threading
from flask import Flask, request, jsonify

# URL for the Flask API (Replace with your production URL)
url = "https://brief-my-press-ai.streamlit.app/Use_HTTP_POST_Request"
MEDIAS = ['bmp_media1', 'bmp_media22']


# Flask API
app = Flask(__name__)


@app.route('/Use_HTTP_POST_Request', methods=['POST'])
def bmp_summaries_and_audio_restapi():
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


# Start Flask API in a separate thread
def run_flask_app():
    app.run(debug=False, use_reloader=False)#, host="0.0.0.0", port=6000)






# Run Flask API in the background
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True  # Allow the thread to exit when the main program exits
    flask_thread.start()



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

    st.sidebar.title("📚 Accès rapide")
    st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")
    st.sidebar.button("🌐 Tester l'API REST")
    st.sidebar.button("🐍 Tester la bibliothèque Python")
    st.sidebar.button("📊 Analytics")
    st.sidebar.button("💵 Nos tarifs")


    # Title
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #555;'>Documentation pour l'intégration Python</h2>", unsafe_allow_html=True)
    st.markdown("---")
