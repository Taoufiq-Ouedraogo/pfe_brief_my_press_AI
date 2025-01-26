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



# Style de la page
st.markdown("""
<style>
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4A90E2;
        margin-bottom: 1rem;
    }
    .sub-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333333;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .price-box {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .price-box:hover {
        background-color: #f0f0f0;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .price {
        font-size: 1.25rem;
        color: #4A90E2;
        font-weight: bold;
    }
    .cta {
        font-weight: bold;
        color: #4A90E2;
    }
</style>
""", unsafe_allow_html=True)


# Titre principal
st.markdown('<div class="title">💵 Pricing</div>', unsafe_allow_html=True)
st.markdown("""
Découvrez nos plans tarifaires flexibles adaptés à vos besoins, allant de l’accès de base pour les petits projets à des solutions plus robustes pour les grandes entreprises. 

Vous pouvez choisir entre des options pay-as-you-go ou des abonnements mensuels en fonction de votre fréquence d’utilisation.
""")

# Plans de tarification
plans = [
    {
        "name": "STANDARD : Intégration Autonome",
        "price": "À partir de 99€/mois",
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
        ]
    },
    {
        "name": "PREMIUM : Accompagnement clé en main",
        "price": "Sur devis",
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
        ]
    }
]

# Affichage des plans
for plan in plans:
    st.markdown(f"""
    <div class="price-box">
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


# Contenu du tableau
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
            <td>Abonnement scalable basé sur le volume de requêtes avec frais pour les services supplémentaires</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)


# Appel à l'action
st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <span class="cta">Need help choosing a plan?</span>  
    Reach out to us via the **Help** menu above!
</div>
""", unsafe_allow_html=True)