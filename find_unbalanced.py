import re

def check_balance(content):
    # This is a very simplified JSX parser
    # It will ignore comments and strings to some extent

    # Remove comments
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    stack = []
    # Find tags: <Tag ... > or </Tag>
    # Note: this will miss self-closing tags if not handled
    tags = re.finditer(r'<(/?[a-zA-Z0-9\.]+)([^>]*?)(/?)>', content)

    for match in tags:
        tag_name = match.group(1)
        is_closing = tag_name.startswith('/')
        is_self_closing = match.group(3) == '/'

        if is_self_closing:
            continue

        if is_closing:
            actual_name = tag_name[1:]
            if not stack:
                print(f"Unexpected closing tag </{actual_name}> at position {match.start()}")
                continue
            last_tag, last_pos = stack.pop()
            if last_tag != actual_name:
                print(f"Mismatched closing tag </{actual_name}>, expected </{last_tag}> (opened at position {last_pos})")
                # Try to recover by pushing last_tag back if it's a common error
                # but for now just print
        else:
            # Ignore some common HTML void elements if they are not self-closed in JSX (though they should be)
            if tag_name.lower() in ['img', 'br', 'hr', 'input', 'link', 'meta']:
                continue
            stack.append((tag_name, match.start()))

    for tag, pos in stack:
        print(f"Unclosed tag <{tag}> opened at position {pos}")

with open('index.html', 'r') as f:
    content = f.read()
    # Find the script block
    match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
    if match:
        check_balance(match.group(1))
