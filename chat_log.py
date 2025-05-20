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


# Counting the message
def count_messages(user, ai):
    return len(user), len(ai), len(user) + len(ai)


# This part is for keyword extraction 
def extract_keywords(messages, top_n=5):
    stop_words = set(stopwords.words('english'))
    all_words = ' '.join(messages).lower()
    words = re.findall(r'\b\w+\b', all_words)
    filtered_words = [w for w in words if w not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(top_n)


# Generating Summary 
def generate_summary(user, ai, keywords):
    user_count, ai_count, total = count_messages(user, ai)
    top_topics = ", ".join([word.capitalize() for word, _ in keywords])
    
    summary = []
    summary.append("Summary:")
    summary.append(f"- The conversation had {total} exchanges.")
    summary.append(f"- The user asked mainly about {keywords[0][0].capitalize()} and its uses.")
    summary.append(f"- Most common keywords: {top_topics}.")
    # print("\n".join(summary))
    return "\n".join(summary)


# final call of all these function above 
file_path = r"C:\Users\Mustafizur Rahman\Desktop\AI_Chat_Log_Summarizer\UserAI_Chat.txt"

user, ai = chat_file(r"C:\Users\Mustafizur Rahman\Desktop\AI_Chat_Log_Summarizer\UserAI_Chat.txt")
keywords = extract_keywords(user + ai)
summary_lines = generate_summary(user, ai, keywords)

print(summary_lines)