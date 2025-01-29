import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

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
        
  



# Titre de la page
st.title("📊 Analytics des Articles et Résumés")


# Description section
st.markdown("""
--------           

###  ✨ Vue d'ensemble des performances de l'API

Cette page analytique vous plonge au cœur des performances de notre API en offrant une analyse détaillée des articles et de leurs résumés (extractifs et abstractifs). 

Chaque graphique vous permet de déceler les tendances et les variations des données, vous offrant une vue claire sur la qualité des résultats générés. Vous pourrez comparer les différentes approches de résumé et ajuster vos attentes selon les performances observées. En résumé, cet espace est un outil indispensable pour comprendre en profondeur le fonctionnement de notre API et vous assurer de son efficacité dans votre plateforme.
            
-------
""")





# Champ d'entrée pour l'ID
id_value = st.text_input('Entrez l\'ID de votre média:', value="exemple: bmp_media1")


# 'Code/WEBAPI/ressources/historique_articles.xlsx'
xl_file = 'https://raw.githubusercontent.com/Taoufiq-Ouedraogo/pfe_brief_my_press_AI/main/Code/WEBAPI/ressources/historique_articles.xlsx'

df = pd.read_excel(xl_file)
df['article_length'] = df['article'].apply(lambda x: len(str(x).split()))
df['extractiveSummary_length'] = df['extractiveSummary'].apply(lambda x: len(str(x).split()))
df['abstractiveSummary_length'] = df['abstractiveSummary'].apply(lambda x: len(str(x).split()))


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



        # Longueur moyenne des articles
        #st.subheader("Longueur moyenne des articles complets et des résumés")
        #kpi_df_m1 = kpi_df.melt(id_vars=['Nombre d\'articles'], 
         #                           value_vars=['Longueur moyenne des articles complets', 
          #                                      'Longueur moyenne des résumés extractifs', 
           #                                     'Longueur moyenne des résumés abstractifs'], 
            #                    var_name='Statistique', value_name='Valeur')

       # fig2 = px.bar(kpi_df_m1, y="Statistique", x="Valeur",  color="Statistique", 
        #            color_discrete_sequence=["purple", "green", "goldenrod"])

        #fig2.update_layout(width=1500, height=600)
        #st.plotly_chart(fig2)



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
