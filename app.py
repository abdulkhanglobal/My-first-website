from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Abdul's Website</h1>
    <p>This is live on the internet.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)