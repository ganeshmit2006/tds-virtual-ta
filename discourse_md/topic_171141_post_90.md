# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/171141/94)

<p>That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.</p>
<p>Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.</p>