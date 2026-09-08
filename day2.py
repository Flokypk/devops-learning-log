print("Weekly DevOps Study Planner")

minutes_per_day = int(input("How many minutes will you study each day "))

days_per_week = int(input("How many days will you study each week? "))

weekly_minutes = minutes_per_day * days_per_week

print("You will study", weekly_minutes, "minutes each week.")

weekly_goal = 600

if weekly_minutes >= weekly_goal:
    print("You reached your weekly goal!")
else:
    minutes_needed = weekly_goal - weekly_minutes
    print("You need", minutes_needed, "more minutes to reach your goal.")