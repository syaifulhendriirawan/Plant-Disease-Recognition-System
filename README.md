# Plant Disease Detection

## Introduction
Plant Disease Detection is a deep learning-based system designed to help you quickly and accurately identify plant diseases. By simply uploading an image of your plant, our system analyzes it to detect signs of disease, enabling you to take timely action to protect your crops and ensure healthier harvests.

---

## How It Works

1. **Upload Image**: Navigate to the "Disease Detection" page and upload an image of the plant you suspect to be diseased.
2. **Analysis**: The system processes the image using advanced algorithms to identify potential diseases.
3. **Results**: View the analysis results along with recommendations for next steps.

---

## Dataset Information

- **Source**: The dataset is a restructured version created with offline augmentation from the original dataset, which can be found [here](https://github.com/spMohanty/PlantVillage-Dataset). 
- **Overview**: It contains approximately 87,000 RGB images of healthy and diseased crop leaves categorized into 38 classes.
- **Structure**: The dataset is split into:
  - Training set: 80%
  - Validation set: 20%
  - Test set: A separate directory with 33 images for prediction purposes.

---

## Features

- **Ease of Use**: User-friendly interface for uploading plant images.
- **Accuracy**: Leverages state-of-the-art deep learning algorithms for precise disease detection.
- **Recommendations**: Provides actionable insights for disease management.

---

## Technologies Used

- **Deep Learning Framework**: TensorFlow
- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Image Processing**: PIL

---

## Installation and Setup

1. Clone the repository:
   ```bash
   https://github.com/syaifulhendriirawan/Plant-Disease-Recognition-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Plant-Disease-Recognition-System
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Launch the application using the command above.
2. Upload an image of the plant in question.
3. Review the analysis results and recommended actions.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

We acknowledge the original creators of the dataset for their valuable contribution to the plant disease detection community.
# Plant-Disease-Recognition-System
