import os
import re
from collections import Counter


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
print(user, ai)

# Counting the message

def count_messages(user, ai):
    return len(user), len(ai), len(user) + len(ai)

user_len, ai_len, total = count_messages(user, ai)
print(f"This is user len: {user_len}\n This is ai len: {ai_len}\n This is total message: {total}")