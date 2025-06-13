# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/171141/71)

<p>We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.</p>
<p>Line number 81 of your app.py</p>
<p><code>subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)</code></p>
<p>which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.</p>