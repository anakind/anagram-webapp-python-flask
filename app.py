from flask import Flask, render_template, json, request
from anagram import Anagram

app = Flask(__name__)

anagram = Anagram()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_anagram')
def check_anagram():
    firstWord = request.args.get("firstWord", "")
    secondWord = request.args.get("secondWord", "")

    if Anagram.checkIfAnagram(firstWord, secondWord):
        return json.dumps({"result": True,
                           "message": "Yes! They are anagrams"})
    else:
        return json.dumps({"result": False,
                           "message": "No! They are NOT anagrams"})


@app.route('/refresh_topten')
def refresh():
    firstWord = request.args.get("firstWord", "")
    secondWord = request.args.get("secondWord", "")

    if len(firstWord) != 0 and len(secondWord) != 0:
        anagram.insertRequest(firstWord, secondWord)
    return json.dumps({"result": anagram.getTopTenRequests()})


if __name__ == "__main__":
    app.run()
