# usersList = ['a', 'b', 'c']
# usersDictionary = {'zmones' : [1,2,3,{'list':['bab']}], 'pirmas' : 'b', 'bet kas': 'c'}
# usersTuple = ('a', 'b', 'c')
# usersSet = {'a', 'b', 'c'}
# print(usersList[0])
# print(usersList[1])
# print(usersDictionary['pirmas'])
# usersDictionary[4] = 'four'
# usersDictionary['pirmas']

dic = {1: "one", 2: 'two', 3: 'three'}
print(len(dic))
dic[4] = 'four'
print(dic[2])
print(dic.get(10))
print(dic.get(10, 'unknown'))
print(dic.get(3, 'unknown'))
print(dic.pop(2))
print(dic)
new = {0: "zero"}
dic.update(new)
print(dic)
dic.clear()
print(dic)


#help(dict)