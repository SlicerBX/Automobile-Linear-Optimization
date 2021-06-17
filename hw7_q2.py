from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="small-problem", sense=LpMinimize)

# Initialize the decision variables
t1 = LpVariable(name="t1", lowBound=0)
t2 = LpVariable(name="t2", lowBound=0)
t3 = LpVariable(name="t3", lowBound=0)
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)

# Add the constraints to the model
model += (2 - x1 - x2 <= t1, "1st constraint")
model += (2 - x1 - x2 >= - t1, "2nd constrant")
model += (4 - (3 * x1) - x2 <= t2, "3rd constraint")
model += (4 - (3 * x1) - x2 >= - t2, "4th constrant")
model += (8 - (5 * x1) - x2 <= t3, "5th constraint")
model += (8 - (5 * x1) - x2 >= - t3, "6th constrant")

# Add the objective function to the model
obj_func = t1 + t2 + t3
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
