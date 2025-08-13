#program assignment one data structure the program is going to output an array sorted with 8 integers inputed by the user

def sorted_array(array, number):
    array.append(number)      # Adds the new number to the list
    array.sort()              # Sorts the list in ascending order
    return array              # Returns the updated, sorted list


def main():
    input_number = []  # Empty list to hold the numbers
    print("Enter 8 numbers (integers):")

    for a in range(8):  # Loop 8 times to collect input
        number = int(input(f"Enter number {a + 1}: "))
        input_number = sorted_array(input_number, number)  # Update and sort the list
        print("Sorted Array:", input_number)  # Show the sorted array after each input


if __name__ == "__main__":
    main()