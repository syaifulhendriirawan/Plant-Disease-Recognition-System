import streamlit as st

st.header("PLANT DISEASE RECOGNITION SYSTEM")
image_path = "assets/home.jpg"
st.image(image_path,use_column_width=True)
st.markdown("""
            ---

            ### Welcome to the Plant Disease Recognition System! 🌿🔍

            We're here to help you identify plant diseases quickly and accurately. Simply upload an image of your plant, and our system will analyze it to detect any signs of disease. Let’s work together to protect your crops and ensure a healthier harvest!

            ### How It Works
            1. **Upload Image**: Go to the Disease Recognition page and upload an image of the plant you suspect might be diseased.
            2. **Analysis**: Our system processes the image using advanced algorithms to identify potential diseases.
            3. **Results**: View the analysis results and get recommendations for further action.

            ### Why Choose Us?
            - **High Accuracy**: Our system uses cutting-edge machine learning techniques for precise disease detection.
            - **User-Friendly**: Simple and intuitive interface for a seamless user experience.
            - **Fast and Efficient**: Get results in seconds, allowing for quick decision-making.

            ### Get Started
            Click on the Disease Recognition page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

            ### About Us
            Learn more about the project, our team, and our goals on the About Us page.

            ---
            """)