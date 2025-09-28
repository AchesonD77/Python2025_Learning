# we have multiple conditions
# two conditions, have high income and good credit, eligible for laon
# and / or, and for both, or for at least one of them is true.
has_high_income = True
has_good_credit = True
# 1 and: both
if has_good_credit and has_high_income:
    print("And condition: Eligible for loan")
# 2 or: at least one
elif has_good_credit or has_high_income:
    print("Or condition: Eligible for loan")
# 3 Not: change it to another side
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("You are good")