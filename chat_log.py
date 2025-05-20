import os
import re
from collections import Counter
import nltk

# Ensuring stopwords are available
nltk.download('stopwords')
from nltk.corpus import stopwords


# Reading chat file which contains User and AI conversation

def chat_file(path):
    user = []
    ai = []
    with open(path, 'r') as f:
        # print(f.read())
        for line in f:
            line = line.strip()
            if line.startswith('User:'):
                user.append(line[5:].strip())
            elif line.startswith('AI:'):
                ai.append(line[3:].strip())
    return user, ai

user, ai = chat_file(r"C:\Users\Mustafizur Rahman\Desktop\AI_Chat_Log_Summarizer\UserAI_Chat.txt")
# print(user, ai)

# Counting the message

def count_messages(user, ai):
    return len(user), len(ai), len(user) + len(ai)

user_len, ai_len, total = count_messages(user, ai)
# print(f"This is user len: {user_len}\n This is ai len: {ai_len}\n This is total message: {total}")

# This part is for keyword extraction 

def extract_keywords(messages, top_n=5):
    stop_words = set(stopwords.words('english'))
    all_words = ' '.join(messages).lower()
    words = re.findall(r'\b\w+\b', all_words)
    filtered_words = [w for w in words if w not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(top_n)


keyword = extract_keywords(user + ai)
print(keyword)