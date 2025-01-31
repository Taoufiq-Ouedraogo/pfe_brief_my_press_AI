import streamlit as st


st.set_page_config(
    page_title="Pricing",
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
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")


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
        
  

        





# Style CSS
st.markdown("""
<style>
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #4A90E2;
        margin-bottom: 1rem;
    }
    .sub-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: #333333;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    .price-box {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: inline-block;
        width: 90%;  
        margin: 10px;
    }
    .price-box:hover {
        background-color: #f0f0f0;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .price {
        font-size: 2rem;
        color: #4A90E2;
        font-weight: bold;
        margin-top: 10px;
        text-align: left;
    }
    .cta {
        font-weight: bold;
        color: #4A90E2;
        font-size: 1.25rem;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    ul li {
        margin-bottom: 10px;
    }
    ul li:before {
        content: "✔️ ";
        color: green;
    }

    .standard {
        background-color: #E0E0E0;  /* Gris clair pour Standard */
        color: #333333;  /* Texte sombre */
    }
    .premium {
        background-color: #A9D6E5;  /* Bleu pastel pour Premium */
        color: #2C3E50;  /* Bleu foncé pour le texte, contraste élégant */
        border: 1px solid #A9D6E5;  /* Bordure bleu pastel pour plus de cohérence */
    }
    .premium:hover {
        background-color: #80C1D1;  /* Légèrement plus foncé au survol pour un effet chic */
    }
</style>
""", unsafe_allow_html=True)



# Titre principal
st.markdown('<div class="title">💵 Pricing</div>', unsafe_allow_html=True)
st.markdown("""
Choisissez l’offre **Pay-As-You-Go** qui correspond à vos besoins : intégration autonome ou accompagnement complet. 
Nos solutions sont flexibles et conçues pour optimiser vos contenus.
""")


# Plans de tarification
plans = [
    {
        "name": "STANDARD : Intégration Autonome",
        "price": "0,20€ / Million de token",
        "features": [
            "Accès à l'outil pour les résumés extractifs, abstractifs et audios.",
            "Documentation technique détaillée.",
            "Tableau de bord dédié pour suivi des performances.",
            "Mises à jour régulières de l'API.",
        ],
        "advantages": [
            "Flexibilité : adaptation aux besoins spécifiques.",
            "Économie : idéal pour les équipes techniques existantes.",
            "Rapidité : intégration immédiate après souscription."
        ],
        "class": "standard"
    },
    {
        "name": "PREMIUM : Accompagnement clé en main",
        "price": "0,25€ / Million de token",
        "features": [
            "Support complet à l’intégration par BriefMyPress.",
            "Personnalisation avancée (design, format des résumés).",
            "Formation des équipes internes pour maximiser l'utilisation.",
            "Maintenance proactive et analyses avancées.",
        ],
        "advantages": [
            "Sérénité : gestion technique entièrement assurée.",
            "Optimisation : ajustements continus selon les retours utilisateurs.",
            "Impact immédiat : solution prête à l’emploi."
        ],
        "class": "premium"
    }
]


# Affichage des plans côte à côte
col1, col2 = st.columns(2)

with col1:
    # Affichage du plan Standard
    plan = plans[0]
    st.markdown(f"""
    <div class="price-box {plan['class']}">
        <div class="sub-title">{plan['name']}</div>
        <div class="price">{plan['price']}</div>
        <div class="description" style="font-size: 1.25rem; font-weight: bold; margin-top: 10px;">
            Caractéristiques principales :
        </div>
        <ul>
            {''.join([f"<li>{feature}</li>" for feature in plan['features']])}
        </ul>
        <div class="description" style="font-size: 1.25rem; font-weight: bold; margin-top: 10px;">
            Avantages pour le client :
        </div>
        <ul>
            {''.join([f"<li>{advantage}</li>" for advantage in plan['advantages']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Affichage du plan Premium
    plan = plans[1]
    st.markdown(f"""
    <div class="price-box {plan['class']}">
        <div class="sub-title">{plan['name']}</div>
        <div class="price">{plan['price']}</div>
        <div class="description" style="font-size: 1.25rem; font-weight: bold; margin-top: 10px;">
            Caractéristiques principales :
        </div>
        <ul>
            {''.join([f"<li>{feature}</li>" for feature in plan['features']])}
        </ul>
        <div class="description" style="font-size: 1.25rem; font-weight: bold; margin-top: 10px;">
            Avantages pour le client :
        </div>
        <ul>
            {''.join([f"<li>{advantage}</li>" for advantage in plan['advantages']])}
        </ul>
    </div>

  

    """, unsafe_allow_html=True)



# Titre de la section
"""----- """
st.markdown('<div class="sub-title">📦 Récapitulatif des Packages</div>', unsafe_allow_html=True)


# CSS pour styliser le tableau
st.markdown("""
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    th, td {
        text-align: left;
        padding: 10px;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f4f4f4;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
</style>
""", unsafe_allow_html=True)





# Tableau des fonctionnalités
st.markdown("""
<table>
    <thead>
        <tr>
            <th>Caractéristiques</th>
            <th>Package STANDARD</th>
            <th>Package PREMIUM</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Accès à l’API</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Personnalisation des résumés (longueur, style, ...) <br> et des audios (voix, intonation, ...)</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Documentation technique</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Support à l’intégration</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Personnalisation avancée</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Maintenance technique</td>
            <td>Par le client</td>
            <td>Gérée par BriefMyPress</td>
        </tr>
        <tr>
            <td>Suivi des performances</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Analyses avancées</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Formation des équipes</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Tarification</td>
            <td>Abonnement scalable basé sur le volume de requêtes</td>
            <td>Abonnement scalable basé sur le volume de requêtes <br> avec frais pour les services supplémentaires</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)





# Appel à l'action
st.markdown("""
<br> 
<div style="text-align: center; margin-top: 2rem;">
    <span class="cta">Besoin d'aide pour choisir un plan ?</span>  
    <br><br>
    <button style="padding: 10px 20px; font-size: 1rem; color: white; background-color: #4A90E2; border: none; border-radius: 5px; cursor: pointer;">
        Contactez-nous
    </button>
</div>
""", unsafe_allow_html=True)







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

