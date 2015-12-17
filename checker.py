class stack:
    def __init__(self):
        self.items = []
    def isempty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[n]
    def size(self):
        return len(self.items)
    def html_filitre(dosya):
	list = []
        m =open(dosya).read()
        while i < len(m):
            if m[i] == "<":
                first = i
            if m[i] == ">":
                last = i
            liste.append(m[first+1:last])
            i = i+1
         print liste
         return liste
        
    def tag_chacker(liste):
        tags = liste
        s =stack()
        blanced = true
        i = 0
        while i < len(tags) and blanced:
            tag = tags[i]
            if tag[0] ! = '/':
                s.push(tag)
            else:
                if s.isEmpty():
                    blanced = false
                else:
                    top = s.pop()
                    if not (top == tag[1:]):
                        blanced = fals
           i = i+1
       if blanced and s.isEmpty():
           return true
        else:
            return false
	def html_tag_checker(html):
		print tag_checker(html_filtrele(html))             
    
            
        
    
