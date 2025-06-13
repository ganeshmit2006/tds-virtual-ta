# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/165959/25)

<p>Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following<br>
" name: Daily Commit</p>
<p>on:<br>
schedule:<br>
- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC<br>
workflow_dispatch:  # This allows manual trigger</p>
<p>jobs:<br>
commit:<br>
runs-on: ubuntu-latest</p>
<pre><code>steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" &gt; daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"
</code></pre>
<p><a class="mention" href="/u/jivraj">@Jivraj</a> can help me to fix the issue</p>