# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161120/94)

<p>hi <a class="mention" href="/u/23f2003853">@23f2003853</a></p>
<p>I think you are running your application server inside a virtual machine because of which it doesn’t have visibility to outside world(request coming from other domains). So you would need to identify  ipaddress of your virtual machine and would need to use that in place of <code>127.0.0.1</code>. Take help from GPT to identify ipaddress of virtual machine.</p>