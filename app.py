from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "nuggetramenbean"
debug = DebugToolbarExtension(app)

@app.route("/")
def ask_story():
    """Ask user which story they would like """

    return render_template("select-story.html", stories = stories.values())

@app.route("/form")
def ask_questions():
    """Generate and show form to ask for adlibs """

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("form.html", story_id = story_id, title = story.title, prompts = prompts)

@app.route("/story")
def fill_story():
    """Show the user created madlibs story """

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title = story.title, text = text)