import streamlit as st
from main import bot_query

# Function to simulate LLM response
def get_llm_response(question):

    # Replace this with your actual LLM response logic
    return f"Answer to: {bot_query(question)}"

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

st.title("SUVs")

# Text input for the user's question
user_input = st.text_input("Ask a question about SUVs:")

# If there's user input, process it
if user_input:
    response = get_llm_response(user_input)
    # Store the question and response in session state
    st.session_state.conversation.append((user_input, response))

# Display the conversation history
if st.session_state.conversation:
    for i, (question, answer) in enumerate(st.session_state.conversation):
        st.write(f"**Q{i+1}:** {question}")
        st.write(f"**A{i+1}:** {answer}")

