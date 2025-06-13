# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/166576/47)

<p><a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a></p>
<p>Your query construction is unnecessarily complicated and therefore will be difficult to debug.</p>
<p>Query construction is best done by thinking what you want at the end.<br>
In this case its an ordered <code>post_id</code></p>
<p>So thats where you begin:</p>
<pre data-code-wrap="SQL"><code class="lang-SQL">SELECT post_id
FROM (
...
)
ORDER BY post_id
</code></pre>
<p>Doing this, produces the actual result without giving the logic yet.</p>
<p>Then at each stage you add the next stage of complexity.<br>
You will still need the <code>post_id</code> for the <em>outermost layer</em> so you have to continue extracting it from the <em>inner layers</em> of the nested query.</p>
<pre data-code-wrap="SQL"><code class="lang-SQL">...
...
FROM (
   SELECT post_id, ( ... ) as max_stars
   FROM social_media
   WHERE time_stamp &gt;= (whatever the parameter you have been given)
      AND max_stars &gt;= (whatever the parameter for min stars you have been given)
)
...
...
</code></pre>
<p>Then the final layer of the nest</p>
<pre data-code-wrap="SQL"><code class="lang-SQL">...
...
(

) as max_stars
...
...
</code></pre>
<p>You are not expecting me to solve the whole question right? (Hint: the inner most extraction involves JSON or “structure” extraction, which is a powerful capability)</p>
<p>But I hope you understand the logic of SQL which is a very elegant set theory language which is why it has lasted for over 4 decades.</p>
<p>Think clearly at each stage what do you need. Start with the answer and work backwards, extracting at each stage the logical items you require for the outer layer to be functional.</p>
<p>Kind regards</p>