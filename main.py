import random
import itertools
import datetime
import matplotlib.pyplot as plt

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
    best_price = 99999999999
    best_size = 99999999999
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
            if permutation_price <= best_price:
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
    neighbor = []
    for item in center_point:
        chance = random.random()
        if chance > 1/len(center_point):
            neighbor.append(random.randint(0, item_count-1))
        else:
            neighbor.append(item)
    return neighbor

def localsearch_best_permutation(objects, permutations, item_count, max_iterations):
    print('localsearch')


if __name__ == '__main__':
    class_count = 5
    item_count = 3
    # generated_objects = generate_objects(class_count,item_count)
    # possible_permutations = generate_all_permutations(class_count,item_count)
    # bruteforce_best_permutation(generated_objects, possible_permutations,item_count)
    # print(test_function((0,1,0,2,2),generated_objects,item_count))

    test_center = [1,2,0,1,2,1,0,0,2]
    print(generate_neighbor(test_center,3))