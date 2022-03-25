# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    user_input = input("Please enter a number")
    sum = 0
    sum += user_input
    if user_input == 0 or sum == 0:
        return sum 
        
    pass


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
