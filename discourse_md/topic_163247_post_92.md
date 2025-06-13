# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/163247/104)

<aside class="quote group-ds-students" data-username="23f2003853" data-post="32" data-topic="163247">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003853/48/67184_2.png" class="avatar"> 23f2003853:</div>
<blockquote>
<p>rm me where I did mistake</p>
</blockquote>
</aside>
<p>Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results.  Any help would be appreciated.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711.png" data-download-href="/uploads/short-url/fIxys39CFlIQfmTQYkqP3Vp3Eo9.png?dl=1" title="Screenshot 2025-02-05 at 6.19.41 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_690x158.png" alt="Screenshot 2025-02-05 at 6.19.41 PM" data-base62-sha1="fIxys39CFlIQfmTQYkqP3Vp3Eo9" width="690" height="158" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_690x158.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_1035x237.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711.png 2x" data-dominant-color="26282C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-05 at 6.19.41 PM</span><span class="informations">1304×299 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}
</code></pre>

![Here's a description for the alt text:

Screenshot of a dark-themed form indicating an error in an API endpoint configuration. The form asks, "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute". Below, a red-bordered text field contains "http://127.0.0.1:8001/execute" followed by a red icon indicating an error. The error message reads "TypeError: Load failed". The form also says: "Make sure you enable CORS to allow GET requests from any origin" and "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition." A blue "Check" button is at the bottom left.](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_690x158.png)

![Image](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003853/48/67184_2.png)