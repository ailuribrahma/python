def find_missing_numbers_set(num_list):
    if not num_list:
        return[]
    full_set = set(range(min(num_list), max(num_list) + 1))
    missing_numbers = sorted(list(full_set - set(num_list)))
    return missing_numbers
# Example usage
numbers = [1, 2, 4, 6, 7, 9]
missing = find_missing_numbers_set(numbers)
print("Missing numbers in the list are:", missing)  