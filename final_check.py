import re

def check_balance(text):
    script_match = re.search(r'<script type="text/babel">(.*?)</script>', text, re.DOTALL)
    if not script_match:
        print("No script block")
        return
    script = script_match.group(1)

    # Remove strings and comments
    script = re.sub(r'"[^"]*"', '""', script)
    script = re.sub(r"'[^']*'", "''", script)
    script = re.sub(r'//.*', '', script)
    script = re.sub(r'/\*.*?\*/', '', script, flags=re.DOTALL)

    tags = re.finditer(r'<(/?[a-zA-Z0-9\.]+)([^>]*?)(/?)>', script)
    stack = []
    for match in tags:
        name = match.group(1)
        self_close = match.group(3) == '/'
        if self_close or name.lower() in ['input', 'br', 'hr', 'img', 'link', 'meta']:
            continue
        if name.startswith('/'):
            tag_name = name[1:]
            if not stack:
                print(f"Extra </{tag_name}> at pos {match.start()}")
                continue
            last_tag, _ = stack.pop()
            if last_tag != tag_name:
                print(f"Mismatch: </{tag_name}> at pos {match.start()} vs <{last_tag}>")
        else:
            stack.append((name, match.start()))
    for name, pos in stack:
        print(f"Unclosed <{name}> at pos {pos}")

with open('index.html') as f:
    check_balance(f.read())
