import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  if n == 0: #Base case, if you are on zero
      d.push(s.pop()) #Pop from the s stack and place in d stack
  else: #Recursive case
      Hanoi_rec(n - 1, s, d, a) #Calls Hanoi_rec with n-1 to move from s stack to a stack with d stack
      d.push(s.pop()) #Pop from the s stack and place in d stack
      Hanoi_rec(n - 1, a, s, d) #Calls Hanoi_rec with n-1 to move from a stack to d stack with s stack
  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
