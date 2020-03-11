#3.1
year_lists = [1980, 1981, 1982, 1983, 1984, 1985]
print(year_lists)

#3.2
print(year_lists[3])

#3.3
print(max(year_lists))

#3.4
things = ['mozzarella', 'cinderella', 'salmonella']

#3.5
print(things[1].capitalize())

#3.6
print(things[0].upper())

#3.7
things.remove('salmonella')
print(things)

#3.8
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise)

#3.9
s = surprise[-1].lower()
invers_s = s[::-1]
print(invers_s.capitalize())

#3.10
e2f = {
    'dog':'chien',
    'cat':'chat',
    'walrus':'morse'
}
print(e2f)

#3.11
print(e2f['walrus'])

#3.12
f2e = dict()
for e,f in e2f.items():
    f2e[f] = e
print(f2e)

#3.13
print(f2e['chien'])

#3.14
print(e2f.keys())

#3.15
life = {
    'animals':{'cats':'Henri', 'octopi':'Grumpy', 'emus':'Lucy'},
    'plants':'',
    'other':''
    }
print(life)

#3.16
print(life.keys())

#3.17
print(life['animals'].keys())

#3.18
print(life['animals']['cats'])