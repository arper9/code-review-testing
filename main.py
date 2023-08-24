

# Initialize the price_threshold variable
price_threshold = 2999

# Check if the user is eligible to purchase Dsa Self Paced
if amount >= price_threshold:
    print("You are eligible to purchase Dsa Self Paced")
else:
    print("The purchase amount is lower than the threshold")
    
# Test value
test_value = 78

# Test code
if test_value >= price_threshold:
    print("The test value is eligible to purchase Dsa Self Paced")
else:
    print("The test value is lower than the threshold")