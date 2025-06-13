# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/164277/67)

<p>Getting the following error :</p>
<pre><code class="lang-auto">127.0.0.1 - - [07/Feb/2025 01:44:54] "GET /run?task=generate%20data%20for%20ujanaishik109@gmail.com HTTP/1.1" 200 -
  File "/tmp/datagenyhqKlO.py", line 1
    404: Not Found
    ^^^
SyntaxError: illegal target for annotation

</code></pre>
<p>when executing the following code :</p>
<h2><a name="p-591326-mainpy-1" class="anchor" href="#p-591326-mainpy-1"></a>Main.py</h2>
<pre><code class="lang-auto">@routes.route("/run", methods=["GET", "POST"])
def run():
    task = request.args.get("task")
    try:
        res = get_func_name(task)
        func_name = res["func_name"]
        args = res.get("arguments", [])
        print("ARGUMENTS : ", args)
        if args:
            generated_func = globals()[func_name](*args)
            print("GENERATED FUNC :",generated_func)
            res = f"{func_name} executed successfully"
        else:
            generated_func = globals()[func_name]()
            print(generated_func)
            res = f"{func_name} executed successfully"
    except Exception as e:
        res = None
        print("error : ", e)
    return jsonify(res)

</code></pre>
<h2><a name="p-591326-taskspy-2" class="anchor" href="#p-591326-taskspy-2"></a>Tasks.py</h2>
<pre><code class="lang-auto">def generate_data_files(user_email: str):
    subprocess.Popen(
        [
            "uv",
            "run",
            "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py",
            f"{user_email}",
            "--root",
            "../data",
        ]
    )
    print("data generated successfully")
</code></pre>
<p>Please Guide <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a></p>