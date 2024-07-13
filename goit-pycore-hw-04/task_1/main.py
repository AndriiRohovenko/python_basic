def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count_employee = 0
            
            for line in file:
                # Split name and salary by comma
                _, salary = line.strip().split(',')
                total_salary += int(salary)
                count_employee += 1
            
            if count_employee == 0:
                raise ValueError("The file does not contain salary data.")
            
            average = total_salary / count_employee
            return total_salary, int(average)
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as ve:
        print(f"File reading error: {ve}")
    except Exception as e:
        print(f"Unknown error: {e}")


if __name__ == "__main__":
    total, average = total_salary("goit-pycore-hw-04\\task_1\\salary_data.txt")
    print(f"Total salaries: {total}, AVG salaries: {average}")