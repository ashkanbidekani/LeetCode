#I want to wirte a program to recognize a number which is palindrome.
rev=0
#Function
def isPalindrome (x,rev):
    if x < 0:
            return False      
    rev=0
    i=x
#loop
    while i!=0:
         j=i%10
         rev = (rev*10)+j
         i=i//10
    return rev == x
x=int(input('Please send your number \n'))
totall=isPalindrome(x , rev)
print (x,"is",totall,",I mean it's a polindrome number")
