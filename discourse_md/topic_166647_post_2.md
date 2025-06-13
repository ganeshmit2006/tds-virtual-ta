# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/166647/2)

<p>Try using the pymupdf4llm Library<br>
pip install pymupdf4llm</p>
<p>import pymupdf4llm<br>
md_text = pymupdf4llm.to_markdown(“input.pdf”)</p>
<p>import pathlib<br>
pathlib.Path(“output.md”).write_bytes(md_text.encode())</p>
<p>import pymupdf4llm<br>
llama_reader = pymupdf4llm.LlamaMarkdownReader()<br>
llama_docs = llama_reader.load_data(“input.pdf”)</p>