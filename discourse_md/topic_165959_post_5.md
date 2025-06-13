# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/165959/6)

<p><a class="mention" href="/u/22f3001315">@22f3001315</a> <a class="mention" href="/u/21f3002277">@21f3002277</a> <a class="mention" href="/u/24ds2000024">@24ds2000024</a> – please try again after reloading the page. The new error message will be clearer, like this:</p>
<pre><code class="lang-plaintext">Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4
</code></pre>
<p>FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.</p>