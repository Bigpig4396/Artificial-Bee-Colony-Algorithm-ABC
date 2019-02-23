# original ABC
import random
import matplotlib.pyplot as plt
# optimize y = x ^ 2 for x in [-500, 500]

def find_max_index(my_list):
    index = 0
    max_value = my_list[index]
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
            index = i
    return index

N_w = 50    # number of workers
N_s = 10    # number of scouts
N_all = N_w + N_s   # number of all the bees
max_limit = 10
max_opt_iter = 100
pos_list = []
fitness_list = []
limit_list = []
opt_fitness_list = []

# initialization
for i in range(N_all):
    pos = 1000*(random.random()-0.5)
    pos_list.append(pos)
    fitness = -pos * pos
    fitness_list.append(fitness)
    limit_list.append(0)


index = find_max_index(fitness_list)
g_best_pos = pos_list[index]
g_best_fitness = fitness_list[index]

print(g_best_fitness)
# start optimization
for opt_iter in range(max_opt_iter):
    #print(opt_iter)
    for i in range(N_w):
        # choose a neighbour
        neigh_index = random.randint(0, N_all - 1)
        while neigh_index == i:
            neigh_index = random.randint(0, N_all - 1)

        # calculate new pos
        temp_pos = pos_list[i] + 2*(random.random()-0.5)*(pos_list[neigh_index] - pos_list[i])

        # bound new pos
        if temp_pos > 500:
            temp_pos = 500
        if temp_pos < -500:
            temp_pos = -500

        # calculate fitness
        temp_fitness = -temp_pos * temp_pos

        # update self fitness and pos
        if temp_fitness > fitness_list[i]:
            fitness_list[i] = temp_fitness
            pos_list[i] = temp_pos
            limit_list[i] = 0
        else:
            limit_list[i] = limit_list[i] + 1

        if limit_list[i] > max_limit:
            pos_list[i] = 1000*(random.random()-0.5)

    for i in range(N_w, N_w+N_s):
        # choose a new pos
        pos_list[i] = 1000 * (random.random() - 0.5)

        # calculate fitness
        fitness_list[i] = -pos_list[i] * pos_list[i]

    # update global best pos
    index = find_max_index(fitness_list)
    if fitness_list[index] > g_best_fitness:
        g_best_pos = pos_list[index]
        g_best_fitness = fitness_list[index]

    opt_fitness_list.append(g_best_fitness)

x = range(max_opt_iter)
plt.plot(x, opt_fitness_list)
plt.show()