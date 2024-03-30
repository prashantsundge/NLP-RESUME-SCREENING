# Resume Screening App

This is a simple web application built using Streamlit that predicts the category of a resume based on its contents. It uses a K-Nearest Neighbors (KNN) classifier trained on TF-IDF features of different resume categories.

## Usage

1. Clone this repository:

2. Navigate to the project directory:

3. Install the required dependencies:

4. Run the Streamlit app:

5. Upload a resume file (supported formats: `.txt` and `.pdf`), and the app will predict its category based on its contents.

## Requirements

- Python 3.x
- Streamlit
- nltk
- scikit-learn

## Files

- `app.py`: Contains the Streamlit web application code.
- `best_knn_classifier.pkl`: Pickled KNN classifier trained on resume data.
- `tfidf.pkl`: Pickled TF-IDF vectorizer trained on resume data.
- `requirements.txt`: List of Python dependencies required for running the app.
- `README.md`: This file.

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [NLTK Documentation](https://www.nltk.org/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
