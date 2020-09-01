import flask
from scripts.random_translate import random_translate
import json

app = flask.Flask("RandomTranslate")
app.static_folder = 'static'
# Making the cache into a Python Dict
app.jinja_env.cache = {}

@app.route("/")
def home():
    default = {}
    return flask.render_template("index.html", max=0, text_dict=default, visibility="hidden")

@app.route("/translate/", methods=["POST"])
def translate():
    form_data = dict(flask.request.form)
    text_input, cycles = form_data['text-input'], form_data['cycles']
    text_dict = random_translate(text_input, int(cycles))

    return flask.render_template("result.html", max=cycles, text_dict=text_dict, visibility="visible")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
