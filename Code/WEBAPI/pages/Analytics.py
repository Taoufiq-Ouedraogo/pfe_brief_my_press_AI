import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import openpyxl
import requests




st.set_page_config(
    page_title="Analytics",
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
paths = ["Code/WEBAPI/ressources/logo black.png", "/ressources/logo black.png"]
path = ""
for p in paths:
    if os.path.exists(p):
        path = p
        break
st.sidebar.image(path, width=350, use_container_width=True)

 

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



        
  



# Titre de la page
st.title("📊 Analytics")


# Description section
st.markdown("""
--------           

###  ✨ Vue d'ensemble des performances de l'API

Cette page analytique vous offre une vision approfondie des performances de notre API, en analysant les différents contenus générés.

<br>
            
🔹 Comparaison des méthodes : Évaluez les performances des différents formats de contenus pour affiner vos attentes.


🔹 Suivi des indicateurs clés (Taux de rebond, taux d'engagement):

- Mesurez l'interaction et l’engagement des utilisateurs avec les contenus générés. 
            
- Identifiez les améliorations pour optimiser l’expérience utilisateur.

- Inclus des fonctionnalités [Google Analytics](https://marketingplatform.google.com/about/analytics/).
    
-------
""", unsafe_allow_html=True)





# Champ d'entrée pour l'ID
id_value = st.text_input('Entrez l\'ID de votre média:', value="exemple: bmp_media1")


url = "https://raw.githubusercontent.com/Taoufiq-Ouedraogo/pfe_brief_my_press_AI/main/Code/WEBAPI/ressources/historique_articles.xlsx"
file_path = "historique_articles.xlsx"


# Télécharger le fichier
response = requests.get(url)
with open(file_path, "wb") as file:
    file.write(response.content)

df = pd.read_excel(file_path, engine="openpyxl")
df['mediaID'] = ['bmp_media1'] * len(df)

#df['article_length'] = df['article'].apply(lambda x: len(str(x).split()))
#df['extractiveSummary_length'] = df['extractiveSummary'].apply(lambda x: len(str(x).split()))
#df['abstractiveSummary_length'] = df['abstractiveSummary'].apply(lambda x: len(str(x).split()))


# Bouton pour appliquer le filtre
if st.button('Valider'):

    if id_value not in df['mediaID'].unique():
        pass

    else:
        # Filtrer selon l'ID renseigné
        df = df[df['mediaID'] == id_value]


        kpi_df = pd.DataFrame({
            'Nombre d\'articles': [len(df)],
            'Longueur moyenne des articles complets': [df['article_length'].mean().round().astype(int)],
            'Longueur maximale des articles complets': [df['article_length'].max()],
            'Longueur minimale des articles complets': [df['article_length'].min()],
            'Longueur moyenne des résumés extractifs': [df['extractiveSummary_length'].mean().round().astype(int)],
            'Longueur maximale des résumés extractifs': [df['extractiveSummary_length'].max()],
            'Longueur minimale des résumés extractifs': [df['extractiveSummary_length'].min()],
            'Longueur moyenne des résumés abstractifs': [df['abstractiveSummary_length'].mean().round().astype(int)],
            'Longueur maximale des résumés abstractifs': [df['abstractiveSummary_length'].max()],
            'Longueur minimale des résumés abstractifs': [df['abstractiveSummary_length'].min()]
        })



        # Titre principal de la section
        st.markdown("<h2 style='text-align:center; color:#4E4E4E;'> 📊 Longueur Moyenne des Articles et Résumés <br> <br> </h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            col1.metric("📄 Longueur moyenne des articles", f"{df['article_length'].mean():,.0f} caractères")
        with col2:
            col2.metric("📝 Longueur moyenne des résumés extractifs", f"{df['extractiveSummary_length'].mean():,.0f} caractères")
        with col3:
            col3.metric("🔍 Longueur moyenne des résumés abstractifs", f"{df['abstractiveSummary_length'].mean():,.0f} caractères")





        # Section pour les graphiques
        st.markdown("<h2 style='text-align:center; color:#4E4E4E;'>  <br> <br> 📈 Distribution des Longueurs <br> </h2>", unsafe_allow_html=True)

        # Plot des longueurs des articles et résumés
        fig1 = px.box(df, title=" ",
                    y=['article_length', 'extractiveSummary_length', 'abstractiveSummary_length'],
                    labels={'value': 'Longueur (caractères)', 'variable': 'Type'},
                    color='variable')

        # Mise à jour des couleurs pour chaque trace
        colors = ["purple", "green", "goldenrod"]
        for trace, color in zip(fig1.data, colors):
            trace.update(line=dict(color=color, width=3))

        # Mise à jour du layout du graphique
        fig1.update_layout(width=1500, height=700, title_x=0.5)
        st.plotly_chart(fig1)



        # Distribution des longueurs avec KDE (Kernel Density Estimation)
        columns = ['article_length', 'extractiveSummary_length', 'abstractiveSummary_length']
        kde = ff.create_distplot([df[col] for col in columns], 
                                group_labels=columns, show_hist=False, show_rug=False)

        # Mise à jour des couleurs pour le KDE
        for trace, color in zip(kde.data, colors):
            trace.update(line=dict(color=color, width=3))

        # Mise à jour du layout du graphique KDE
        kde.update_layout(title=" ", 
                        width=1500, height=700, 
                        xaxis_title="Longueur", 
                        yaxis_title="Densité", 
                        template="plotly_white", 
                        title_x=0.5)
        st.plotly_chart(kde)






        # Titre général des graphiques
        st.markdown("<h2 style='text-align:center; color:#4E4E4E;'>Analyse des Longueurs des Articles et Résumés</h2>", unsafe_allow_html=True)

        # Section pour les longueurs minimales
        st.markdown("<h3 style='color:#4E4E4E;'>🔽 Longueurs Minimales</h3>", unsafe_allow_html=True)

        # Affichage des graphiques dans des colonnes
        col1, col2, col3 = st.columns(3)
        with col1:
            c = 'Longueur minimale des articles complets'
            fig11 = px.pie(kpi_df, values=c, color_discrete_sequence=['purple'], hole=0.8, title=c)
            fig11.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig11.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig11, use_container_width=True)

        with col2:
            c = 'Longueur minimale des résumés extractifs'
            fig22 = px.pie(kpi_df, values=c, color_discrete_sequence=['green'], hole=0.8, title=c)
            fig22.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig22.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig22, use_container_width=True)

        with col3:
            c = 'Longueur minimale des résumés abstractifs'
            fig33 = px.pie(kpi_df, values=c, color_discrete_sequence=['goldenrod'], hole=0.8, title=c)
            fig33.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig33.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig33, use_container_width=True)

        # Section pour les longueurs maximales
        st.markdown("<h3 style='color:#4E4E4E;'>🔼 Longueurs Maximales</h3>", unsafe_allow_html=True)

        # Affichage des graphiques pour les longueurs maximales
        col1, col2, col3 = st.columns(3)
        with col1:
            c = 'Longueur maximale des articles complets'
            fig111 = px.pie(kpi_df, values=c, color_discrete_sequence=['purple'], hole=0.8, title=c)
            fig111.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig111.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig111, use_container_width=True)

        with col2:
            c = 'Longueur maximale des résumés extractifs'
            fig222 = px.pie(kpi_df, values=c, color_discrete_sequence=['green'], hole=0.8, title=c)
            fig222.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig222.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig222, use_container_width=True)

        with col3:
            c = 'Longueur maximale des résumés abstractifs'
            fig333 = px.pie(kpi_df, values=c, color_discrete_sequence=['goldenrod'], hole=0.8, title=c)
            fig333.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, font_size=20, showarrow=False)], width=400, height=400)
            fig333.update_traces(textinfo='value', textposition='outside', textfont_size=1)
            st.plotly_chart(fig333, use_container_width=True)




        # Titre général des graphiques
        st.markdown("<h2 style='text-align:center; color:#4E4E4E;'> Impact des contenus </h2>", unsafe_allow_html=True)
        coltps1, coltps2 = st.columns()
        with coltps1:
            figtps1 = go.Figure()

            # Avant intégration de BMP
            figtps1.add_trace(go.Scatter(
                x=list(range(1, 11)), 
                y=df["Temps avant BMP"],  
                fill='tozeroy', 
                mode='lines', 
                name="Avant intégration de BMP", 
                opacity=0.7,
                fillcolor="rgba(255, 0, 0, 0.6)",  # Red fill under the curve
                line=dict(color="red")
            ))

            # Après intégration de BMP
            figtps1.add_trace(go.Scatter(
                x=list(range(1, 11)), 
                y=df["Temps après BMP"], 
                fill='tonexty', 
                mode='lines', 
                name="Après intégration de BMP", 
                opacity=0.7,
                fillcolor="rgba(0, 128, 0, 0.3)",  # Green fill under the curve
                line=dict(color="green")
            ))

            # Update layout
            figtps1.update_layout(
                title="Temps de consommation des articles", 
                xaxis_title="Lecteur", 
                yaxis_title="Temps (s)", 
                template="plotly_white"
            )

            st.plotly_chart(figtps1, use_container_width=True)

        with coltps2:
            figtps2 = go.Figure()

            # Résumé Abstractif
            figtps2.add_trace(go.Scatter(
                x=list(range(1, 11)), 
                y=df["Temps Resumé Abstractif"], 
                fill='tonexty', 
                mode='lines', 
                name="Résumé Abstractif",
                line=dict(color="black"),
                fillcolor="rgba(0, 0, 0, 0.2)"  # Light Black between lines
            ))

            # Résumé Extractif
            figtps2.add_trace(go.Scatter(
                x=list(range(1, 11)), 
                y=df["Temps Resumé Extractif"], 
                fill='tonexty', 
                mode='lines', 
                name="Résumé Extractif",
                line=dict(color="purple"),
                fillcolor="rgba(128, 0, 128, 0.3)"  # Light Purple between lines
            ))

            # Chatbot
            figtps2.add_trace(go.Scatter(
                x=list(range(1, 11)), 
                y=df["Temps Chatbot"], 
                fill='tonexty', 
                mode='lines', 
                name="Chatbot",
                line=dict(color="orange"),
                fillcolor="rgba(255, 165, 0, 0.3)"  # Light Orange between lines
            ))

            # Update layout
            figtps2.update_layout(
                title="Temps de consommation après intégration de BMP",
                xaxis_title="Lecteur",
                yaxis_title="Temps (s)",
                template="plotly_white"
            )
            st.plotly_chart(figtps2, use_container_width=True)


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
