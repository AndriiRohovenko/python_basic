from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    try:
        today = datetime.today().date()
        upcoming_birthdays = []
        one_week_from_today = today + timedelta(days=7)

        for user in users:
            name = user["name"]
            birthday = user["birthday"]
            birthday_date = datetime.strptime(birthday, "%Y.%m.%d").date()
            
            # Create anoter obj and Change the user birthday to current year for comparing
            birthday_this_year = birthday_date.replace(year=today.year)
            
            # If the birthday already passed in current year, check for the next year
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)      
            
            # Check if the birthday in next 7 days
            if today <= birthday_this_year <= one_week_from_today:
                # If the birthday is on the weekend, move it to the next Monday
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year
                
                upcoming_birthdays.append({
                    "name": name,
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })

        return upcoming_birthdays
    except Exception as ex:
            print(f"An unknown error has occurred! {ex}")