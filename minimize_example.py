from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="small-problem", sense=LpMinimize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# Add the constraints to the model
model += (x + 2 * y >= 40, "1st constraint")
model += (x + y >= 30, "2nd constrant")

# Add the objective function to the model
obj_func = 12 * x + 16 * y
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
