# Ask the user for the number of seconds
total_seconds = int(input("Enter the number of seconds: "))


minutes = total_seconds // 60
seconds = total_seconds % 60


print(total_seconds, "seconds is equal to", minutes, "minute(s) and", seconds, "second(s).")
