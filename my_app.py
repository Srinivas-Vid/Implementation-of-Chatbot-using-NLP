import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("C:\\Users\\ERRAMALLA SRINIVAS\\Chat Bot using NLP\\chat_intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Global variables for enhanced features
session_memory = {"user_name": None, "chat_history": []}
counter = 0

def chatbot(input_text):
    input_text_vec = vectorizer.transform([input_text])
    tag = clf.predict(input_text_vec)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response, tag
    return "I'm not sure I understand that. Can you rephrase?", None

def main():
    global counter
    st.title("Gen Z Chatbot")
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Sidebar session information
    st.sidebar.header("Session Info")
    session_start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f"Session started: {session_start_time}")

    if choice == "Home":
        # User name collection
        if not session_memory["user_name"]:
            session_memory["user_name"] = st.text_input("What is your name?", key="user_name_input")
            if session_memory["user_name"]:
                st.success(f"Welcome, {session_memory['user_name']}! Let's chat.")
                st.sidebar.write(f"User: {session_memory['user_name']}")

        # Random welcome message
        welcome_messages = [
            "Did you know? Chatbots can save up to 30% of customer support costs!",
            "Hello! Ask me anything, and I'll try to help!",
            "Hi there! Looking forward to chatting with you!"
        ]
        st.info(random.choice(welcome_messages))

        # Chat interface
        user_input = st.text_input("You:", key=f"user_input_{counter}")
        if user_input:
            counter += 1
            response, tag = chatbot(user_input)

            # Store the conversation
            session_memory["chat_history"].append({"user": user_input, "chatbot": response})

            # Display response with highlighted keywords
            keywords = ["help", "chatbot", "assist", "thank you", "goodbye"]
            for keyword in keywords:
                response = response.replace(keyword, f"**{keyword}**")

            st.markdown(f"**Chatbot:** {response}")

            # Feedback mechanism
            feedback = st.radio(f"Was this response helpful?", ["Yes", "No"], key=f"feedback_{counter}")
            if feedback == "Yes":
                st.success("Thanks for your feedback!")
            else:
                st.warning("Sorry! I'll try to improve.")

            # Session statistics
            st.sidebar.write(f"Messages exchanged: {counter}")
            st.sidebar.write("Recent message: ", user_input)

    elif choice == "Conversation History":
        # Display the conversation history
        st.header("Conversation History")
        if session_memory["chat_history"]:
            for message in session_memory["chat_history"]:
                st.text(f"You: {message['user']}")
                st.text(f"Chatbot: {message['chatbot']}")
                st.markdown("---")
        else:
            st.warning("No conversation history found.")

    elif choice == "About":
        # About section
        st.subheader("About the Enhanced Chatbot")
        st.write("""
        This chatbot uses Natural Language Processing (NLP) and Machine Learning (ML) techniques to interact with users, 
        classify their intents, and provide accurate responses.
        
        **Features:**
        - User personalization
        - Feedback mechanism for continuous improvement
        - Real-time session statistics
        - Conversation history tracking
        
        **Technologies Used:**
        - TF-IDF vectorization
        - Logistic Regression
        - Streamlit for the user interface
        
        Explore and enjoy chatting with the bot!
        """)

if __name__ == "__main__":
    main()