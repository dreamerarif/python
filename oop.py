#john=["John Doe", 30, "Manager", 2001]
#Bob=["Bob Mccoy", 27, "Developer", 2004]
#Alice=["Alice Spock", "HR", 2015]

class Employee:
    employeeType = "Full Time" # Class attribute
    def __init__(self, name, age, designation, joiningYear, salary):
        # name1, age1, designation1, joiningYear1 = Instance attributes
        self.name1 = name
        self.age1 = age
        self.designation1 = designation
        self.joiningYear1 = joiningYear
        self.salary1 = salary
    
    def promote(self, promotedDesignation):
        self.designation1 = promotedDesignation
    def salaryIncrement(self, increment):
        #self.salary1 = self.salary1 + increment
        self.salary1 += increment
    
john= Employee("John Doe", 30, "Manager", 2001, 30000)
bob= Employee("Bob Mccoy", 27, "Developer", 2004, 20000)

#print(john.name1, '\n', john.employeeType)

#print(john == bob)

#john.age1 = 32

print(john.name1, "is a", john.designation1)

john.promote("Director")
print(john.name1, "is a", john.designation1)

john.salaryIncrement(10000)
print("New Salary of John:", john.salary1)

print("Salary of Bob:",bob.salary1)

bob.salaryIncrement(5000)
print("New salary of Bob:",bob.salary1)