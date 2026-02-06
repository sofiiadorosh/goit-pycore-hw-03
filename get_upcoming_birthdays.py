from datetime import datetime, timedelta

SATURDAY_WEEKDAY = 5
WEEK_DAYS = 7

def get_upcoming_birthdays(users):
    today = datetime.today()
    today_date = today.date()
    in_seven_days_date = (today + timedelta(days=WEEK_DAYS)).date()

    upcoming_birthdays = []

    for user in users:
        name, birthday = user["name"], user["birthday"]

        try:
            birthday_datetime = datetime.strptime(birthday, "%Y.%m.%d")
        except ValueError:
            print(f"⚠️ Invalid birthday for {name}: {birthday}, skipping")
            continue

        try:
            birthday_this_year_date = datetime(
                year=today_date.year,
                month=birthday_datetime.month,
                day=birthday_datetime.day
            )
        except ValueError:
            print(f"⚠️ Cannot find birthday this year for {name}: {birthday}")
            continue

        if today_date < birthday_this_year_date.date() < in_seven_days_date:
            birthday_weekday = birthday_this_year_date.weekday()

            if birthday_weekday >= SATURDAY_WEEKDAY:
                birthday_this_year_date += timedelta(days=WEEK_DAYS - birthday_weekday)

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

birthday_users = [
    {"name": "John Doe", "birthday": "1985.02.08"},
    {"name": "Jane Smith", "birthday": "1990.02.11"},
    {"name": "Jane Doe", "birthday": "1989.02.24"}
]
seven_days_birthdays = get_upcoming_birthdays(birthday_users)
print("Список привітань на цьому тижні:", seven_days_birthdays)
