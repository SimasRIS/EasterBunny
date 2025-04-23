import os
import openai
from flask import Flask, session, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

SYSTEM_PROMPT = ('Tu esi velykų kiškutis, draugiškas asistentas vaikams.'
                 'Tavo užduotis yra vaizdžiai ir žaismingai, bet glaustai atsakinėk į užduotus klausimus'
                 'Visada palaikyk draukišką pokalbį, palaikyk interaktyvumą')


def get_history():
    if "history" not in session:
        session["history"] = [{  # Nurodo musu vartotojo duomenis ir pacio modelio
            "role": "system",  # Paduosim duomenis
            "content": SYSTEM_PROMPT  # Nurodo kas jis toks
        }]
    return session["history"]


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route("/chat", methods=["POST"])  # method post, kad siunciam i serveri duomenis
def chat():
    user_msg = request.json.get('message', "")
    history = get_history()
    history.append({
        "role": "user",  # koks vartotojas is ka parase
        "content": user_msg  # msg content
    })

    completion = openai.chat.completions.create(
        model='gpt-4',
        messages=history
    )

    assist_msg = completion.choices[0].message.content  # Grazina suformuota atsakyma
    history.append({
        "role": "assistant",
        "content": assist_msg
    })

    session["history"] = history
    return jsonify({
        "reply": assist_msg
    })


if __name__ == '__main__':
    app.run()
