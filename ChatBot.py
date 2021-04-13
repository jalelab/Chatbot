from Back_Files import chat
from autocorrect import Speller
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    spell = Speller()
    userText = request.args.get('msg')
    response= str(chat.chatbot_response(userText))
    if response in ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"]:
        userText= spell(userText)
        response= str(chat.chatbot_response(userText))
    return response
if __name__ == "__main__":
    app.run()
