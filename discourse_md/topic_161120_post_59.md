# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/161120/63)

<p>I’m not sure of the exact reason for the issue, but there are different ways to deploy to Vercel. One approach is using a <code>vercel.json</code> configuration file, and another is adding headers directly in the API code.</p>
<p>You can follow <a href="https://www.frontend-devops.com/blog/python-on-vercel" rel="noopener nofollow ugc">Gui Bibeau’s guide</a> to add CORS headers to your deployment setup. Also check the recording from yesterday’s session for more clarity in that session Carlton deployed application directly from github repository. If you’re still facing issues, you can join today’s session at 9 PM.</p>
<p>For deploying a Flask or FastAPI app to Vercel, refer to <a href="https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k" rel="noopener nofollow ugc">this guide on DEV Community</a>. I’ve tried both methods, and they work well.</p>