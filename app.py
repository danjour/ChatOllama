from flask import render_template, session, request
from model import *
from msg import *
from user import *
import os
from datetime import datetime

app.secret_key = os.urandom(24)

@app.route("/chat", methods=['GET', 'POST'])
def index():
    login = session['login']
    name = session['name']
    initials = session['initials']
    session['message_history'] = read_messages_from_file(login)  
    message_history = session.get('message_history', [])
    if request.method == 'POST':
        text_message = request.form.get('text')
        now = datetime.now().strftime("%d/%m %H:%M")
        user_message = {"sender": "user", "text": text_message, "time": now}
        response_message = {"sender": "response", "text": answer_model(text_message), "time": now}  
        message_history.extend([user_message, response_message])
        session['message_history'] = message_history 
        save_messages_to_file([user_message, response_message], login) 
        session.modified = True  
    return render_template('index.html', message_history=message_history,name=name, initials=initials)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)