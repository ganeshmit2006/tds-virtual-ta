# No Title

[Original Post](https://discourse.onlinedegree.iitm.ac.in/t/169029/69)

<p>Hi,<br>
In GA 2, q5, this is the code i got in the question.</p>
<pre><code class="lang-auto">import numpy as np
from PIL import Image
from google.colab import files
import colorsys

# There is a mistake in the line below. Fix it
image = Image.open(list(files.upload().keys)[0])

rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness &gt; 0.554)
print(f'Number of pixels with lightness &gt; 0.554: {light_pixels}')
</code></pre>
<p>Is this the code for others as well?<br>
Thanks</p>