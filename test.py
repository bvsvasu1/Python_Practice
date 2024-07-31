try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    print(total_value,value)
    print(f"That is {(value/total_value)*100}")
except Exception as e:
    print(e,ValueError)
    raise e

# except ValueError as e:
#     if e==ValueError:
#         print("You need to enter a number. Run the program again.")

# total_value = float(input("Enter total value: "))
# value = float(input("Enter value: "))
# print(total_value,value)
# print(f"That is {(value/total_value)*100}")