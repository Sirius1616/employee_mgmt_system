from flask import Blueprint

# Define a Blueprint for authentication or employee-related routes
bp = Blueprint('auth', __name__)

# -------------------------------
# Employee Routes
# -------------------------------

@bp.route('/employees')
def employees():
    """
    Route: /employees
    Description: Display the list of all employees.
    """
    return "Employee List Page"

@bp.route('/employee/<int:id>')
def employee_detail(id):
    """
    Route: /employee/<id>
    Description: Display details for a specific employee by ID.
    """
    return "Employee Detail Page for Employee ID: {}".format(id)

@bp.route('/employee/add')
def add_employee():
    """
    Route: /employee/add
    Description: Page for adding a new employee.
    """
    return "Add Employee Page"

@bp.route('/employee/edit/<int:id>')
def edit_employee(id):
    """
    Route: /employee/edit/<id>
    Description: Page for editing an existing employee by ID.
    """
    return "Edit Employee Page for Employee ID: {}".format(id)

@bp.route('/employee/delete/<int:id>')
def delete_employee(id):
    """
    Route: /employee/delete/<id>
    Description: Page for deleting an employee by ID.
    """
    return "Delete Employee Page for Employee ID: {}".format(id)

@bp.route('/employee/search')
def search_employee():
    """
    Route: /employee/search
    Description: Page for searching employees.
    """
    return "Search Employee Page"

# -------------------------------
# Filtered Views by Department
# -------------------------------

@bp.route('/employee/department/<string:department>')
def employee_by_department(department):
    """
    Route: /employee/department/<department>
    Description: List employees filtered by department.
    """
    return "Employee List Page for Department: {}".format(department)

@bp.route('/employee/department/<string:department>/active')
def active_employees_by_department(department):
    """
    Route: /employee/department/<department>/active
    Description: List active employees in a specific department.
    """
    return "Active Employees List Page for Department: {}".format(department)

@bp.route('/employee/department/<string:department>/inactive')
def inactive_employees_by_department(department):
    """
    Route: /employee/department/<department>/inactive
    Description: List inactive employees in a specific department.
    """
    return "Inactive Employees List Page for Department: {}".format(department)

# -------------------------------
# Filtered Views by Role
# -------------------------------

@bp.route('/employee/role/<string:role>')
def employee_by_role(role):
    """
    Route: /employee/role/<role>
    Description: List employees filtered by role.
    """
    return "Employee List Page for Role: {}".format(role)

@bp.route('/employee/role/<string:role>/active')
def active_employees_by_role(role):
    """
    Route: /employee/role/<role>/active
    Description: List active employees filtered by role.
    """
    return "Active Employees List Page for Role: {}".format(role)

# -------------------------------
# Status-Based Views
# -------------------------------

@bp.route('/employee/active')
def active_employees():
    """
    Route: /employee/active
    Description: List all active employees.
    """
    return "Active Employees List Page"

@bp.route('/employee/inactive')
def inactive_employees():
    """
    Route: /employee/inactive
    Description: List all inactive employees.
    """
    return "Inactive Employees List Page"
@bp.route('/employee/terminated')
def terminated_employees():
    """
    Route: /employee/terminated
    Description: List all terminated employees.
    """
    return "Terminated Employees List Page"
@bp.route('/employee/archived')
def archived_employees():
    """
    Route: /employee/archived
    Description: List all archived employees.
    """
    return "Archived Employees List Page"