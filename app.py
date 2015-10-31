from flask import Flask, render_template, request, redirect, url_for
from FrenchBingo import bingo 

app = Flask(__name__, static_url_path='/static')
words = bingo.read_file('FrenchBingo/FrenchWordList.txt', encoding='ISO-8859-1')

@app.route("/", methods=['GET'])
def hello():
        letters = request.args.get('letters')
        if not letters: 
                return app.send_static_file('home.html')
        return redirect(url_for('run', letters=letters))

@app.route("/<letters>")
def run(letters):
        results = bingo.find_words(words, letters, sort_by_length=True)[:15]
        return render_template('results.html', letters=letters, results=results)

if __name__ == "__main__":
	app.run(debug=True)
