Test
You are given an array of N integers. you want to split them using N/2 pairs in such a way that the sum of intergers in each pair is odd. N is even and every element on the array must be present in exactly on pair.
your task is to determine whether it is possible to split the number into such pairs. For exmaple, given [2,7,4,6,3,1], the answer is True. One of the possible sets of pairs is (2,7), (6,3), (4,1). Their sums are respectively 9,9, and 5 all of which are odd. 

write a function: 
def solution(A)

which, given an array of integers A of length N, returns True
when it is possible to create the required parirs and False otherwise.
Example:
given A = [2,7,4,6,3,1] the function should return True, 
given A = [-1,1] it should return False
as the sum of pair is even.
