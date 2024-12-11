# Implementation-of-Chatbot-using-NLP

# **Chatbot Using NLP**

## **Project Overview**
This project is a general-purpose chatbot built using **Natural Language Processing (NLP)** and **Machine Learning** techniques. The chatbot leverages **TF-IDF vectorization** for feature extraction and **Logistic Regression** for intent classification. It is implemented with a modular design and features a user-friendly web interface built using **Streamlit**.

---

## **Features**
1. **User Personalization**: Captures and remembers the user's name for tailored responses.
2. **Keyword Highlighting**: Highlights key phrases in chatbot responses for better visibility.
3. **Feedback Mechanism**: Users can rate responses as helpful or not.
4. **Conversation History**: Logs all interactions for review during the session.
5. **Session Information Sidebar**: Displays session start time, number of messages, and recent user input.
6. **Dynamic Responses**: Handles a variety of predefined intents such as greetings, FAQs, and general queries.

---

## **Technology Stack**
- **Language**: Python 3.x
- **Libraries**: 
  - Streamlit (for web interface)
  - Scikit-learn (for ML modeling)
  - NLTK (for text preprocessing)
- **Model**: Logistic Regression for intent classification
- **Data**: JSON file containing intents, patterns, and responses

---

## **Setup Instructions**
Follow these steps to set up and run the chatbot locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Srinivas-Vid/Implementation-of-Chatbot-using-NLP.git
   cd YourChatbotProject
   ```

2. **Install Dependencies**
   Make sure you have Python installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**
   Start the Streamlit server to launch the chatbot interface:
   ```bash
   streamlit run my_app.py
   ```

4. **Interact with the Chatbot**
   Open the provided local URL in your browser (usually `http://localhost:8502/`) to start chatting with the bot.

---

## **Project Structure**
| File/Folder      | Description                                       |
|------------------|---------------------------------------------------|
| `my_app.py`         | Main Python file containing the chatbot logic.    |
| `intents.json`   | JSON file containing intents, patterns, and responses. |
| `README.md`      | Project documentation.                           |
| `requirements.txt` | List of dependencies to install.                |

---

## **Snapshots**
### **Chat Interface**
![Chat Interface](https://github.com/Srinivas-Vid/Implementation-of-Chatbot-using-NLP/blob/main/User%20Interface.png)  
*Snapshot showing user input and chatbot response.*

### **Feedback Mechanism**
![Feedback](https://github.com/Srinivas-Vid/Implementation-of-Chatbot-using-NLP/blob/main/Feedback%20Mechanism.png)  
*Snapshot demonstrating the feedback feature.*

### **About**
![About](https://github.com/Srinivas-Vid/Implementation-of-Chatbot-using-NLP/blob/main/About.png)  
*Snapshot of the about feature.*

---

## **Future Enhancements**
1. Add multi-turn conversation handling for better context retention.
2. Integrate APIs for dynamic responses (e.g., weather, news).
3. Expand the intent dataset to handle more complex queries.
4. Add multilingual support for diverse user interaction.

---

## **License**
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the license terms.

---

## **Author**
Developed by **[SRINIVAS ERRAMALLA]**.  
For any queries or suggestions, feel free to reach out at [srinivaserramalla5@gmail.com].
