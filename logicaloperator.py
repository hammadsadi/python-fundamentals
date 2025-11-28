#  Logical Operators in Python
# and, or, not

high_income = False
good_credit = False
is_student= False


# Using 'and' operator
if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")



    # Using 'or' operator
    if high_income or good_credit:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")

        # Using 'not' operator
if not is_student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


    # Combining logical operators
    if (high_income or good_credit) and is_student:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")