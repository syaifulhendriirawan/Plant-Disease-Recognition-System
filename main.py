import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "views/home.py",
    title="Home",
    default=True,
)
about_page = st.Page(
    "views/about.py",
    title="About",
)
disease_page = st.Page(
    "views/disease_recognition.py",
    title="Prediction",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(pages=[home_page, about_page, disease_page])


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")
st.sidebar.markdown("Made by Syaiful Hendri Irawan")


# --- RUN NAVIGATION ---
pg.run()