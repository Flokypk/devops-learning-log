print("CPU Temperature Checker")

cpu_cels = int(input("What's your current CPU temperature in celsius: "))
cpu_warning = 85
cpu_critical = 95

if cpu_cels >= cpu_critical:
    print("Warning Temperature is critical!")
elif cpu_cels >= cpu_warning:
    print("Warning Temperature is high!")
else:
    print("Temperature is safe")

