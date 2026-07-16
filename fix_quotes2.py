with open('src/utils.ts', 'r') as f:
    text = f.read()

text = text.replace("code.push(\\'            \"R0\"\\');", "code.push('          \"R0\"');")

with open('src/utils.ts', 'w') as f:
    f.write(text)
