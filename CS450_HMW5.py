'''--------------------------------------------------------------------------
Author: Carlos Flores Valero
Northwestern Polytechnic University, Fremont, CA
Date: 10/17/2019
---------------------------------------------------------------------------'''

#Ex1__________________________________________________
def mk_wd(balance):
  def confirm(x):
    if (balance - x < 0):
      print("Insufficient funds")
      return
    return (balance - x)
  return confirm

#rem = mk_wd(100)
#rem(10)
#rem(20)
#rem(100)
#rem(101)


#Ex2__________________________________________________
def rm_all(elem, lst):
  for i in lst:
    if (i == elem):
      lst.remove(i)
      return rm_all(elem, lst)
  return lst

#x = [3,1,2,1,5,1,1,7]
#rm_all(1, x)


#Ex3__________________________________________________
def add_many(x, elem, lst):
  if (x == 0):
    return lst
  else:
    lst.append(elem)
    return add_many(x-1, elem, lst)

#lst = [1, 2, 4, 2, 1]
#add_many(2, 5, lst)
#lst


#Ex4__________________________________________________
def f(suits, numbers):
  aux = []
  for i in suits:
    for j in range (len(numbers)):
      aux.append(list(set(mrg(list(i), [numbers[j]]))))
  print(aux)

#f(['S', 'C'], [1, 2, 3])


#Ex5__________________________________________________
def mrg(ls1, ls2):
  return list(set(ls1 + ls2))

#mrg([1, 3, 5], [2, 4, 6])
#mrg([], [2, 4, 6])
#mrg([1, 2, 3], [])
#mrg([5, 7], [2, 4, 6])


#Ex6__________________________________________________
tmp = []
def right(tree):
  return tree[1:]
def left(tree):
  return tree[:1]
def root(tree):
  return tree[0]

def fltn(ls):     #Recursion Rocks!!!!
  if ls == []:
    return ls
  if isinstance(root(ls), list):
    return fltn(root(ls)) + fltn(right(ls))
  return left(ls) + fltn(right(ls))

#x = [1, 2, 3]
#x = [1, [2, 3], 4]
#x = [[1, [1, 1]], 1, [1, 1]]
#fltn(x)


#Ex7__________________________________________________
def chk_elm(lst, n):  #SAME IDEA OF #6 BUT USING OR OPERATOR FOR DEAL WITH BOOL
  if lst == []:
    return False
  if isinstance(root(lst), list):
    return chk_elm(root(lst), n) or chk_elm(right(lst), n)
  elif root(lst) == n:
    return True
  else:
    return False or chk_elm(right(lst), n)

#a = [[1, [2]], 3, [[4], [5, [6]]]]
#chk_elm(a, 3)
#chk_elm(a, 6)



#Ex8__________________________________________________
def sym(ls):
  if ls == ls[::-1]:
    return True
  return False

#sym([])
#ym([1])
#sym([1, 4, 5, 1])
#sym([1, 4, 4, 1])
#sym(['l', 'o', 'l'])


#Ex9__________________________________________________
#Ex10_________________________________________________
