import re
import os
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer


# Reading chat file which contains User and AI conversation
def chat_file(path):
    user = []
    ai = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('User:'):
                user.append(line[5:].strip())
            elif line.startswith('AI:'):
                ai.append(line[3:].strip())
    return user, ai


# Counting the message
def count_messages(user, ai):
    return len(user), len(ai), len(user) + len(ai)


# This part is for keyword extraction 
##### This is TF-IDF approach 
def extract_keywords(messages, top_n=5):
    joined_text = ' '.join(messages)
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([joined_text])

    scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return sorted_scores[:top_n]



# Generating Summary 
def generate_summary(user, ai, keywords):
    user_count, ai_count, total = count_messages(user, ai)
    top_topics = ", ".join([word.capitalize() for word, _ in keywords])
    
    summary = []
    summary.append(f"- The conversation had {total} exchanges.")
    summary.append(f"- The user asked mainly about {keywords[0][0].capitalize()} and its uses.")
    summary.append(f"- Most common keywords: {top_topics}.")
    return "\n".join(summary)


# Summary for a single file 
def summarize_single_file(folder_path, filename):
    file_path = os.path.join(folder_path, filename)
    user, ai = chat_file(file_path)
    keywords = extract_keywords(user + ai)
    summary = generate_summary(user, ai, keywords)

    print(f"\nSummary for {filename}:\n")
    print(summary)


# Summarization of All Files in the Folder
def summarize_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            summarize_single_file(folder_path, filename)


# User Choice Logic

if __name__ == "__main__":
    folder_path = r"C:\Users\Mustafizur Rahman\Desktop\AI_Chat_Log_Summarizer"

    choose = input("Enter 1 for single file\nEnter 2 for all files in folder: ").strip()

    if choose == '1':
        fileName = input("Enter file name (with .txt): ").strip()
        if fileName in os.listdir(folder_path):
            summarize_single_file(folder_path, fileName)
        else:
            print("File not found!")
    elif choose == '2':
        summarize_folder(folder_path)
    else:
        print("Invalid choice.")