from flask import Flask, current_app
from flask import render_template, request
from markov_gen.markov_gen import word_markovIt, ngram_markovIt

app = Flask(__name__)


def read_file(corpus):
    file_path = "markov_gen/corpus/" + corpus + ".txt"
    with current_app.open_resource(file_path, mode="r") as f:
        txt = f.read().replace('\n', '')
    txt_list = txt.split()
    return txt_list, txt


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/markov', methods=['POST', 'GET'])
def markov():
    sizes = {"small": 250, "medium": 1000, "large": 5000}
    n_gram_order = 10
    if request.method == 'POST':
        if 'corpus' in request.form:
            corpus = request.form['corpus']
        size = request.form['size']
        chain_type = request.form['type']
        text = request.form['text']
        if len(text) == 0:
            txt_list, txt = read_file(corpus)
        else:
            txt_list, txt = text.split(), text
        generated_txt = word_markovIt(txt_list, sizes[size]) if chain_type == "word" else ngram_markovIt(
            txt, n_gram_order, sizes[size])
        #  print(generated_txt)
        return render_template("markov.html", data=generated_txt)


if __name__ == '__main__':
    app.run(debug=True)
