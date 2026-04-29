import re

content = open('index.html').read()
script_match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
if not script_match:
    print("No script block found")
    exit()

script = script_match.group(1)

def find_tags(text):
    i = 0
    while i < len(text):
        if text[i] == '<':
            start = i
            i += 1
            if i < len(text) and text[i] == '/':
                i += 1
                name_start = i
                while i < len(text) and (text[i].isalnum() or text[i] in '._'):
                    i += 1
                name = text[name_start:i]
                while i < len(text) and text[i] != '>':
                    i += 1
                yield ('close', name, start)
            else:
                name_start = i
                while i < len(text) and (text[i].isalnum() or text[i] in '._'):
                    i += 1
                name = text[name_start:i]
                while i < len(text) and text[i] != '>':
                    if text[i] in ['"', "'", '`']:
                        quote = text[i]
                        i += 1
                        while i < len(text) and text[i] != quote:
                            if text[i] == '\\': i += 1
                            i += 1
                    i += 1
                if i < len(text) and text[i-1] == '/':
                    yield ('self', name, start)
                else:
                    yield ('open', name, start)
        i += 1

stack = []
for type, name, pos in find_tags(script):
    if name.lower() in ['input', 'br', 'hr', 'img', 'link', 'meta']: continue
    if type == 'open':
        stack.append((name, pos))
    elif type == 'close':
        if not stack:
            print(f"Extra closing tag </{name}> at pos {pos}")
            continue
        last_name, last_pos = stack.pop()
        if last_name != name:
            print(f"Mismatch: </{name}> vs <{last_name}> (opened at pos {last_pos})")

for name, pos in stack:
    print(f"Unclosed <{name}> at pos {pos}")
