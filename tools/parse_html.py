from html.parser import HTMLParser

class TagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack=[]
        self.errors=[]
        self.line=1
        self.positions=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=='div' or tag.lower().startswith('section'):
            self.stack.append((tag, self.getpos()))
        self.positions.append(('start',tag,self.getpos()))
    def handle_endtag(self, tag):
        self.positions.append(('end',tag,self.getpos()))
        if tag.lower()=='div' or tag.lower().startswith('section'):
            if not self.stack:
                self.errors.append(f'Unexpected </{tag}> at {self.getpos()}')
            else:
                open_tag, pos = self.stack.pop()
                # no need to match tag name for divs
    def close(self):
        super().close()
        if self.stack:
            for tag,pos in self.stack:
                self.errors.append(f'Unclosed <{tag}> opened at {pos}')

if __name__=='__main__':
    import sys
    path='index.html'
    txt=open(path,'r',encoding='utf-8').read()
    p=TagParser()
    p.feed(txt)
    p.close()
    print('Errors:')
    for e in p.errors:
        print(e)
    # Print around problematic areas
    lines=txt.splitlines()
    for e in p.errors:
        import re
        m=re.search(r'at \((\d+),(\d+)\)',e)
        if m:
            ln=int(m.group(1))
            start=max(1,ln-5)
            end=min(len(lines),ln+5)
            print('\nContext lines',start,'to',end)
            for i in range(start-1,end):
                print(f'{i+1:4}: {lines[i]}')
