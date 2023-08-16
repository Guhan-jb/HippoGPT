import streamlit as st
import json
import requests

# Function to generate MCQs using ChatGPT
def generate_mcqs(content):
    api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your OpenAI API key
    }

    prompt = f"generate mcqs for the content given above:\n{content}"
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
        "top_p": 1.0,
        "n": 5,  # Number of MCQs to generate
        "stop": "\n"
    }

    response = requests.post(api_url, headers=headers, json=data)
    mcqs = response.json()["choices"][0]["text"]
    return mcqs

# Function to display MCQs and check user's answer
def display_mcqs(mcqs):
    questions = mcqs["questions"]
    total_questions = len(questions)
    correct_answers = 0

    st.write(f"Total MCQs: {total_questions}\n")

    for i, question in enumerate(questions):
        st.write(f"Question {i + 1}: {question['question']}")
        selected_option = st.radio("Options", question["options"])

        if selected_option == question["answer"]:
            st.write("Your answer is correct!")
            correct_answers += 1
        else:
            st.write("Your answer is wrong!")
            st.write(f"Correct answer: {question['answer']}")

        st.write("---")

    st.write(f"Correctly answered: {correct_answers}/{total_questions}")

# Main Streamlit code
st.title("MCQ Generator")

input_type = st.radio("Select input type", ["Passage", "PDF"])

if input_type == "Passage":
    passage = st.text_area("Enter the passage")
    if st.button("Generate MCQs"):
        mcqs = generate_mcqs(passage)
        mcqs_json = json.loads(mcqs)
        display_mcqs(mcqs_json)

else:
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        if st.button("Generate MCQs"):
            # Convert PDF to text
            # Perform text extraction from file_contents (use suitable library)
            # Assign extracted text to the 'passage' variable
            mcqs = generate_mcqs(passage)
            mcqs_json = json.loads(mcqs)
            display_mcqs(mcqs_json)
