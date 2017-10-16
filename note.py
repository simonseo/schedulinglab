class MyClass:
 def __lt__(self, other):
      # return comparison
 def __le__(self, other)
      # return comparison
 def __eq__(self, other)
      # return comparison
 def __ne__(self, other)
      # return comparison
 def __gt__(self, other)
      # return comparison
 def __ge__(self, other)
      # return comparison

class MC(type):
  def __repr__(self):
    return 'Wahaha!'
  def __str__(self):
    return 'Wahaha!'




from operator import attrgetter
from functools import partial
valget = attrgetter('value')
maxval = partial(max, key=valget)
minval = partial(max, key=valget)
sortedval = partial(sorted, key=valget)
sortval = partial(list.sort, key=valget)

Where you call them just as maxval(obj_list) instead of max(obj_list) etc., 
and sortval(obj_list) to sort in-place instead of obj_list.sort()

FCFS
1. create array of processes
2. read in file. init as unstarted
3. print original input
4. sort according to arrival time
5. print sorted processes
while unfinished:
6. print processes
7. put unstarted process into ready
8. if there are no running process then retrieve earliest from ready
9. 