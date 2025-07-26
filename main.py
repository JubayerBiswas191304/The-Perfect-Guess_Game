from random import randint
print("guess the number in 1 to 100")
guesses=1
a=-1
n=randint(1,100)
while(n!=a):
    a=int(input("Guess the number: "))
    
    if(a>n):
        print("lower number please!\n")
        guesses+=1
    elif(a<n):
        print("higher number please!\n")
        guesses+=1
    

print(f"You guessed {n} correctly in {guesses} attempts")
