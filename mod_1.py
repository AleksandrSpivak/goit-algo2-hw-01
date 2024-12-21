import sys
import random

# Визначаємо системні обмеження глибини рекурсії
max_length = sys.getrecursionlimit()
print(f"System: max depth of recursion = {max_length}")

#Робимо "запас міцності"
max_length -= 10

def find_min_recursive(arr):
    """
    Функція пошуку мінімального елемента масиву за допомогою рекурсії
    """
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0], find_min_recursive(arr[1:]))

    
def min_max(arr):
    """
    Функція пошуку мінімального та максимального елемента масиву
    """
    if len(arr)>0:
        min = find_min_recursive(arr)
        
        arr = [-x for x in arr]
        max = -find_min_recursive(arr)

        return (min, max)
    else:
        return None

def long_array(arr):
    """
    Функція обробки довгих масивів
    """
    while len(arr)>max_length:
        first_part = arr[:max_length]
        arr = arr[max_length:]
        min, max = min_max(first_part)
        arr.append(min)
        arr.append(max)
    return arr

def check_all_elements_digital(arr):
    """
    Функція перевірки, що всі елементи масиву - числові
    """
    for a in arr:
        if not isinstance(a, (int, float)):
            return False
    return True

def generate_array():
    """
    Функція генерації довгого масиву
    """
    return [random.randint(-1_000_000, 1_000_000) for _ in range(10_000)]


arr = generate_array()

if check_all_elements_digital(arr):

    if len(arr)>0:
        if len(arr)>max_length:
            arr = long_array(arr)

        min, max = min_max(arr)
        print(f"min = {min}\nmax = {max}")
    else:
        print("Array is empty")
else:
    print("Array contains non-digit elements")
