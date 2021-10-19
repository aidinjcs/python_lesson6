array = [1, 5, 5, 6, 'string', [1, 2], 1.2]

if __name__ == '__main__' :
   array.append('hello')
   print(array)

   array = [1, 4, 6, 'string', [3,3], 4.2]
   array.extend([1, 4, 6, 'string', [3,3], 4.2], )
   print(array)

array = [2, 3, 5, 7]
array.insert(4, 11)
print(array)

array = ['spider', 'kanday', 'bmw']
array.remove('spider')
print(array)


array = [1, 3 , 4, 5]
array.pop(-2)
print(array)

vowels = ['t', 'a', 'n', 'k',]
index = vowels.index('k')
print(index)

array = ['c', 1, 2, 3, 4, 4, 4, 4, 'o', 'u', 'n', 't', 'e', 'r']

print(array.count(4))

array = ['rank' 'bank' 'tank']
array.sort(reverse=True)
print(array.sort)

array = [1, 2, 3, 4, 5]
array.reverse()
print('reversed list:', array)

array = [1, 2, 3, 4]
array = array.copy()
print('copied list:', array)


array = [5, 5, 5, 5, 5, 5]
array.clear()
print('list after clear:', array)
