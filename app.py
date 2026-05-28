import streamlit as st

st.title("🍔 Otsy Gestion")

st.subheader("📊 Rapport Journalier")
montant_z = st.number_input("Montant de l'État Z (DA)", min_value=0)
photo_z = st.file_uploader("Photo État Z", type=['png', 'jpg', 'jpeg'])

st.subheader("🛒 Achats et Dépenses")
montant_achat = st.number_input("Prix de l'achat (DA)", min_value=0)
photo_achat = st.file_uploader("Photo ticket achat", type=['png', 'jpg', 'jpeg'])

if st.button("ENVOYER LE RAPPORT"):
    st.success("✅ Données envoyées !")
  
