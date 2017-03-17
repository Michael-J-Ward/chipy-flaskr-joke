from flask import Flask
import  random
app = Flask(__name__)

jokes = ["What did the big Buffalo said to small Buffalo - Byson",
    "Whaty don't some couples go to the gym? Because some relationships don't work out.",
    "Did you hear about the guy whose whole left side was cut off? He's all right now."
]


@app.route("/")
def hello():

    randomNumber = random.randint(0,2)
    return jokes[randomNumber]

@app.route("/<query>")
def search_jokes(query):
    for joke in jokes:
        if query in joke:
            return joke
    return hello()

            # return "Jokes not here! We aren't joking"



if __name__ == "__main__":
    app.run()
