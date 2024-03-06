class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        List_Values=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                List_Values.append("FizzBuzz")
            elif i%3==0:
                List_Values.append("Fizz")
            elif i%5==0:
                List_Values.append("Buzz")
            else:
                List_Values.append(str(i))
        return List_Values
            
