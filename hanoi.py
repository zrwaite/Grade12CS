def hanoi(fr, to, tp, n):
   '''receive from, to and temp peg values, with n - the number of the ring
    use recursion to detemine movement of each disc'''
   if n == 1:
      print("Move disc 1 from "+fr+" to "+to)
   else:
      hanoi(fr, tp, to, n - 1)
      print("Move disc",n,"from "+fr+" to "+to)
      hanoi(tp, to, fr, n - 1)

from_peg = "A"
to_peg = "C"
temp_peg = "B"
#begin Towers of Hanoi with 4 disks
n = 4
print("Towers of Hanoi problem")
print("There are " , n , " discs on peg " + from_peg + " initially")
#Execute hanoi method to solve the problem
hanoi(from_peg, to_peg, temp_peg, n)
