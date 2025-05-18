# lib/testing/debug.py
from __init__ import CONN, CURSOR
from department import Department

# Drop and recreate the table
Department.drop_table()
Department.create_table()

# Create and save departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
hr = Department.create("Human Resources", "Building C, East Wing")

# Test update/delete
hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()

payroll.delete()  # Delete payroll (but object still exists in memory)

# Enter debugger to inspect
import ipdb; ipdb.set_trace()