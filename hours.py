def convert_to_24_hour(time_12_hour):
    # Split the input into time and meridian parts
    time_parts = time_12_hour.split()
    
    # Check if there are exactly two parts (time and meridian)
    if len(time_parts) != 2:
        return "Invalid input"
      
    time = time_parts[0]
    meridian = time_parts[1]
    
    # Split the time into hour and minute parts and convert them to integers
    hour, minute = map(int, time.split(':'))
    
    # Check if the meridian is AM or PM and adjust the hour accordingly
    if meridian == "AM" or meridian == "am":
        if hour == 12:
            hour = 0
    elif meridian == "PM" or meridian == "pm":
        if hour != 12:
            hour += 12
    else:
        return "Invalid meridian"
    
    # Return the time in 24-hour format as a formatted string
    return f"{hour:02}:{minute:02}"
    
    time_12_hour = "02:30 PM"
    time_24_hour = convert_to_24_hour(time_12_hour)
    print(time_24_hour)
