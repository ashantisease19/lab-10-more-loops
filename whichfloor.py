maximum_stories = 50
userstring = input("You've been demoted. You don't have access to floors above the 50th.")
usernum = int(userstring)

while usernum > maximum_stories:
    print("You do not have clearance to these floors. Do not proceed further.")


print("Thank you for staying in your proper place.")
