def cal():
    print("Select An Operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Floor division\n6. Modulus\n7. Exponentiation")
    print("Enter a Choice:")

    while True:
        Choice = input("Enter a choice (1/2/3/4/5/6/7): ")
        
        if Choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Please enter num1: "))
                num2 = float(input("Please enter num2: "))
            except ValueError:
                print("Invalid Input. Please enter a correct input.")
                continue
            
            if Choice == '1':
                result = num1 + num2
            elif Choice == '2':
                result = num1 - num2
            elif Choice == '3':
                result = num1 * num2
            elif Choice == '4':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero. Please enter a non-zero value for num2.")
                    continue
            elif Choice == '5':
                result = num1 // num2
            elif Choice == '6':
                result = num1 % num2
            elif Choice == '7':
                result = num1**num2

            print("Result: ", result)

# Call the function
cal()
