# Written by: Katherine Epifanio

import copy
import random

# Initiate boxes to choose from
box_set = []
box_set.append((1, 20, 6))
box_set.append((2, 30, 5))
box_set.append((3, 60, 8))
box_set.append((4, 90, 7))
box_set.append((5, 50, 6))
box_set.append((6, 70, 9))
box_set.append((7, 30, 4))
box_set.append((8, 30, 5))
box_set.append((9, 70, 4))
box_set.append((10, 20, 9))
box_set.append((11, 20, 2))
box_set.append((12, 60, 1))

# Set up initial population
def init():
    init_pop = []
    init_pop.append([(1, 20, 6)])
    init_pop.append([(2, 30, 5)])
    init_pop.append([(3, 60, 8)])
    init_pop.append([(4, 90, 7)])
    init_pop.append([(5, 50, 6)])
    init_pop.append([(6, 70, 9)])
    init_pop.append([(7, 30, 4)])
    init_pop.append([(8, 30, 5)])
    init_pop.append([(9, 70, 4)])
    init_pop.append([(10, 20, 9)])
    init_pop.append([(11, 20, 2)])
    init_pop.append([(12, 60, 1)])
    return init_pop

# Mutation Function
def mutate(new, pop):
    rand_value = random.randint(1, 5)
    if rand_value == 2:
        print("MUTATION:   swapping " + str(new) + "    ")
        mut_type = "swap"
        new = add_or_swap(new, mut_type)
        print("            with " + str(new))
    elif rand_value == 4:
        print("MUTATION:     adding " + str(new) + "    ")
        mut_type = "add"
        new = add_or_swap(new, mut_type)
        print("              to " + str(new))

    # Check score
    new.sort()
    if get_score(new) == 300:
        return new

    # Check that mutation doesn't already exist
    non_repeat = True
    for i in pop:
        if i == new:
            non_repeat = False
    if non_repeat == True:
        pop.append(new)

    return pop

# Reproduction Function
def reproduce(pop, size):
    while len(pop) < size:
        pop_len = len(pop)
        x = 0
        y = 0
        while x == y:
            x = random.randint(0, pop_len-1)
            y = random.randint(0, pop_len-1)
        print("CROSS:      crossing " + str(pop[x]))
        print("            with " + str(pop[y]))

        if len(pop[y]) > 1 and len(pop[x]) > 1:
            new = crossover(copy.deepcopy(pop[y]), copy.deepcopy(pop[x]))
        else:
            new = copy.deepcopy(pop[y])

        # Facilitate mutation
        pop = mutate(new, pop)

    return pop

# Main function that drives the solution
def solve(curr_pop, rounds):
    # Initiate a second population
    pop_2 = []
    size = len(curr_pop)

    # Keep track of best score
    for i in range(size - int((size/2))):
        best_index = 0
        best_score = 0
        pop_len = len(curr_pop)
        for j in range(pop_len):
            if best_score < get_score(curr_pop[j]):
                best_index = j
                best_score = get_score(curr_pop[j])

        # Prevent algorithm from running too long
        if rounds == 30:
            return curr_pop[best_index]
        else:
            pop_2.append(curr_pop[best_index])
            del curr_pop[best_index]

    # Facilitate reproduction
    pop_2 = reproduce(pop_2, size)
    return solve(pop_2, rounds+1)

# Performs actual adding or swapping of boxes
def add_or_swap(x, mutation_type):
    weight_val = set()
    y = copy.deepcopy(x)
    for i in x:
        weight_val.add(i[0]-1)
    while True:
        mutation = random.randint(0, 11)
        while mutation in weight_val:
            mutation = random.randint(0, 11)
        if(mutation_type == "swap"):
            swap_box = random.randint(0, len(x)-1)
            x[swap_box] = box_set[mutation]
        else:
            x.append(box_set[mutation])

        if check_wght(x):
            return x
        else:
            x = copy.deepcopy(y)
            return x

# Swaps two boxes
def crossover(x, y):
    weight_val = set()
    temp = copy.deepcopy(x)
    for i in x:
        weight_val.add(i[0]-1)
    while True:
        mutation = random.randint(0, 11)
        while mutation in weight_val:
            mutation = random.randint(0, 11)
        swap_box = random.randint(0, len(x)-1)
        x[swap_box] = box_set[mutation]
        if check_wght(x):
            return x
        else:
            x = copy.deepcopy(temp)
            tokeep = random.randint(1, 3)
            if tokeep == 1:
                return x
            else:
                return y

# Checks if we are ready to return a solution due to current weight
def check_wght(x):
    weight = 0
    for i in x:
        weight = weight + i[1]
    if weight <= 250:
        return True
    else:
        return False


# Checks if we are ready to return a solution due to current score
def get_score(x):
    score = 0
    for i in x:
            score = score + i[1]
    return score


# Runs the program
solution = solve(init(), 0)
print("\n\n\n\n             *#*#*# SOLUTION #*#*#* \n")
total = 0
for i in solution:
    total += int(i[1])
print(str(solution))
print("Total Weight: " + str(total))
print("\n\n")
