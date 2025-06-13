# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161083/72)

<p><a class="mention" href="/u/rohitkumar7463">@Rohitkumar7463</a> <a class="mention" href="/u/23f2003845">@23f2003845</a></p>
<p>If you are on Windows Powershell<br>
Then instead of <code>sha256sum</code> you can simply use <code>Get-FileHash</code></p>
<p>Send the output of the <code>npx -y prettier@3.4.2 README.md</code> to a text file eg. <code>output.txt</code> and then use <code>Get-FileHash</code> on powershell with the <code>output.txt</code> and it will use sha256 by default and give you the exact same output.<br>
You might be able to pipe the data directly to <code>Get-FileHash</code> but I have not tried direct piping. The above method works guaranteed.</p>
<p>Kind regards</p>