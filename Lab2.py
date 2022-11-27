def display_main_menu():
    print("Display_main_menu")
    print("Enter some numbers separated by commas (eg. 5,67,32)")


def get_user_input():
    print("Enter the sequences of number")
    x = input()
    y = x.split(",")
    float_list = [float(number) for number in y]
    print(float_list)
    return float_list

def main():
    display_main_menu()
    list = get_user_input()
    calc_average_temperature(list)
    calc_min_max_temperature(list)
    calc_median_temperature(list)

def calc_average_temperature(input):
    count = 0
    total = 0
    for k in input:
        count += 1
    for k in input:
        total = total + k
    average = total / count
    print("The average is = " + str(average))

def calc_min_max_temperature(input):
    biggest = smallest = input[0]
    for k in input:
        if k > biggest:
            biggest = k
    for k in input:
        if k < smallest:
            smallest = k
    print("The biggest num is = " + str(biggest))
    print("The smallest num is = " + str(smallest))


def calc_median_temperature(input):
    n = len(input)
    input.sort()
    print(input)
    count = 0
    if n % 2 == 0 :
        median1 = input[n//2]
        median2 = input[n//2 - 1]
        median = (median1 + median2)/2
    else :
        median = input[n//2]
    print("The median is: " + str(median))





if __name__=="__main__":
    main()



