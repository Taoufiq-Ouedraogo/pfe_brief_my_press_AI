import streamlit as st


st.set_page_config(
    page_title="Python API",
    layout="wide",  
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'About': "# BriefMyPress.AI This is an *extremely* cool app!"
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
st.header("🐍 Utilisation de la bibliothèque Python : [`bmp_lib`](https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library)")

st.code("pip install bmp_lib@git+https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library", language="bash")



st.markdown("""
Avec `bmp_lib`, vous pouvez :
- Générer des résumés **extractifs** et **abstractifs**.
- Convertir les résumés en **audio** (MP3).
- Intégrer nos services dans vos scripts ou applications Python.

-----
""")




# Deux colonnes
left, right = st.columns(2)

with left:
    st.subheader("📝 Documentation des entrées : `bmp_summaries_and_audio`")
    st.write("""
    La fonction `bmp_summaries_and_audio` accepte les paramètres suivants :
    
    - **`text`** : *(str)*  
      Le texte de l'article à résumer.  
      *(Exigence : le texte doit être en français et non vide.)*
      
    - **`mediaID`** : *(str)*  
      L'identifiant du média qui utilise cette fonction.  
      *(Exigence : l'identifiant doit être valide.)*

    ⚠️ **Notes importantes :**
    - Si un `mediaID` non valide est fourni, une erreur sera levée.
    - La langue principale du texte doit être le français pour garantir une analyse optimale.
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

st.markdown("---")



# Exemple d'utilisation
with st.expander("🔧 Exemple d'utilisation"):
    st.code("""
    from bmp_lib import bmp_summaries_and_audio

    text = "Votre article ici..."
    media_id = "bmp_media1"

    # Appel de la fonction
    result = bmp_summaries_and_audio(text, media_id)

    # Résultats
    print("Résumé extractif :", result["extractiveSummary"])
    print("Résumé abstrait :", result["abstractiveSummary"])

    """, language="python")



# Exemple de gestion des buffers audio
with st.expander("💾 Exemple d'enregistrement d'un buffer audio"):
    st.code("""
    # Appel de la fonction
    result = bmp_summaries_and_audio(text, media_id)

    # Enregistrement du buffer audio en MP3
    with open("audio_extractif.mp3", "wb") as f:
        f.write(result["extractiveAudioBuffer"].read())

    with open("audio_abstrait.mp3", "wb") as f:
        f.write(result["abstractiveAudioBuffer"].read())
            
    """, language="python")


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 BMP Media AI - Tous droits réservés</p>", unsafe_allow_html=True)


