ans=True
while ans:
    print("""
    Welcome to the Collatz Conjecture attacker.

    1.Bruteforce
    2.Enter integer
    3.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      num = 1
      while True:
        print(f'Checking number: {num}')
        temp = num
        steps = 0
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = temp * 3 + 1
            steps += 1
        print(f'We have reached {temp} from {num}, it took: {steps} steps.')
        num += 1  # increment the number for the next iteration
    elif ans=="2":
      num = input("Please enter a integer:")
      try:
        num = int(num)
        steps = 0
        while num != 1:
            print(f'We are at: {num}')
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            steps += 1
        print(f'We have reached {num}, it took: {steps} steps.')  # To print 1 at the end
      except ValueError:
        print("Not a valid integer. Please try again.")
    elif ans=="3":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
