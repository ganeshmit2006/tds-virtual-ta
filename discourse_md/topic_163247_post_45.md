# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/163247/48)

<p>Hello Sir,</p>
<p>I am unable to recieve a proper output for q1 of ga3.<br>
This is my test message. Its been given in two lines.</p>
<p><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/60deb1fe7cda3d6876df481d07803e66d1974e45.png" alt="image" data-base62-sha1="dOWXuMn1NzBuHNYXw6RnYs0LbPT" width="332" height="84"></p>
<p>The below is my code for the question.</p>
<pre><code class="lang-auto">import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])
</code></pre>
<p>I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative</p>
<p><code>user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"</code></p>
<p>The error message i keep receiving is as below.</p>
<p><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/740853eca092fd94814c5c4cb8cc4ddb5f10eba3.png" alt="image" data-base62-sha1="gytebKLwoJRYvxAXz46owLm92Th" width="690" height="52" data-dominant-color="312C30"></p>
<p>Kindly advice on how to proceed.</p>
<p>Thanks and Regards<br>
Shalini</p>

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/740853eca092fd94814c5c4cb8cc4ddb5f10eba3.png)

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/60deb1fe7cda3d6876df481d07803e66d1974e45.png)