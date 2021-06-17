from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)
z = LpVariable(name="z", lowBound=0)

# Add the constraints to the model
model += (x + y + 2 * z <= 3, "1st constraint")
model += (x - y + z == 1, "2nd constraint")
model += (2 * x + y - z >= 2, "3rd constraint")

# Add the objective function to the model
obj_func = x + y + z
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
