def divide_numbers():
    try:
        # Ask users for 2 nums
        dividend=float(input("Enter dividend"))
        divisor=float(input("Enter the divisor"))

        # Perform Division
        result=dividend/divisor
        print(result)

    except ZeroDivisionError:
        # handle the case where divison  is done by 0
        print("Divsion by 0 is not allowed")

    except ValueError:
        # handle the case were the divisor is non numeric
        print("Error: please enter valid numeric values")

    except Exception as e:
        # handle any other Exception
        print("Somthing wen wrong")


divide_numbers()