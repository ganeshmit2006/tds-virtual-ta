# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/66)

<p>Hi TAs,</p>
<p>I attended the meet which happened today. But I don’t clearly get one thing.</p>
<p>Most of the questions have a <strong>question text</strong> and a <strong>file: csv,zip,json,etc</strong></p>
<p>My doubt is, will the request to the end point be :</p>
<pre><code class="lang-auto">curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file=https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;template=results;type=batting"
</code></pre>
<blockquote>
<p>my doubt :<br>
Is this the only format or can there be other too ?</p>
</blockquote>