# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/71)

<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<p>The data file sent to the api will always be in the <strong>requester’s</strong> local machine. When the api server receives the request, the file will be in binary format?</p>
<p>Or</p>
<p>Sometimes the api server receives the file in byte and some times, it will recieve a link like this : <a href="https://exam.sanand.workers.dev/shapes.png" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/shapes.png</a></p>
</blockquote>
</aside>
<p>file format will be exactly same as corresponding GA.</p>
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<pre><code class="lang-auto">"&lt;table&gt;\n&lt;thead&gt;\n&lt;tr&gt;\n&lt;th&gt;Col 1&lt;/th&gt;\n&lt;th&gt;Col 2&lt;/th&gt;\n&lt;/tr&gt;\n&lt;/thead&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 1, Col1&lt;/td&gt;\n&lt;td&gt;Row 1 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 2, Col 1&lt;/td&gt;\n&lt;td&gt;Row 2 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;/tbody&gt;\n&lt;/table&gt;
</code></pre>
</blockquote>
</aside>
<p>This is correct html table format.</p>
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<p>Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block</p>
</blockquote>
</aside>
<p>It will be just answer.</p>
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<p>Some questions have more than one file. For example, the last question of GA5, it has a png file in this link <a href="https://exam.sanand.workers.dev/jigsaw.webp" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/jigsaw.webp</a> and a table.</p>
<p>In this case, how will the curl request be? Is it some thing like this</p>
<pre><code class="lang-auto">curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file= Image file" \
  -F "file= table file/ string" 
</code></pre>
</blockquote>
</aside>
<p>In last question of GA5 there is only one file(image), table is not coming through file, it will be kept same for project2.</p>
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<p>Will the CORS headers asked in the question be the same or can it be different?</p>
</blockquote>
</aside>
<p>I didn’t get this question, could you point to exact question?</p>

![Image](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png)