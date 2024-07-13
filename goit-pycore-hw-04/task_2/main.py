def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            cats_count = 0
            
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)
                cats_count += 1
                if cats_count == 0:
                    raise ValueError("The file does not contain cats data.")
            
            return cats_info
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as ve:
        print(f"File reading error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")