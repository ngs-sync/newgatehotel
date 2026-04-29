import re

def check_tags(filepath):
    content = open(filepath).read()
    script_match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
    if not script_match:
        return "No babel script found"

    script = script_match.group(1)

    # Simple tag parser
    tags = re.findall(r'<(/?[a-zA-Z0-9.]+)([^>]*?)(/?)>', script)
    stack = []
    void_elements = {'input', 'br', 'hr', 'img', 'link', 'meta'}

    for name, attrs, self_closing in tags:
        if name.startswith('/'):
            name = name[1:]
            if not stack:
                print(f"Extra closing tag </{name}>")
                continue
            last = stack.pop()
            if last != name:
                print(f"Mismatch: </{name}> closed but <{last}> was expected")
        elif self_closing == '/' or name.lower() in void_elements:
            # Self-closing or void element
            continue
        else:
            stack.append(name)

    for remaining in stack:
        print(f"Unclosed tag: <{remaining}>")

check_tags('index.html')
