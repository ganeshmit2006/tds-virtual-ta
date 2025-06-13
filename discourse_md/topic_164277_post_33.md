# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/164277/36)

<p>evaluate.py<br>
TDS course repo</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...</a></h3>


  <p><span class="label1">Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>line 20</p>
<pre><code class="lang-auto">from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
</code></pre>
<p>but we get datagen.py only in a1 task<br>
line 69</p>
<pre><code class="lang-auto">async def a1(email: str, **kwargs):
    await run(
        f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
    )
    return email in await read("/data/format.md")
</code></pre>
<p>The issue is <strong>importing <code>datagen</code> before ensuring it exists</strong></p>
<p>just checking</p>
<p><a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a></p>

![Image](https://github.githubassets.com/favicons/favicon.svg)