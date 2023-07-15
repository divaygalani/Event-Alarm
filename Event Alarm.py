from datetime import datetime, timedelta
from time import sleep
import winsound
import msvcrt

# Create empty lists to store event names and alarm times
event_names = []
alarm_times = []

# Prompt the user to enter multiple events and alarm times
while True:
    event_name = input("Enter the name of the event (or 'q' to stop entering events): ")
    if event_name.lower() == 'q':
        break
    alarm_date = input("Enter the date for the alarm in 'DD-MM-YYYY' format: ")
    alarm_time = input("Enter the time for the alarm in 'HH:MM' format: ")

    # Convert the entered date and time into a datetime object
    alarm_time = datetime.strptime(f"{alarm_date} {alarm_time}", '%d-%m-%Y %H:%M')

    # Calculate and display the time remaining until the alarm rings
    time_remaining = alarm_time - datetime.now()
    time_remaining = time_remaining - timedelta(microseconds=time_remaining.microseconds)
    print(f"The alarm for {event_name} will ring in {time_remaining}")

    # Add the entered event name and alarm time to their respective lists
    event_names.append(event_name)
    alarm_times.append(alarm_time)

# Print a message saying how many alarms have been set
print(f"{len(alarm_times)} alarms have been set.")

# Enter an infinite loop to check the alarm times
while True:
    current_time = datetime.now()
    for i, alarm_time in enumerate(alarm_times):
        if current_time >= alarm_time:
            # If an alarm time is greater than or equal to the current time, print a message and play a beep sound
            print(f"Alarm ringing for {event_names[i]}! \nPress 'x' to stop the alarm or 's' to snooze for 5 minutes.")
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode().lower()
                    if key == 'x':
                        # If the user presses 'x', stop the alarm and remove it from the lists
                        event_names.pop(i)
                        alarm_times.pop(i)
                        break
                    elif key == 's':
                        # If the user presses 's', snooze the alarm for 5 minutes
                        snooze_time = timedelta(minutes=5)
                        new_alarm_time = current_time + snooze_time
                        print(f"Snoozing alarm for {event_names[i]} until {new_alarm_time.strftime('%H:%M')}")
                        alarm_times[i] = new_alarm_time
                        break
                winsound.Beep(2500, 1000)
            break
    # If there are no remaining alarm times, break out of the infinite loop and end the program
    if not alarm_times:
        break
    sleep(1)