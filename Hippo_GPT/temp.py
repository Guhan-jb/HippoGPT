import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
import nltk
import streamlit as st
nltk.download('stopwords')
nltk.download('punkt')

def summarize_pdf(file_path, num_sentences=3):
    # Read the PDF file
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""

        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequency
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_freq[word]
                else:
                    sentence_scores[sentence] = word_freq[word]

    # Select the top N sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Return the summary as a string
    summary = ' '.join(summary_sentences)
    return summary

# Example usage
# pdf_file_path = "d:/IONIX.pdf"
# summary = summarize_pdf(pdf_file_path)
# print(summary)
def main():
    st.title("Travel Planner AI")
    st.write("Enter your travel details below:")

    # User input form
    pdf = st.text_input("Enter the travel destination:")
    duration = st.number_input("Enter the duration of the trip (in days):", min_value=1, step=1)

    # Generate travel plan when user clicks the button
    if st.button("Generate Travel Plan"):
        if pdf and duration:
            plan = summarize_pdf(pdf, duration)
            st.subheader("summary:")
            st.markdown(plan, unsafe_allow_html=True)  # Use markdown to render the images
        else:
            st.warning("Please enter the travel destination and duration.")

if _name_ == "_main_":
   main()
