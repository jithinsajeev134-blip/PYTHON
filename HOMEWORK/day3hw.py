# Step 1: Boolean variables
is_logged_in = True
is_subscribed = False

# Step 2: Credit initialization
user_credits = 100
max_credits = 200
min_credits = 50

# Step 3: Check if credits are valid
credits_valid = min_credits < user_credits <= max_credits

# Step 4: Bonus eligibility
bonus_eligible = is_subscribed or not (user_credits <= min_credits)

# Step 5: Modify user_credits
user_credits += 50      # 100 + 50 = 150
user_credits -= 20      # 150 - 20 = 130
user_credits *= 2       # 130 * 2 = 260
user_credits %= 150     # 260 % 150 = 110

# Step 6: Compute square
power_result = user_credits ** 2  # 110^2 = 12100

# Step 7: Logical AND for full access
full_access = is_logged_in and is_subscribed

# Step 8: Identity check
is_true_login = is_logged_in is True

# Step 9: Operator precedence
access_result = is_logged_in or is_subscribed and False

print("Is logged in:", is_logged_in)
print("Is subscribed:", is_subscribed)
print("Credits valid:", credits_valid)
print("Bonus eligible:", bonus_eligible)
print("Final user credits:", user_credits)
print("Power result:", power_result)
print("Full access:", full_access)
print("Is true login:", is_true_login)
print("Access result (precedence demo):", access_result)