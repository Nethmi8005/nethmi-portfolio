import re
lines=open('index.html','r',encoding='utf-8').read().splitlines()
opens=[]
closes=[]
for i,l in enumerate(lines, start=1):
    for m in re.finditer(r'<div\b', l):
        opens.append((i, l.strip()))
    for m in re.finditer(r'</div>', l):
        closes.append((i, l.strip()))
print('Total opens', len(opens), 'Total closes', len(closes))
print('\nLast 20 opens:')
for o in opens[-20:]: print(o)
print('\nLast 20 closes:')
for c in closes[-20:]: print(c)
# Find first mismatch by simulating stack
stack=[]
for i,l in enumerate(lines, start=1):
    opens_here = len(re.findall(r'<div\b', l))
    closes_here = len(re.findall(r'</div>', l))
    for _ in range(opens_here): stack.append(i)
    for _ in range(closes_here):
        if stack:
            stack.pop()
        else:
            print('Extra close at', i)
print('Remaining unclosed count:', len(stack))
if stack:
    print('Unclosed opened at lines (first 10):', stack[:10])
