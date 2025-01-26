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


st.sidebar.title("📚 Accès rapide")
st.sidebar.write("Explorez nos fonctionnalités via les onglets ci-dessous.")
st.sidebar.button("🌐 Tester l'API REST")
st.sidebar.button("🐍 Tester la bibliothèque Python")
st.sidebar.button("📊 Analytics")
st.sidebar.button("💵 Nos tarifs")




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
Explore the different pricing options available for our services.  
Our plans are tailored to meet a variety of needs:
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