import re
from db import read_chat,save_chat
   
def save_messages_to_file(message_history, login):
    filename = f"data/message_history_{login}.txt"
    with open(filename, "a", encoding="utf-8") as file:
        for message in message_history:
            file.write(f"{message['time']} - {message['sender']}: {message['text']}\n")
            save_chat(login,filename)

def is_new_message(line):
    return re.match(r"\d{2}/\d{2} \d{2}:\d{2} - ", line) is not None

def read_messages_from_file(login):
    filename = f'{read_chat(login)}'
    messages = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            current_message = None
            for line in file:
                if is_new_message(line):
                    if current_message:
                        messages.append(current_message)
                    parts = line.strip().split(" - ")
                    time, sender_and_text = parts[0], parts[1]
                    sender, text = sender_and_text.split(":")[0], sender_and_text.split(":", 1)[1]
                    current_message = {"time": time, "sender": sender, "text": text.strip()}
                else:
                    current_message["text"] += " " + line.strip()
            if current_message:
                messages.append(current_message)
    except FileNotFoundError:
        print("File not found. Starting a new conversation.")
    return messages
