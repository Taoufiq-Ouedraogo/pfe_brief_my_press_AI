import streamlit as st


st.set_page_config(
    page_title="Python API",
    layout="wide",  
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'About': "# BriefMyPress.AI This is an *extremely* cool app!"
    }
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
        
  

st.markdown("""
    <style>
        .sidebar .sidebar-content .element-container {
            background-color: transparent;
        }
        .sidebar .sidebar-content .element-container:hover {
            background-color: #f0f0f0;
        }
        .sidebar .sidebar-content .element-container.selected {
            background-color: #2C3E50; /* Darker blue shade */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)



# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>BMP Media AI</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #555;'>Documentation pour l'intégration Python</h2>", unsafe_allow_html=True)

st.markdown("---")


# Bibliothèque Python
st.header("🐍 Utilisation de la bibliothèque Python : [`BmpLib-Ai`](https://github.com/Taoufiq-Ouedraogo/Brief-My-Press-AI-Library)")

st.warning("⚠️ Version de Python requise : >= 3.10, < 3.11")

st.code("pip install BmpLib-Ai", language="bash")




st.markdown("""
Avec `BmpLib-Ai`, vous pouvez :
- Générer des résumés **extractifs** et **abstractifs**.
- Convertir les résumés en **audio** (MP3).
- Configurer un chatbot pour mieux interroger les articles.
- Intégrer nos services dans vos scripts ou applications Python.
            
------
""")





# Deux colonnes
left, right = st.columns(2)

with left:
    st.subheader("📝 Documentation des entrées : `get_BMP_Article_Object`")
    st.write("""
    La fonction `get_BMP_Article_Object` accepte les paramètres suivants :
    
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
    st.write("La fonction retourne un objet `BMP_Object` contenant les attributs suivants :")
    st.code("""
            
        "content": Texte complet de l’article
            
        "extractiveSummary": Résumé extractif...
            
        "abstractiveSummary": Résumé abstractif...
            
        "extractiveAudioBuffer": Buffer audio MP3 du résumé extractif
            
        "abstractiveAudioBuffer": Buffer audio MP3 du résumé abstractif
            
        "chat_model": Modèle utilisé pour générer des réponses 
                        aux questions sur l’article
    
    """, language="json")


st.markdown("---")




# Description générale du projet
st.markdown("""
            
### 🌟 BMP_Object 🌟

Cette classe permet de générer des résumés **extractifs** et **abstractifs** à partir d'un article, ainsi que des versions audio de ces résumés. De plus, elle intègre un chatbot capable de répondre à des questions basées sur le contenu de l'article.

🔍 **Fonctionnalités principales** :
- **Génération de résumés** : Résumés extractifs et abstractifs.
- **Conversion audio** : Résumés convertis en fichiers audio (MP3).
- **Chatbot interactif** : Posez des questions à l'article et obtenez des réponses générées par un modèle AI.

""", unsafe_allow_html=True)





# get_summaries()
st.markdown("""
            
#### 🛠️ Méthodes accessibles
            
#### 1️⃣ `get_summaries()` : Résumés extractif et abstractif
            
Cette méthode retourne deux types de résumés générés à partir du texte de l'article :
- **Résumé extractif** : Il extrait les passages les plus importants de l'article.
- **Résumé abstractif** : Il reformule l'article pour générer un résumé condensé.

🔑 **Retour** : Un tuple contenant les deux résumés sous forme de chaînes de caractères (`str`).
""", unsafe_allow_html=True)



# get_audios()
st.markdown("""
            
#### 2️⃣ `get_audios()` : Buffers audio des résumés            
Cette méthode génère des fichiers audio pour les deux types de résumés. Les résumés sont convertis en audio à l'aide de la technologie Google Text-to-Speech (gTTS).

- **extractiveAudioBuffer** : Audio du résumé extractif.
- **abstractiveAudioBuffer** : Audio du résumé abstractif.

🔑 **Retour** : Un tuple contenant deux buffers audio (format MP3). 
            
Les utilisateurs peuvent ainsi écouter les résumés de manière pratique !

✅ Les fichiers audio peuvent être enregistrés ou directement utilisés dans des playlists.
""", unsafe_allow_html=True)



# chat_with_question()
st.markdown("""
            
#### 3️⃣ `chat_with_question()` : Interaction via un chatbot
Cette méthode permet à l'utilisateur de poser des questions sur le contenu de l'article. Le modèle chatbot génère une réponse en utilisant le texte complet de l'article comme contexte.

⚙️ **Paramètre** : 
- `question` (str) : La question que vous souhaitez poser à propos de l'article.

🔑 **Retour** : La réponse générée par le modèle sous forme de texte.

 ------           
""", unsafe_allow_html=True)




"### Utilisation"
st.code(""" import BmpLib_Ai as bmp """)

# Exemple d'utilisation
with st.expander("🔧 Exemple d'utilisation des résumés"):

    left, right = st.columns(2)

    with left:
        "##### Code"
        st.code("""
        import BmpLib_Ai as bmp
                
        text = \"""
                Accoudé à un bureau marqué du sceau présidentiel au cœur d’une salle bouillonnante remplie de supporteurs galvanisés, 
                puis dans le bureau Ovale, Donald Trump a savamment mis en scène ses premiers paraphes devant les caméras du monde entier, 
                lundi 20 janvier, au premier jour de son investiture. Réduction drastique de l’immigration, remise en cause du droit du sol et 
                des droits des personnes transgenres, retrait de l’Organisation mondiale de la santé ou encore de l’accord de Paris sur le 
                climat… Le 47e président des Etats-Unis a signé une avalanche de décrets marquant une rupture brutale avec l’administration Biden.
                De nombreux juristes et acteurs de la société civile américaine estiment toutefois que plusieurs de ses décisions sortent de la 
                légalité ou seront inapplicables. Les démocrates dénoncent également des mesures menaçant les droits des minorités et l’Etat de 
                droit. Cela entraîne, dès le lendemain du retour de Donald Trump au pouvoir, la relance de la bataille judiciaire, qui avait marqué 
                son premier mandat.
        \"""
                
        media_id = "bmp_media1"

        # Appel de la fonction
        bmp_object = bmp.get_BMP_Article_Object(text, media_id)

        # Résultats
        extractiveSummary, abstractiveSummary = bmp_object.get_summaries()
        print("Résumé extractif :", extractiveSummary)
        print("Résumé abstractif :", abstractiveSummary)

        """, language="python")

    with right:
        "##### extractiveSummary Output"
        st.code("""
        au cœur d’une salle bouillonnante remplie de supporteurs galvanisés, puis dans le bureau Ovale, Donald Trump
        a savamment mis en scène ses premiers paraphes devant les caméras du monde entier, lundi 20 janvier, au premier 
        jour de son investiture. Réduction drastique de l’immigration, remise en cause du droit du sol et des droits des 
        personnes transgenres, retrait de l’Organisation mondiale de la santé ou encore de l’accord de Paris sur le climat… 
        De nombreux juristes et acteurs de la société civile américaine estiment toutefois que plusieurs de ses décisions sortent de la 
        légalité ou seront inapplicables.
        """, language="json")

        "##### abstractiveSummary Output"
        st.code("""
        Donald Trump a savamment mis en scène ses premiers paraphes devant les caméras du monde entier, lundi 20 janvier, 
        au premier jour de son investiture . Le 47e président des Etats-Unis a signé une avalanche de décrets marquant une 
        rupture brutale avec l’administration Biden . De nombreux juristes et acteurs de la société civile américaine estiment 
        toutefois que plusieurs de ses décisions sortent de la légalité ou seront inappli
        """, language="json")





# Exemple de gestion des buffers audio
with st.expander("💾 Exemple d'enregistrement d'un buffer audio"):
    st.code("""
    # Appel de la fonction
    bmp_object = get_BMP_Article_Object(text, media_id)
    
    # Résultats
    extractiveAudioBuffer, abstractiveAudioBuffer = bmp_object.get_audios()
            
    # Enregistrement du buffer audio en MP3
    with open("audio_extractif.mp3", "wb") as f:
        f.write(extractiveAudioBuffer.read())

    with open("audio_abstractif.mp3", "wb") as f:
        f.write(abstractiveAudioBuffer.read())
            
    """, language="python")



# Chatbot
with st.expander("🤖 Exemple d'utilisation du Chatbot"):
    left, right = st.columns(2)


    with left:
        "##### Code"
        st.code("""
    # Appel de la fonction
    bmp_object = bmp.get_BMP_Article_Object(text, media_id)

    # Utilisez le chatbot pour poser une question
    response = bmp_object.chat_with_question("De qui parle le texte?")
    print('answer: ', response)
                
    response = bmp_object.chat_with_question('quels sont les dates mentionnées?')
    print('answer: ', response)
        """, language="python")


    with right:
        "##### Output"
        st.code("""
            Le texte parle de l'importance de l'intelligence artificielle dans la recherche moderne. 
        """, language="json")
   





"""
-----
### Modèles
"""


# Résumé extractif
st.markdown("""
#### 🔹 Résumé Extractif        

- **Modèle** : `fr_core_news_sm` de [spaCy](https://spacy.io/models/fr#fr_core_news_sm).
- **Fonctionnement** : Le modèle analyse le texte et extrait les phrases les plus significatives.
""")

# Résumé abstrait
st.markdown("""
#### 🔹 Résumé Abstrait

- **Modèle** : `Falconsai/text_summarization` de [Hugging Face](https://huggingface.co/Falconsai/text_summarization).
- **Fonctionnement** : Génération d'un résumé condensé du texte en utilisant un modèle de résumé abstrait.
""")

# Audio
st.markdown("""
#### 🔹 Audio 

- **Outil** : gTTS [Google Text-to-Speech](https://gtts.readthedocs.io/en/latest/).
- **Fonctionnement** : Convertit les résumés extraits et abstraits en fichiers audio pour une écoute rapide.
""")

# Chatbot
st.markdown("""
#### 🔹 Chatbot            

- **Modèle** : `mlx-community/Llama-3.2-1B-Instruct-4bit` de [Hugging Face](https://huggingface.co/mlx-community/Llama-3.2-1B-Instruct-4bit).
- **Fonctionnement** : Permet d'interagir avec le contenu de l'article pour obtenir des réponses précises aux questions.
""")




"""
-----
### Architecture de la Bibliothèque
"""

l, ll, r = st.columns(3)

with l:
    st.image("Code/WEBAPI/ressources/lib_python_tree.png", width=1000)

with r:
    st.markdown("""
    ##### Structure

    - **LICENSE** : Définit les termes de la licence d’utilisation du projet
    - **dist/** : Contient les fichiers de distribution du package
    - **pyproject.toml** : Contient la configuration moderne pour le projet
    - **requirements.txt** : Liste les dépendances nécessaires au projet
    - **src/** : Contient le code source de l’application ou bibliothèque
    - **BmpLib_Ai/** : dossier contenant les fichiers du package Python principal
    - **BmpLib_Ai.egg-info/** : contenant les métadonnées générées pour la distribution du package
    """)









# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 35px;'> 🚀 Commencez à intégrer l'API dans vos médias dès aujourd'hui ! </p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 BMP Media AI - Tous droits réservés</p>", unsafe_allow_html=True)


