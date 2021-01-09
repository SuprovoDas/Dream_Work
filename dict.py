

"""z = 'class' not in dict
print(z)
dict['dept']='Computer Science'
print(dict)"""

#clear()
#copy()
#fromkeys()
#item()
#keys()
#pop()
dic={'Name':'Suprovo','Id': 200,'salary':2000}
print(dict)
print('all keys in dict= ',dic.keys())
print('values in dict= ',dic.values())
print('Item in dict= ',dic.items())
for k in dic:
    print(k)
for k in dic:
    print(dic[k])

for k,v in dic.items():
    print('key = {} value= {}'.format(k,v))
#sequence of each letter and store in dictonary
new = {}
st = 'Book'
for x in st:
    new[x]=new.get(x,0)+1
print(new)

#convert a list into dict
city = ["kolkata",'agartala','howrah']
states = ['West Bengal','Tripura']

d = dict(zip(states,city))
print(d)

#convert a string into dictonary
string = "spandan=21,Soumen=65,Ranajit=34"
lst= []
for x in string.split(','):
    y =x.split('=')
    lst.append(y)
print(lst)
de =dict(lst)
d1={}
for k,v in de.items():
    d1[k] = int(v)
print(d1)


s ="salon:23,sriman:12"
liste=[]
for x in s.split(','):
    y=x.split(':')
    liste.append(y)
print(liste)