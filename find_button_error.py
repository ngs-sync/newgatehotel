content = open('index.html').read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if '<button' in line and '</button>' not in line:
        # Check if it closes on a later line
        found_close = False
        for j in range(i, min(i + 10, len(lines))):
            if '</button>' in lines[j]:
                found_close = True
                break
        if not found_close:
            print(f"Potential unclosed button at line {i+1}: {line.strip()}")
