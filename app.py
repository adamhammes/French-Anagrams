from flask import Flask, render_template, request, redirect, url_for
from FrenchBingo import bingo

MAX_WORD_LENGTH = 7


app = Flask(__name__, static_url_path='/static/')
words = bingo.read_file('FrenchBingo/words.txt')


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        letters = request.form['letters']
        return redirect(url_for('run', letters=letters))


@app.route("/<letters>", methods=['GET', 'POST'])
def run(letters):
    if request.method == 'GET':
        letters = letters[:MAX_WORD_LENGTH]
        results = bingo.find_words(words, letters, sort_by_length=True)[:15]
        return render_template('results.html', letters=letters, results=results)

    return redirect(url_for('run', letters=request.form['letters']))

if __name__ == '__main__':
    app.run()
