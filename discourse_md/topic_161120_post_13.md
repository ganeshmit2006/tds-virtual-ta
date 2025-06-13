# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161120/14)

<p>Hi Mishkat,</p>
<p>This error is because you are filtering on <code>class_</code> instead of <code>class</code></p>
<p>So if you send a request on <code>http://127.0.0.1/api?class_=1S</code> you will see response for that <code>1S</code> class only.</p>
<p>kind regards</p>