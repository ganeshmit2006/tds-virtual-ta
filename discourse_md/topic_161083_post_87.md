# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161083/96)

<p>Hi Arnav,</p>
<p>I tried your script on your dataset.<br>
Problem might be you are not executing <code>grep . * | LC_ALL=C sort | sha256sum</code> in correct directory, you would need to execute it from <code>all_files</code> directory also there should not be any extra file other than that gets generated.</p>