import re
#\w --> select  a-z A-Z 0-9 _
# \W --> harchi ke kochike entekhab nakonad
# \d --> number 0-9
# \D --> harchizi be joz adada 0-9
#\s--> space
# \S --> harchizi be joz space
# . dot --> hame chiz
# [abcd] --> feqat in ha select kon
# [a-n] --> az a ta n harche bood select kon  mesal digar [0-4]
#[a-zA-Z0-9] --> hooroof bozorg , koochak , adad
# [^0-9] hat  --> agar dakhel braket va aval on bashad not harch dakhel braket bood select mikonad
# \ beraye select character haye daraye mani dar regular expression  mesl  (* + \ [?
# ^ hat dar in halat be mani avval line hast ^a khat haye ke ba a shoro mishevad
# $ dollar  akar khat chek mikonad agar match bood select mikone
# * star  be manaye 0 ya bishtar
# + plus be manaye 1 ya bishtar
# @? qustion mark  be manaye bashad ya nebashad  manzoor be tedae 0 ya 1
# {3} deqiqan be tadad 3 ta  oon chiz
# {3 ,9} bin 3 ta 9 tekrar on chiz
# {3, } az 3 ta bishtar tekrat oon chiz
# pip ya |  be nabay ya
# () group


# mesal
text = """524581214  ham do reqam ham addad basjhe 
050468
11111111111111111111111111
222222
1fhfhfh1
165.192.14.84
82.145.129.50
100.100.100.100
900.500.400.555
109.68.89.158
38.161.3.24
56.71.194.31
 #\@%^&*+---- ?
56[]
56{}
purdy.katheryn@hand.com zola13@wisozk.org
raina.willms@stracke.info
annabelle82@gmail.com
mlarkin@leffler.biz
marlen.carter@collier.biz
janet.mcclure@hotmail.com
windler.alverta@gmail.com
milan.mckenzie@beatty.com
aurore00@hotmail.com
82.178.127.166
50.220.234.79
217.90.24.64
241.158.254.14
taha nemati  13456546464
09172256452
+9823135456165
babak
9
44
558
jahn_      
(42424)-+=
havij
qolitttttttttttttttttttteeeeeeeeeeee
/n @#$%&^**((mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
"""
pattern = re.compile(r"(\w[a-z]{1}[a-zA-Z0-9_.]*)@(\w*)\.(\w{3,})")
result = pattern.search(text) # joostejoo va yaftan avali
print(result)
print(result.group())
result_find = pattern.findall((text)) # sakht list az temam match ha ke payda mikonad
print(result_find)
print(result.group(0)) # group() ya group(0) da har 2 halat kamelesh miare
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
for item in result_find:
    print(item[2])



# re.compile(pattern) , pattern.search ya pattern.findall() ,
# sub  pattern.sub('TAHA',TEXT)
result3 = pattern.sub('taha@gmail.com',text ,4)
#pattern.sub(replcement,text,count = tedad ke mikhahid jaygozin shevad)

print(result3)