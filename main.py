import random
import itertools
import datetime
import matplotlib.pyplot as plt
import numpy as np


def generate_objects(nclasses,nitems):
    objects = []
    for nclass in range(nclasses):
        for i in range(nitems):
            price = random.randint(1, 50)
            size = random.randint(1, 50)
            objects.append((nclass+1,i+1,size,price))
    return objects

def generate_all_permutations(nclasses,nitems):
    permutations = itertools.product(range(nitems),repeat=nclasses)
    return permutations


def bruteforce_best_permutation(objects, permutations, item_count):
    start_time = datetime.datetime.now()
    best_permutation_objects = []
    best_price = 0
    best_size = 0
    max_size = int(len(objects)/item_count*20)
    for j,permutation in enumerate(permutations):
        permutation_size = 0
        permutation_price = 0
        permutation_objects = []
        for x,i in enumerate(permutation):
            current_object = objects[x*item_count+i]
            permutation_size += current_object[2]
            permutation_price += current_object[3]
            permutation_objects.append(current_object)
        if permutation_size <= max_size:
            if permutation_price >= best_price:
                best_price = permutation_price
                best_size = permutation_size
                best_permutation_objects = permutation_objects
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f'Calculation duration: {duration} s')
    row_labels = ['Trida', 'Id', 'Objem', 'Cena']
    plt.table(cellText=best_permutation_objects, colLabels=row_labels, loc='center')
    plt.axis('off')
    plt.title(f'Nejlepší kombinace předmětů\nSumy - Objem: {best_size} Cena: {best_price}')
    plt.show()


def test_function(coords,objects,nitems):
    perm_price = 0
    perm_size = 0
    for x,coord in enumerate(coords):
        current_object = objects[x * nitems + coord]
        perm_size += current_object[2]
        perm_price += current_object[3]
    return perm_price,perm_size

def generate_neighbor(center_point,item_count):
    while True:
        neighbor = []
        for item in center_point:
            chance = random.random()
            if chance > 1/len(center_point):
                neighbor.append(random.randint(0, item_count-1))
            else:
                neighbor.append(item)
        if center_point != neighbor:
            break
    return neighbor

def localsearch_best_permutation(objects, item_count, max_iterations, population):
    start_time = datetime.datetime.now()
    center_point = [random.randint(0,item_count-1) for i in range(int(len(objects)/item_count))]
    center_result = test_function(center_point,objects,item_count)
    convergence_results = []
    max_size = int((len(objects) / item_count) * 20)
    best_result = (0, 999999999)
    best_point = 0
    for i in range(max_iterations):
        best_result = (0,999999999)
        best_point = 0
        for x in range(population):
            coords = generate_neighbor(center_point, item_count)
            local_test = test_function(coords, objects, item_count)
            current_price = local_test[0]
            current_size = local_test[1]
            if best_result[0] == 0:
                best_result = center_result
                best_point = center_point
            if current_size <= max_size:
                if current_price >= best_result[0] or best_result[1] > max_size:
                    best_result = local_test
                    best_point = coords
        center_point = best_point
        center_result = best_result
        convergence_results.append(best_result)
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f'Calculation duration: {duration} s \nFor {item_count} items and {int((len(objects) / item_count))} classes')
    best_permutation_objects = [[i+1,item+1,objects[i * item_count + item][2],objects[i * item_count + item][3]] for i,item in enumerate(best_point)]
    row_labels = ['Trida', 'Id', 'Objem', 'Cena']
    plt.table(cellText=best_permutation_objects, colLabels=row_labels, loc='center')
    plt.axis('off')
    plt.title(f'Nejlepší kombinace předmětů\nSumy - Objem: {best_result[1]} Cena: {best_result[0]}')
    plt.show()
    return convergence_results


if __name__ == '__main__':
    class_count = 19
    item_count = 3
    generated_objects = generate_objects(class_count,item_count)

    # possible_permutations = generate_all_permutations(class_count,item_count)
    # bruteforce_best_permutation(generated_objects, possible_permutations,item_count)

    convergence = localsearch_best_permutation(generated_objects,item_count,10000,5)
    swapped_convergence = np.transpose(convergence,axes=[1,0])
    plt.plot(swapped_convergence[0])
    plt.show()