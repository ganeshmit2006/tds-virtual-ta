# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161120/45)

<pre><code class="lang-auto">{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api",
      "dest": "app.py"
    }
  ],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Credentials", "value": "true" },
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET,OPTIONS,PATCH,DELETE,POST,PUT"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
        }
      ]
    }
  ]
}
</code></pre>
<p><a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a><br>
i have added the header key in order to use the cors as said in the vercel doc but still i am getting that error.<br>
what to do?<br>
i have added the cors in the app.py file as well</p>
<pre><code class="lang-auto">from flask import Flask, request, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load the data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [student["marks"] for student in data if student["name"] in names]
    return jsonify({"marks": marks})


if __name__ == "__main__":
    app.run()

</code></pre>
<p><a href="https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api" class="onebox" target="_blank" rel="noopener nofollow ugc">https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api</a></p>