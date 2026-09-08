print("DevOps Disk Usage Checker")

user_usage = int(input("What is the current disk usage percentage? "))
usage_warning = 80

if user_usage >= usage_warning: 
    print("Warning disk usage is high.")
else:
    print("Disk usage is healthy.")