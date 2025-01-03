from flask import Flask, redirect, abort
import json

app = Flask(__name__)

# Load redirects from JSON
with open("redirects.json") as f:
    redirects = json.load(f)

@app.route("/<id>")
def handle_redirect(id):
    print(id)
    if id in redirects:
        return redirect(redirects[id], code=302)
    else:
        abort(404, description="URL not found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
