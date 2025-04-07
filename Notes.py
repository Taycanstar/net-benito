guess = 0
tries = 0
low = 1
high = 387
midpoint = (low + high) // 2
dollar = 27
while guess != dollar:
    midpoint = (low + high) // 2
    print("Midpoint is ", midpoint)
    guess = int(input("Enter a number "))
    if guess < dollar:
        print("Too Low :)")
        low = guess
        tries = tries + 1
        print("Attempts:", tries)
    elif guess > dollar:
        high = guess
        print("Too High :)")
        tries = tries + 1
        print("Attempts:", tries)   
print("Lucky guess >:(")
print("It took you", tries, "attempts")