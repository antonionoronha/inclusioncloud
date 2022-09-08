def even(nums):

    print("Original list of integers:")
    print(nums)
    print("\nEven numbers from the list:")
    even_nums = list(filter(lambda x: x%2 == 0, nums))

    return even_nums

def main():

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(even(nums))

if __name__ == "__main__":
    main()