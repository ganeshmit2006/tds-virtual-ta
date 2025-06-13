# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/165922/3)

<p>For some projects where there are many dependencies, like an ML project or flask app, it’s better you mantain a virtual environment since the dependencies are interconnected with their versions.</p>
<p>Whereas for some simple projects, with less dependencies, global installation is fine.</p>
<blockquote>
<p>For project that is to be deployed, make sure you use the virtual environment, only then you can ensure what worked for you also works on the deployement</p>
</blockquote>
<hr>
<aside class="quote group-ds-students" data-username="24f2006531" data-post="1" data-topic="165922">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png" class="avatar"> 24f2006531:</div>
<blockquote>
<p>Additionally, when managing dependencies, would it be better to install packages individually using pip or list them in a requirements.txt file?</p>
</blockquote>
</aside>
<p>Coming to your second question,</p>
<p>The first time you install a fresh dependency, use direct and latest version. But if you are cloning or thinking of sharing the repo or using someone’s project it’s better to use requirements.txt.</p>
<hr>
<aside class="quote group-ds-students" data-username="24f2006531" data-post="1" data-topic="165922">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png" class="avatar"> 24f2006531:</div>
<blockquote>
<p>My understanding is that if a version is not specified in the requirements.txt file, it installs the latest available version, whereas specifying a version ensures a specific installation</p>
</blockquote>
</aside>
<p>The creation of requirements.txt ensures that the current installation version is listed.</p>
<blockquote>
<p>Never try to list requirements.txt. There is a command to do that, <code>pip3 freeze &gt; requirements.txt </code>. This does the hard work of listing the dependencies for you</p>
</blockquote>

![Image](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/24f2006531/48/111700_2.png)