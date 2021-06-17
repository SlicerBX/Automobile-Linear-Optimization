from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="small-problem", sense=LpMinimize)

# Initialize the decision variables
C1 = LpVariable(name="C1", lowBound=0) # cars produced month 1
C2 = LpVariable(name="C2", lowBound=0) # cars produced month 2
C3 = LpVariable(name="C3", lowBound=0) # cars produced month 3
C4 = LpVariable(name="C4", lowBound=0) # cars produced month 4

LC1 = LpVariable(name="LC1", lowBound=0) # num. of cars in inventory at end of month 1
LC2 = LpVariable(name="LC2", lowBound=0) # num. of cars in inventory at end of month 2
LC3 = LpVariable(name="LC3", lowBound=0) # num. of cars in inventory at end of month 3
LC4 = LpVariable(name="LC4", lowBound=0) # num. of cars in inventory at end of month 4

PC1 = LpVariable(name="PC1", lowBound=0) # production capacity increase for month 1
PC2 = LpVariable(name="PC2", lowBound=0) # production capacity increase for month 2
PC3 = LpVariable(name="PC3", lowBound=0) # production capacity increase for month 3
PC4 = LpVariable(name="PC4", lowBound=0) # production capacity increase for month 4

EC1 = LpVariable(name="EC1", lowBound=0) # cars under prodcution capacity for month 1
EC2 = LpVariable(name="EC2", lowBound=0) # cars under prodcution capacity for month 2
EC3 = LpVariable(name="EC3", lowBound=0) # cars under prodcution capacity for month 3
EC4 = LpVariable(name="EC4", lowBound=0) # cars under prodcution capacity for month 4


# Add the constraints to the model
# constraints for cars produced
model += (C1 <= 3000, "month 1 car production constraint")
model += (C2 <= 3000, "month 2 car production constraint")
model += (C3 <= 3000, "month 3 car production constraint")
model += (C4 <= 3000, "month 4 car production constraint")
# constraints for extra cars produced from changes in production capacity
model += (EC1 == PC1, "month 1 car increase production constraint")
model += (EC2 == PC2, "month 2 car increase production constraint")
model += (EC3 == PC3, "month 3 car increase production constraint")
model += (EC4 == PC4, "month 4 car increase production constraint")
# constraints for demands and holding inventory at end of month
model += (300 + C1 + EC1 == 4000 + LC1, "month 1 demands and excess loading constraint")
model += (LC1 + C2 + EC2 == 2000 + LC2, "month 2 demands and excess loading constraint")
model += (LC2 + C3 + EC3 == 5000 + LC3, "month 3 demands and excess loading constraint")
model += (LC3 + C4 + EC4 == 1000 + LC4, "month 4 demands and excess loading constraint")
# requirement at the end of month 4
model += (LC4 >= 4000, "FINAL month 4 capacity constraint")

# Add the objective function to the model
obj_func = 150 * (LC1 + LC2 + LC3 + LC4) + 3000 * (C1 + C2 + C3 + C4 + EC1 + EC2 + EC3 + EC4) + 100 * (PC1 + PC2 + PC3 + PC4) + 50 * (EC1 + EC2 + EC3 + EC4)
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
