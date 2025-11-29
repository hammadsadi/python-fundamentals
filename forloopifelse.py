is_successful = True
for number in range(3):
    print("Sending Messages", number +1)

    if is_successful:
        print("Successful Delivery")
        break

else:
        print("Failed Delivery")