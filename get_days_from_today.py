from datetime import datetime

def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d")
        today_object = datetime.today()
        return (today_object - datetime_object).days
    except ValueError:
        print(f"⚠️ Invalid date format: '{date}', expected YYYY-MM-DD")
        return None

first_day = get_days_from_today("2026-01-01")
incorrect_day = get_days_from_today("2025.01.09")

print(first_day)
print(incorrect_day)