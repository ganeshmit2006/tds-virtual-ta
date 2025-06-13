# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/164277/76)

<pre data-code-wrap="result"><code class="lang-result">    expected = sum(1 for date in dates if parse(date).weekday() == 2)
    if result.strip() != str(expected):
        return mismatch("/data/dates-wednesdays.txt", expected, result)
    return True```


</code></pre>
<p><img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> /data/dates-wednesdays.txt<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
129<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“129”</p>
<p>If it is expecting str then why throw error sir  ? <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a><br>
or just tell me how to pass count as an int here</p>
<pre><code class="lang-auto">with open(output_file, "w") as f:
        f.write(str(count)) 
</code></pre>