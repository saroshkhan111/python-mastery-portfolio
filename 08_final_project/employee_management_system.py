# ============================================================
# PROGRAM: Employee Management System
# AUTHOR : Sarosh Khan
# DATE   : 04-Sep-2026
#
# PROBLEM:
#   Write a Python program that manages employee records
#   using all data types and operations learned.
#
# DATA TYPES COVERED:
#   1. str        -> Name, Department, Position
#   2. int        -> Employee ID, Age
#   3. float      -> Salary
#   4. list       -> Projects, Skills
#   5. tuple      -> Allowed Departments (fixed data)
#   6. range      -> Valid Employee ID range
#   7. dict       -> Employee Record (nested dictionary)
#   8. set        -> Unique Departments
#   9. frozenset  -> Company Benefits (fixed data)
#  10. bool       -> Active Status
#  11. bytes      -> Encoded Names
#  12. bytearray  -> Modifiable Registry Buffer
#  13. memoryview -> Memory View of the Registry
#  14. complex    -> (Optional) not used in this project
# ============================================================

# ============================================================
# Step 2: DATA - Nested Dictionary (Dictionary of Dictionaries)
#   Key   = Employee ID (unique number)
#   Value = Dictionary with all employee details
# ============================================================

employees = {
    101: {
        "name": "Ali Ahmed",
        "age": 28,
        "department": "IT",
        "position": "Developer",
        "salary": 75000.50,
        "projects": ["Project A", "Project B"],
        "skills": ["Python", "SQL"],
        "is_active": True,
    },
    102: {
        "name": "Sara Khan",
        "age": 25,
        "department": "HR",
        "position": "Recruiter",
        "salary": 55000.00,
        "projects": ["Recruitment 2024"],
        "skills": ["Communication", "HR Software"],
        "is_active": True,
    },
    103: {
        "name": "Ahmed Raza",
        "age": 30,
        "department": "IT",
        "position": "Team Lead",
        "salary": 85000.00,
        "projects": ["Project A", "Project C", "Project D"],
        "skills": ["Python", "Java", "Management"],
        "is_active": True,
    },
    104: {
        "name": "Fatima Noor",
        "age": 27,
        "department": "Finance",
        "position": "Accountant",
        "salary": 62000.00,
        "projects": ["Financial Report 2024"],
        "skills": ["Excel", "QuickBooks"],
        "is_active": True,
    },
    105: {
        "name": "Omar Farooq",
        "age": 35,
        "department": "IT",
        "position": "System Admin",
        "salary": 70000.00,
        "projects": ["Network Setup", "Security Audit"],
        "skills": ["Linux", "Networking", "Security"],
        "is_active": True,
    },
}

# ============================================================
# ALL REMAINING DATA TYPES USED INSIDE THE SYSTEM
# ============================================================

# 5. tuple : non-changing / fixed data
ALLOWED_DEPARTMENTS = ("IT", "HR", "Finance", "Marketing", "Data Science")

# 9. frozenset : fixed company benefits (cannot be changed)
COMPANY_BENEFITS = frozenset({"Health Insurance", "Bonus", "Paid Leave"})

# 8. set : unique departments collected from the employees dictionary
unique_departments = {emp["department"] for emp in employees.values()}

# 6. range : valid employee ID range
EMPLOYEE_ID_RANGE = range(100, 200)

# 11/12/13. bytes + bytearray + memoryview : registry buffer
registry_buffer = bytearray()                       # bytearray (modifiable)
for emp in employees.values():
    registry_buffer.extend(emp["name"].encode("utf-8"))   # bytes (encoded)
registry_view = memoryview(registry_buffer)         # memoryview (no copy)

def validate_employee_data(emp_id, age, salary, department):
    """Check that new employee data follows the project rules."""
    valid_id = emp_id in EMPLOYEE_ID_RANGE          # range membership test
    valid_age = age > 18                            # age must be > 18
    valid_salary = salary > 0                       # salary must be positive
    valid_dept = department in ALLOWED_DEPARTMENTS  # tuple membership test
    return valid_id and valid_age and valid_salary and valid_dept
# ============================================================
# ALGORITHM 1: DISPLAY ALL EMPLOYEES
# ============================================================

def display_employee(emp_id, emp):
    """Print one employee's complete details."""
    print(f"Employee ID: {emp_id}")
    print(f"Name: {emp['name']}")
    print(f"Age: {emp['age']}")
    print(f"Department: {emp['department']}")
    print(f"Position: {emp['position']}")
    print(f"Salary: {emp['salary']:.2f}")
    print(f"Projects: {', '.join(emp['projects'])}")
    print(f"Skills: {', '.join(emp['skills'])}")
    print(f"Active: {emp['is_active']}")
    print()

def display_all_employees(employees):
    """Show the complete list of all employees."""
    print("=" * 50)
    print("ALL EMPLOYEES")
    print("=" * 50)
    print()
    for emp_id, emp in employees.items():
        display_employee(emp_id, emp)

# ============================================================
# ALGORITHM 2: DEPARTMENT-WISE SUMMARY
# ============================================================

def department_summary(employees):
    """Show employee count and average salary per department."""
    print("=" * 50)
    print("DEPARTMENT SUMMARY")
    print("=" * 50)

    dept_data = {}
    for emp in employees.values():
        dept = emp["department"]
        if dept not in dept_data:
            dept_data[dept] = {"count": 0, "total_salary": 0.0}
        dept_data[dept]["count"] += 1
        dept_data[dept]["total_salary"] += emp["salary"]

    for dept, data in dept_data.items():
        avg_salary = data["total_salary"] / data["count"]
        print(f"{dept}: {data['count']} employees, Avg Salary: {avg_salary:.2f}")
    print()

# ============================================================
# ALGORITHM 3: SALARY STATISTICS
# ============================================================

def salary_statistics(employees):
    """Show total, highest, lowest and average salary."""
    print("=" * 50)
    print("SALARY STATISTICS")
    print("=" * 50)

    all_salaries = []
    for emp in employees.values():
        all_salaries.append(emp["salary"])

    total_employees = len(all_salaries)
    highest_salary = max(all_salaries)
    lowest_salary = min(all_salaries)
    average_salary = sum(all_salaries) / total_employees

    print(f"Total Employees: {total_employees}")
    print(f"Highest Salary: {highest_salary:.2f}")
    print(f"Lowest Salary: {lowest_salary:.2f}")
    print(f"Average Salary: {average_salary:.2f}")
    print()

# ============================================================
# ALGORITHM 4: ADD NEW EMPLOYEE
# ============================================================

def add_employee(employees, emp_id, name, age, department, position,
                 salary, projects, skills, is_active=True):
    """Add a new employee after checking for duplicate ID."""
    if emp_id in employees:
        print("Error: Employee already exists!")
        return

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "position": position,
        "salary": salary,
        "projects": projects,
        "skills": skills,
        "is_active": is_active,
    }
    print(f" Employee {emp_id} added successfully!")
    print()

# ============================================================
# ALGORITHM 5: UPDATE EMPLOYEE  (uses **kwargs)
# ============================================================

def update_employee(employees, emp_id, **kwargs):
    """Update one or more fields of an existing employee."""
    if emp_id not in employees:
        print("Error: Employee not found!")
        return

    for field, new_value in kwargs.items():
        if field in employees[emp_id]:
            employees[emp_id][field] = new_value
        else:
            print(f"Field does not exist, skipping: {field}")

    print(f" Employee {emp_id} updated successfully!")
    print()
    print("After Update:")
    display_employee(emp_id, employees[emp_id])

# ============================================================
# ALGORITHM 6: DELETE EMPLOYEE
# ============================================================

def delete_employee(employees, emp_id):
    """Delete an employee and print the remaining employee list."""
    if emp_id in employees:
        del employees[emp_id]
        print(f" Employee {emp_id} deleted successfully!")
        print()
    else:
        print("Error: Employee does not exist!")

    print("After Delete:")
    display_all_employees(employees)
# ============================================================
# MAIN PROGRAM EXECUTION FLOW
# ============================================================

# Welcome banner
print("=" * 60)
print("       EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)
print()

# 1. Display all initial employees
display_all_employees(employees)

# 2. Show department-wise summary
department_summary(employees)

# 3. Show salary statistics
salary_statistics(employees)

# 4. Add new employee -> ID 106
add_employee(
    employees,
    emp_id=106,
    name="Shakir Ali",
    age=32,
    department="Marketing",
    position="Manager",
    salary=65000.00,
    projects=["Marketing Campaign 2024"],
    skills=["Marketing", "Management"],
    is_active=True,
)

# 5. Update employee -> ID 101 (promote position and salary)
update_employee(employees, 101, position="Senior Developer", salary=80000.00)

# 6. Delete employee -> ID 104
delete_employee(employees, 104)

# Final completion message
print("=" * 60)
print("       ALL CONCEPTS DEMONSTRATED SUCCESSFULLY!")
print("=" * 60)