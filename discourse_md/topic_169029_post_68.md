# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/68)

<p>Fine sir, this is clear. I have a few doubts in the file formats. When free, kindly address these to. I will try to cover most common doubts, so that you wouldn’t need to answer similar doubts again. Sorry if some of the doubts are basic / written incorrectly.</p>
<h2><a name="p-608672-files-1" class="anchor" href="#p-608672-files-1"></a>FILES</h2>
<p>The data file sent to the api will always be in the <strong>requester’s</strong> local machine. When the api server receives the request, the file will be in binary format?</p>
<p>Or</p>
<p>Sometimes the api server receives the file in byte and some times, it will recieve a link like this :  <a href="https://exam.sanand.workers.dev/shapes.png" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/shapes.png</a></p>
<p>This link was take from GA2 Question 2</p>
<h2><a name="p-608672-html-and-table-2" class="anchor" href="#p-608672-html-and-table-2"></a>HTML AND TABLE</h2>
<p>Some questions have <code>html</code> and <code>tables</code>. In this case will these two be in a file encoded in binary, or will it be a string.</p>
<p>Example for string. Consider the table</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Col 1</th>
<th>Col 2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Row 1, Col1</td>
<td>Row 1 Col 2</td>
</tr>
<tr>
<td>Row 2, Col 1</td>
<td>Row 2 Col 2</td>
</tr>
</tbody>
</table>
</div><p>Will this be something like this</p>
<pre><code class="lang-auto">"|Col 1| Col 2|\n|-|-|\n|Row 1, Col1 | Row 1 Col 2|\n|Row 2, Col 1|Row 2 Col 2|"
</code></pre>
<p>or something like</p>
<pre><code class="lang-auto">"&lt;table&gt;\n&lt;thead&gt;\n&lt;tr&gt;\n&lt;th&gt;Col 1&lt;/th&gt;\n&lt;th&gt;Col 2&lt;/th&gt;\n&lt;/tr&gt;\n&lt;/thead&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 1, Col1&lt;/td&gt;\n&lt;td&gt;Row 1 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 2, Col 1&lt;/td&gt;\n&lt;td&gt;Row 2 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;/tbody&gt;\n&lt;/table&gt;
"
</code></pre>
<h2><a name="p-608672-hidden-block-and-answer-2-tasks-3" class="anchor" href="#p-608672-hidden-block-and-answer-2-tasks-3"></a>HIDDEN BLOCK AND ANSWER : 2 TASKS</h2>
<p>In one question, there were two tasks.</p>
<ul>
<li>Find the answer to the question</li>
<li>Enable the <code>disabled</code> text block</li>
</ul>
<p>In this question, what will the answer type be?</p>
<p>Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block</p>
<h2><a name="p-608672-more-than-one-file-4" class="anchor" href="#p-608672-more-than-one-file-4"></a>MORE THAN ONE FILE</h2>
<p>Some questions have more than one file. For example, the last question of GA5, it has a png file in this link <a href="https://exam.sanand.workers.dev/jigsaw.webp" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/jigsaw.webp</a> and a table.</p>
<p>In this case, how will the curl request be? Is it some thing like this</p>
<pre><code class="lang-auto">curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file= Image file" \
  -F "file= table file/ string" 
</code></pre>
<h2><a name="p-608672-cors-headers-5" class="anchor" href="#p-608672-cors-headers-5"></a>CORS HEADERS</h2>
<p>Will the CORS headers asked in the question be the same or can it be different?</p>