# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/166576/100)

<pre data-code-wrap="SQL"><code class="lang-SQL">SELECT DISTINCT post_id 
FROM (
   SELECT timestamp, post_id, UNNEST (comments-&gt;'$[*].stars.useful') AS useful
   FROM social_media
) AS temp
WHERE useful &gt;= 2.0 
   AND timestamp &gt; '2024-12-08T05:30:31.073Z'
</code></pre>