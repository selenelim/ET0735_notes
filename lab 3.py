W3 schools python 


1. Git & GitHub Commands
    git init - Initialize a new Git repository
    git clone <url> - Clone a GitHub repository
    git status - Check status of your working directory
    git add <file> - Stage specific file(s)
    git add . - Stage all changes
    git commit -m "message" - Commit changes with message
    git push origin main - Push commits to GitHub
    git pull origin main - Pull latest updates from GitHub
    git log - Show commit history
    git branch -M main - Rename current branch to 'main'
    git remote -v - Show connected remotes
    git remote add origin <url> - Link to a GitHub repo
2. Creating a GitHub Release
    1. Push your changes to GitHub.
    2. Go to your repository page on GitHub.
    3. Click on "Releases" > "Draft a new release".
    4. Tag version: Lab3_v4.0 or Lab3_v5.0
    5. Title and describe your changes.
    6. Publish release.
3. Terminal Commands for File Navigation
    pwd - Print working directory (where you are)
    ls - List files in current directory
    cd folder_name - Change directory into 'folder_name'
    cd .. - Move back one directory
    cd - Go to home directory
    mkdir name - Create new directory
    touch file.py - Create a new file (Linux/Mac)
    del file.py - Delete a file (Windows)
    rm file.py - Delete a file (Linux/Mac)
    rmdir folder - Remove empty folder
    code . - Open folder in VS Code (if installed)


1. Python Dictionary Methods
    .get(key, default): Access a value safely without error.
    price = fruit_prices.get("apple", 0)

    .items(): Returns all key-value pairs.
    for fruit, price in fruit_prices.items():
        print(f"{fruit}: {price}")

    .keys(): Returns all keys.
    for key in fruit_prices.keys():
        print(key)

    .values(): Returns all values.
    for val in fruit_prices.values():
        print(val)

    .update(): Add or change values.
    fruit_prices.update({"kiwi": 2.0})

    .pop(key): Remove item by key.
    fruit_prices.pop("banana")

2. Code for price_info.py
    price_list = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 1.8
    }
    quantity_list = {
    "apple": 2,
    "banana": 3,
    "orange": 1
    }
    def cost_of_fruit(fruit, quantity):
        return price_list.get(fruit, 0) * quantity

    def total_cost_shopping():
        total = 0
         for fruit, quantity in quantity_list.items():
            price = price_list.get(fruit, 0)
            total += price * quantity

            return total
   
3. Unit Tests for price_info.py
    import pytest
    from price_info import cost_of_fruit, total_cost_shopping

    def test_cost_of_fruit():
        assert cost_of_fruit("apple", 2) == 5.0
    def test_total_cost_shopping():
        assert total_cost_shopping() == 9.1

4. Code for employee_info.py
    employees = [
    {"name": "Alice", "age": 30, "department": "Sales", "salary": 3000},
    {"name": "Bob", "age": 25, "department": "HR", "salary": 2800},
    {"name": "Charlie", "age": 35, "department": "IT", "salary": 3200}
    ]
    def calculate_average_salary():
        total = sum(e["salary"] for e in employees)
    return total / len(employees)
    def get_employees_by_age_range(min_age, max_age):
        return [e for e in employees if min_age <= e["age"] <= max_age]
    def get_employees_by_dept(department):
        return [e for e in employees if e["department"] == department]

5. Unit Tests for employee_info.py
    import pytest
    from employee_info import calculate_average_salary, get_employees_by_age_range, get_employees_by_dept

    def test_average_salary():
        assert calculate_average_salary() == 3000
    def test_employees_by_age():
        result = get_employees_by_age_range(25, 30)
        assert len(result) == 2
    def test_employees_by_dept():
        result = get_employees_by_dept("Sales")
        assert result[0]["name"] == "Alice"