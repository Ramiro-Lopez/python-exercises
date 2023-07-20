# %%
def is_two(value):
    return value == 2 or value == '2'

# %%
def is_vowel(value):
  return len(value) == 1 and value.lower() in 'aeiou' # or ['a', 'e', 'i', 'o', 'u']

# %%
def is_consonant(value):
  return len(value) == 1 and value.lower() not in "aeiou" and value.isalpha() # or ['a', 'e', 'i', 'o', 'u'] 

# %%
def capitalize_starting_consonant(my_string):
    if len(my_string.split()) == 1:
        my_new_string = ''
        if is_consonant(my_string[0]):
            my_new_string += my_string[0].upper() 
            my_new_string += my_string[1:]
        else:
            my_new_string = my_string
    else:
        my_new_string = my_string
    return my_new_string

# %%
def calculate_tip(bill, tip_percent):
    tip_amount = bill * tip_percent
    return tip_amount

# %%

def apply_discount(price, discount):
    total_discount = price - (price * discount)
    return total_discount

# %%
def handled_commas(word):
    return int(word.replace(',', ''))

# %%
def get_letter_grade(grade):
    if grade in range(90, 101):
        return 'A'
    elif grade in range(80, 90):
        return 'B'
    elif grade in range(70, 80):
        return 'C'
    elif grade in range(60, 70):
        return 'D'
    else:
        return 'F'

# %%
def remove_vowels(word):
    return word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

# %%
def normalize_name(some_bad_identifier):
    my_new_string = ''
    for i in some_bad_identifier:
        if i.isalpha() or i.isdigit() or i == ' ':
            my_new_string += i
        else:
            continue
    return my_new_string.lower().strip().replace(' ','_')

# %%
def cumulative_sum(some_list):
    mynewlist, num_sum = [], 0
    for i in some_list:
        num_sum += i
        mynewlist.append(num_sum)
    return mynewlist


