# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/87)

<p>Use the following script to enable answer boxes and check answers buttons:</p>
<pre><code class="lang-auto">inputs = document.querySelectorAll('input')
textboxes = document.querySelectorAll("textarea")
buttons  = document.querySelectorAll("button")
inputs.forEach(input =&gt; input.removeAttribute('disabled'));
buttons.forEach(input =&gt; input.removeAttribute('disabled'));
textboxes.forEach(input =&gt; input.removeAttribute('disabled'));
</code></pre>
<p>This was provided with the Mock ROE2 mail.</p>