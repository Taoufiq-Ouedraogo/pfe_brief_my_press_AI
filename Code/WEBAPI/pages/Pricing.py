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
        "name": "Basic Plan",
        "price": "Free forever",
        "features": [
            "Essential features to get started",
            "No cost, no commitment"
        ]
    },
    {
        "name": "Pro Plan",
        "price": "$9.99/month",
        "features": [
            "Advanced features",
            "Priority support",
            "Enhanced customization"
        ]
    },
    {
        "name": "Enterprise Plan",
        "price": "Custom pricing",
        "features": [
            "Tailored solutions for businesses",
            "Dedicated account manager",
            "Custom integrations and support"
        ]
    }
]

# Affichage des plans
for plan in plans:
    st.markdown(f"""
    <div class="price-box">
        <div class="sub-title">{plan['name']}</div>
        <div class="price">{plan['price']}</div>
        <ul>
            {''.join([f"<li>{feature}</li>" for feature in plan['features']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Appel à l'action
st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <span class="cta">Need help choosing a plan?</span>  
    Reach out to us via the **Help** menu above!
</div>
""", unsafe_allow_html=True)