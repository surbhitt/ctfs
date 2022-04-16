# this is the template for a program with a dictionary sorted with the keys

l = { 0 :'d' ,
29: 'a',
4 :'r',
2 :'5',
23: 'r',
3 :'c',
17: '4',
1 :'3',
7 :'b',
10: '_',
5 :'4',
9 :'3',
11: 't',
15: 'c',
8 :'l',
12: 'H',
20: 'c',
14: '_' ,
6: 'm' ,
24: '5',
18: 'r',
13: '3',
19: '4',
21: 'T',
16: 'H',
27: '6',
30: 'f',
25: '_',
22: '3',
28: 'd',
26: 'f',
31: '4' }

sl = [value for key, value in sorted(l.items())] # Note the () after items!
print("".join(sl))


''' for sorting dictionary with values use
	sorted(d.items(), key = lambda x : x[1])
'''
