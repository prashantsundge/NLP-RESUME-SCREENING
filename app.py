import streamlit as st
import pickle
import re
import nltk

# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf = TfidfVectorizer(stop_words='english')

nltk.download('punkt')
nltk.download('stopwords')


#Loading Models
clf =pickle.load(open('best_knn_classifier.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(text):

    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove non-alphanumeric characters and extra whitespaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    # Remove extra whitespaces
    text = re.sub(r"\s+", " ", text)
    # Remove hashtags (words starting with #)
    text = re.sub(r"#\w+", "", text)
    # Remove mentions (words starting with @)
    text = re.sub(r"@\w+", "", text)
    # Remove punctuation and special characters
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"[\n\t\r]", "", text)
    text = re.sub(r"\n", "", text)
    # Convert to lowercase
    text = text.lower()

    return text


#Web app
def main():
    st.title("Resume Screening App")
    upload_file = st.file_uploader("Upload Resume", type=['txt' , 'pdf'])

    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # if UTF-8 decoding fails try decoding with latin 1
            resume_text = resume_bytes.decode('latin-1')
        
        cleaned_resume= clean_resume(resume_text)
        #transformed the cleaned resume using the trained tfidvectorizer
        input_features = tfidfd.transform([cleaned_resume])
        # make the predictions using the loaded classifier
        prediction_id = clf.predict(input_features)[0]
        st.write(prediction_id)
        category_dict = {6: 'Data Science',
                        12: 'HR',
                        0: 'Advocate',
                        1: 'Arts',
                        24: 'Web Designing',
                        16: 'Mechanical Engineer',
                        22: 'Sales',
                        14: 'Health and fitness',
                        5: 'Civil Engineer',
                        15: 'Java Developer',
                        4: 'Business Analyst',
                        21: 'SAP Developer',
                        2: 'Automation Testing',
                        11: 'Electrical Engineering',
                        18: 'Operations Manager',
                        20: 'Python Developer',
                        8: 'DevOps Engineer',
                        17: 'Network Security Engineer',
                        19: 'PMO',
                        7: 'Database',
                        13: 'Hadoop',
                        10: 'ETL Developer',
                        9: 'DotNet Developer',
                        3: 'Blockchain',
                        23: 'Testing'}
                                
        category_name = category_dict.get(prediction_id , "Unknown")
        st.write("Predicted Category :  ",category_name)


  
        
#python  Mian 
if __name__ == "__main__":
    main()
