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


st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")
st.sidebar.button("🌐 Tester l'API REST")
st.sidebar.button("🐍 Tester la bibliothèque Python")
st.sidebar.button("📊 Analytics")
st.sidebar.button("💵 Nos tarifs")





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


df = pd.read_excel('Code/WEBAPI/historique_articles.xlsx')
df['article_length'] = df['article'].apply(len)
df['extractiveSummary_length'] = df['extractiveSummary'].apply(len)
df['abstractiveSummary_length'] = df['abstractiveSummary'].apply(len)


# Bouton pour appliquer le filtre
if st.button('Valider'):

    if id_value not in df['mediaID'].unique():
        pass

    else:
        # Filtrer selon l'ID renseigné
        df = df[df['mediaID'] == id_value]


        kpi_df = pd.DataFrame({
            'Nombre d\'articles': [len(df)],
            'Longueur moyenne des articles': [df['article_length'].mean()],
            'Longueur maximale des articles': [df['article_length'].max()],
            'Longueur minimale des articles': [df['article_length'].min()],
            'Longueur moyenne des résumés extractifs': [df['extractiveSummary_length'].mean()],
            'Longueur maximale des résumés extractifs': [df['extractiveSummary_length'].max()],
            'Longueur minimale des résumés extractifs': [df['extractiveSummary_length'].min()],
            'Longueur moyenne des résumés abstractifs': [df['abstractiveSummary_length'].mean()],
            'Longueur maximale des résumés abstractifs': [df['abstractiveSummary_length'].max()],
            'Longueur minimale des résumés abstractifs': [df['abstractiveSummary_length'].min()]
        })



        # Affichage des graphiques
        fig1 = px.box(df, title="Longueurs des articles et résumés",
                    y=['article_length', 'extractiveSummary_length', 'abstractiveSummary_length'],
                    labels={'value': 'Longueur (caractères)', 'variable': 'Type'},
                    color='variable')

        colors = ["purple", "green", "goldenrod"]
        for trace, color in zip(fig1.data, colors):
            trace.update(line=dict(color=color, width=3))

        fig1.update_layout(width=1500, height=700)
        st.plotly_chart(fig1)



        # Distribution des longueurs des articles et résumés
        columns = ['article_length', 'extractiveSummary_length', 'abstractiveSummary_length']
        kde = ff.create_distplot([df[col] for col in columns], 
                group_labels=columns, show_hist=False, show_rug=False)

        for trace, color in zip(kde.data, colors):
            trace.update(line=dict(color=color, width=3))

        kde.update_layout(title="Distribution des longueurs des articles et résumés", width=1500, height=700,
            xaxis_title="Longueur", yaxis_title="Densité", template="plotly_white")
        st.plotly_chart(kde)



        # Longueur moyenne des articles
        st.subheader("Longueur moyenne des articles et des résumés")
        kpi_df_m1 = kpi_df.melt(id_vars=['Nombre d\'articles'], 
                                    value_vars=['Longueur moyenne des articles', 
                                                'Longueur moyenne des résumés extractifs', 
                                                'Longueur moyenne des résumés abstractifs'], 
                                    var_name='Statistique', value_name='Valeur')

        fig2 = px.bar(kpi_df_m1, y="Statistique", x="Valeur",  color="Statistique", 
                    color_discrete_sequence=["purple", "green", "goldenrod"])

        fig2.update_layout(width=1500, height=600)
        st.plotly_chart(fig2)





        # Plot des longueurs minimales
        c = 'Longueur minimale des articles'
        fig11 = px.pie(kpi_df, values=c, color_discrete_sequence=['purple'], hole=0.8, title=c)
        fig11.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig11.update_traces(textinfo='value', textposition='outside', textfont_size=1)


        c = 'Longueur minimale des résumés extractifs'
        fig22 = px.pie(kpi_df, values=c, color_discrete_sequence=['green'], hole=0.8, title=c)
        fig22.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig22.update_traces(textinfo='value', textposition='outside', textfont_size=1)  


        c = 'Longueur minimale des résumés abstractifs'
        fig33 = px.pie(kpi_df, values=c, color_discrete_sequence=['goldenrod'], hole=0.8, title=c)
        fig33.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig33.update_traces(textinfo='value', textposition='outside', textfont_size=1)  

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig11, use_container_width=True)
        with col2:
            st.plotly_chart(fig22, use_container_width=True)
        with col3:
            st.plotly_chart(fig33, use_container_width=True)




        # Plot des longueurs maximales
        c = 'Longueur maximale des articles'
        fig111 = px.pie(kpi_df, values=c, color_discrete_sequence=['purple'], hole=0.8, title=c)
        fig111.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig111.update_traces(textinfo='value', textposition='outside', textfont_size=1)


        c = 'Longueur maximale des résumés extractifs'
        fig222 = px.pie(kpi_df, values=c, color_discrete_sequence=['green'], hole=0.8, title=c)
        fig222.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig222.update_traces(textinfo='value', textposition='outside', textfont_size=1)  


        c = 'Longueur maximale des résumés abstractifs'
        fig333 = px.pie(kpi_df, values=c, color_discrete_sequence=['goldenrod'], hole=0.8, title=c)
        fig333.update_layout(annotations=[dict(text=str(kpi_df[c][0]), x=0.5, y=0.5, 
                        font_size=20, showarrow=False)], width=500, height=500)
        fig333.update_traces(textinfo='value', textposition='outside', textfont_size=1)  

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig111, use_container_width=True)
        with col2:
            st.plotly_chart(fig222, use_container_width=True)
        with col3:
            st.plotly_chart(fig333, use_container_width=True)





