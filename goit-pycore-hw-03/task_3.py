import re

def normalize_phone(phone_number):
    try:
        # Remove all characters except digits and '+'
        pattern = r'[^\d+]'
        phone_number = re.sub(pattern, '', phone_number)
        
        if phone_number.startswith('+'):
            if not phone_number.startswith('+380'):
            # If it doesn't start with '+380', change it to '+38'
                phone_number = '+38' + phone_number[1:]
        else:
            # If it starts with '380', add '+'
            if phone_number.startswith('380'):
                phone_number = '+' + phone_number
            else:
                # Otherwise, add '+38' at the beginning
                phone_number = '+38' + phone_number
        print(phone_number)
        return phone_number
    except Exception as ex:
        print(f"An unknown error has occurred! {ex}")