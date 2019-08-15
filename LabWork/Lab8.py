import pulp

#Lab 8
#Part 1
problem = pulp.LpProblem("Simple problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x_1", lowBound=0, upBound=None, cat='Continuous')
x2 = pulp.LpVariable("x_2", lowBound=0, upBound=None, cat='Continuous')

objective = x1 + x2, "Objective function to maximize"
problem += objective

c1 = 2 * x1 + x2 <= 4, "First constraint"
c2 = x1 + 2 * x2 <= 3, "Second constraint"
problem += c1
problem += c2

print(problem)
problem.solve()
print("Optimal objective function = ", pulp.value(problem.objective))
for v in problem.variables():
    print(v.name, "=", v.varValue)

#Part 2
diet_Problem = pulp.LpProblem("Cat diet problem", pulp.LpMinimize)
x1 = pulp.LpVariable("Chicken Percentage", lowBound=0)
x2 = pulp.LpVariable("Beef Percentage", lowBound=0)
objective = 0.013 * x1 + 0.008 * x2, "Total cost over weight per can"
diet_Problem += objective
c1 = x1 + x2 == 100, "Percentage"
c2 = 0.07 * x1 + 0.2 * x2 >= 8, "LB on protein"
c3 = 0.08 * x1 + 0.1 * x2 >= 6, "LB on fat"
c4 = 0.001 * x1 + 0.005 * x2 <= 2, "UB on fibers"
c5 = 0.002 * x1 + 0.005 * x2 <= 0.4, "UB on salt"
diet_Problem += c1
diet_Problem += c2
diet_Problem += c3
diet_Problem += c4
diet_Problem += c5
print(diet_Problem)
diet_Problem.solve()
print(pulp.LpStatus[diet_Problem.status])
print(pulp.value(diet_Problem.objective) )
for v in diet_Problem.variables():
    print (v.name, "=", v.varValue, "%")
