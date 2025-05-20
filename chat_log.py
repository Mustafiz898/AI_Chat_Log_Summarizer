


# Reading chat file which contains User and AI conversation

def chat_file(path):
    user = []
    ai = []
    with open(path, 'r') as f:
        print(f.read())
        for line in f:
            line = line.strip()
            if line.startswith('User:'):
                user.append(line[5:].strip())
            elif line.startswith('AI:'):
                ai.append(line[3:].strip())
    return user, ai

chat_file(r"C:\Users\Mustafizur Rahman\Desktop\AI_Chat_Log_Summarizer\UserAI_Chat.txt")