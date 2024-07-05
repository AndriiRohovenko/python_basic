from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert string in format 'YYYY-MM-DD' to datetime object
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # Get current date
        today = datetime.today().date()
        
        # Get the date part of the datetime object
        date_obj = date_obj.date()
        
        # Calculate the difference in days
        result = today - date_obj
        
        return result.days
    except ValueError:
        return "Incorrect date format. Please use the format 'YYYY-MM-DD'."
    except Exception as ex:
            print(f"An unknown error has occurred! {ex}")