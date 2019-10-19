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
#def f(suits, numbers):

#Ex5__________________________________________________
def mrg(ls1, ls2):
  return list(set(ls1 + ls2))

#mrg([1, 3, 5], [2, 4, 6])
#mrg([], [2, 4, 6])
#mrg([1, 2, 3], [])
#mrg([5, 7], [2, 4, 6])


#Ex6__________________________________________________
tmp = []
def branches(tree):
  return tree[1:]
def is_leaf (tree):
  return not branches(tree)
def root(tree):
  return tree[0]
def fltn(ls):
  if (is_leaf(ls)):
    tmp.append(ls)
  else:
    tmp.append(branches(ls[0]))
    return fltn(branches(ls))
  return tmp
#fltn([1, 2, 3])
x = [1, [2, 3], 4]
fltn(x)
#branches(x)




#Ex7__________________________________________________

#def chk_elm(lst, n):
#  for i in range (lst):
#    for j in range(i):
#      if (x == lst[i][j]):
#        return True
#  return False


#Ex8__________________________________________________
#def sym(ls):


  
