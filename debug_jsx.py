import re

content = open('index.html').read()
script = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL).group(1)

tags = re.finditer(r'<(/?[a-zA-Z0-9\.]+)([^>]*?)(/?)>', script)
for m in tags:
    print(f"Tag: {m.group(0)}, Name: {m.group(1)}, Self: '{m.group(3)}'")
