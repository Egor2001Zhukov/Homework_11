from flask import Flask, render_template
from utils import *


data = load_candidates_from_json("https://www.jsonkeeper.com/b/8Q2K")

app = Flask(__name__)


@app.route("/")
def page_home():
    return render_template('list.html', candidates=data)


@app.route("/candidate/<int:x>")
def page_condidate(x):
    return render_template('card.html', candidate=get_candidate(data, x))


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    return render_template('search.html', candidates=searching_name(data, candidate_name))


@app.route("/skills/<skill_name>")
def page_skills(skill_name):
    return render_template('skills.html', candidates=get_candidates_by_skill(data, skill_name), skill_name=skill_name)


app.run(debug=True)
