from flask import Flask, render_template, request
from FrenchBingo import bingo

app = Flask(__name__, static_url_path='/static/')
words = bingo.read_file('FrenchBingo/words.txt')


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return app.send_static_file('home.html')
    else:
        letters = request.form['letters']
        results = bingo.find_words(words, letters, sort_by_length=True)[:15]
        return render_template('results.html', letters=letters, results=results)

if __name__ == '__main__':
    app.run()