import math
import datetime
import calendar

def math_examples():
    print("Math examples:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi: {math.pi}")
    print(f"Factorial of 5: {math.factorial(5)}")

def datetime_examples():
    now = datetime.datetime.now()
    print("\nDateTime examples:")
    print(f"Current time: {now}")
    print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Days until next year: {(datetime.datetime(now.year + 1, 1, 1) - now).days}")

def calendar_example(year):
    print(f"\nCalendar for {year}:")
    print(calendar.calendar(year))

# Main execution
if __name__ == "__main__":
    math_examples()
    datetime_examples()
    calendar_example(2025)