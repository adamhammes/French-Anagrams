import sys

from flask import Flask, render_template, request, redirect, url_for
from FrenchBingo import bingo

MAX_WORD_LENGTH = 9
NUM_WORDS_TO_DISPLAY = 14

app = Flask(__name__, static_url_path='/static/')
words = bingo.read_file('FrenchBingo/words.txt')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        letters = request.form['letters']
        return redirect(url_for('query', letters=letters))


@app.route("/<letters>", methods=['GET', 'POST'])
def query(letters):
    if request.method == 'POST':
        return redirect(url_for('query', letters=request.form['letters']))

    letters = letters[:MAX_WORD_LENGTH].lower()
    results = bingo.find_words(words, letters, sort_by_length=True)[:NUM_WORDS_TO_DISPLAY]
    return render_template('results.html', letters=letters, results=results)


if __name__ == '__main__':
    debug = '--debug' in sys.argv[1:]
    app.run(debug=debug)
