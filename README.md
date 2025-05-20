# AI_Chat_Log_Summarizer

## 📄 Project Overview
This Python project summarizes chat logs between a user and an AI. It extracts key insights like total messages, common topics, and frequently used keywords using TF-IDF (Term Frequency-Inverse Document Frequency).

## ✅ Features
- Reads chat logs.
- Separates messages by User and AI.
- Counts messages (User, AI, Total).
- Extracts top 5 keywords using TF-IDF.
- Prints a simple summary of the conversation.
- Supports both single and multiple file summarization.


## 🛠️ Requirements
Python 3.6+
scikit-learn (for TF-IDF keyword extraction)
Install it with:
    pip install scikit-learn


## 🚀 How to Run
1. Place all your chat log `.txt` files inside a folder (e.g. `AI_Chat_Log_Summarizer`).
2. Make sure the chat logs follow the format:
   User: Hello!
   AI: Hi! How can I help?
3. Update the folder path in the script.
4. Run the script using: python your_script_name.py
5. Choose an option:
   - 1 to summarize a single file
   - 2 to summarize all chat logs in the folder


### - Author
Mustafizur Rahman
