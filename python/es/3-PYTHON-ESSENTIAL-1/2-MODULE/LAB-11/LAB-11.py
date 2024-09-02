hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print("Starts at:", hour, ":", mins)

total_mins = hour * 60 + mins + dura
finish_mins = total_mins % 60
finish_hour = (total_mins // 60) % 24


print("Ends at:", finish_hour, ":", finish_mins)