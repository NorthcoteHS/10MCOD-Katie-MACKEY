'''
Name: Katie Mackey
Desc: Pig latin generator, eg. Pig Latin is = igPay atinLay isay
Note: this code cannot handle punctuation in a sentence. I don't think I can do that.
'''
p = input("Translate: ")
#list version of p
pl = p.split()
#list of vowels
v = ['a','e','i','o','u','A','E','I','O','U']
#translated list
t =[]
#variable for while loop
a = 0
#testing first letter
while a < len(pl):
    #is it a vowel
    if pl[a][0] in v:
        t.append(pl[a] + "ay ")
    else:
        #is the second letter also a vowel
        if pl[a][1] in v:
            t.append(pl[a][1:]+pl[a][0]+"ay ")
        #if it's not then do this
        else:
            t.append(pl[a][2:]+pl[a][:2]+"ay ")
    a+= 1
#glues it all together
final = "".join(t)
print(final)