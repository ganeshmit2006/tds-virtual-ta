# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/96)

<p>I faced the same issue. Initially, I used <code>geopy.geocoders</code> to solve the question, and it provided the correct answer during the assignment submission. However, the same approach is now giving an incorrect result.</p>
<p>Instead of using <code>geopy</code>, try using this URL directly: <a href="https://nominatim.openstreetmap.org/search" rel="noopener nofollow ugc">https://nominatim.openstreetmap.org/search</a> .<br>
This worked for me.</p>