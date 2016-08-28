#-*- coding: utf-8 -*-
import random
class stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):        return len(self.items)
    def randomEleman(self):
        sayi = random.randint(0,self.size())
        return self.items[sayi-1]
  
s = stack()
sifatlar = ["Titrek","asil","kurak","olgun","otomotik","yavas","hizli","kofik","cam","soluk","vezinli","zoraki",
"celalli","cizbiz","çabuk","çevik","çökelekli","dantelli","durgun","dumansız","eskimsi","şairimsi",
"evhamlı","forslu","gagalı","gıcırtısız","görgülü","gür","gürültülü","hafif","halkalı","sivri",
"harbi","has","hassas","hoşsohbet","ışıklı","ılıman","istikrarlı","jarse","kavuklu","serinkanlı",
"karıştırıcı","kâküllü","kaygılı","küpeli","senfonik","bozuk","ilkel","antik","gri","radikal",
"mavi","laklak","lüle","manyetik","manidar","monşer","monoton","yakışıklı","güzel","morumsu","muazzam","protez","loş",
"mütevazi","nahoş","natürel","otoriter","ortopedik","pamuklu"," promosyonlu","püsküllü","kocamanca"]
isimler = ["keci","kunduz","hayat","efsane","ova","panda","simsek","ocak","çerçeve","göz",
"gün","çiçek","dağ","tabak","baca","soba","şeker","papağan","adım","yol","sarımsak","susam","minder","elmas",
"otobüs","krater","tuzluk","deniz","dere","duman","toprak","yagmur","yürek","rüya","ses","sokak","soğan",
"kitap","hal","gönül","bilgi","hikaye","sanayi","çamur","at","araba","mecnun","duman","makina","maki",
"otoban","kirpi","parmak","gezegen","duvar","manzara","halı","baca","mızka","yetenek","fiş","saksı","çam",
"çiçek","toka","şeftali","lahana","fırtına","kumaş","kelime","şiir","hikaye","yıldız", "çöl"]

for i in sifatlar:
    s.push(i)
 
k =stack()

for j in isimler:
    k.push(j)
print s.randomEleman()+"_"+k.randomEleman()



