# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161120/46)

<p><a class="mention" href="/u/23f2003751">@23f2003751</a><br>
While I understand why you might choose to use <code>flask</code> due to your familiarity with it,<br>
the <code>http.server</code> library is just very simple to use.</p>
<p>The <strong>only extra line of code</strong> you would need inside your <code>get</code> request if you used the <code>http.server</code> library would be:</p>
<p><code>self.send_header("Access-Control-Allow-Origin", "*")</code></p>
<p>Try to rewrite your code using <code>http.server</code>  library so that your debugging for simple tasks like this is easy.</p>
<p>The boilerplate code for a <code>get</code> request using the <code>http.server</code> library was already given in Q6. So you have to do very minimal modifications to it and it works like a charm.</p>
<p>Kind regards</p>