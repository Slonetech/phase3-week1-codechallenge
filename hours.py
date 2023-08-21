def convert_to_24_hour(time_12_hour):
    time_parts = time_12_hour.split()
    
    if len(time_parts) != 2:
        return "Invalid input"
      
    time = time_parts[0]
    meridian = time_parts[1]
    
    hour, minute = map(int, time.split(':'))
      #check if AM OR PM
    if meridian == "AM" or meridian == "am":
        if hour == 12:
            hour = 0
    elif meridian == "PM" or meridian == "pm":
        if hour != 12:
            hour += 12
    else:
        return "Invalid meridian"
    
    return f"{hour:02}:{minute:02}"


time_12_hour = "02:30 PM"
time_24_hour = convert_to_24_hour(time_12_hour)
print(time_24_hour)