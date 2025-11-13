# Step 1: Basic account and email status
has_account = True
email_verified = False

# Step 2: Initial login check
can_login = has_account and email_verified

# Step 3: Email validation
email = "g@example.com"
is_email_valid = "@" in email

# Step 4: Age verification
user_age = 17
is_age_valid = user_age >= 18

# Step 5: Final login logic
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

# Step 6: Print results
print("Can login (basic check):", can_login)
print("Is email valid:", is_email_valid)
print("Is age valid:", is_age_valid)
print("Can login (final check):", can_login_final)

# Step 7: Identity check
print("Has account is True:", has_account is True)