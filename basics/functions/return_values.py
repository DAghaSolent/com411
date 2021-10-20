def sum_weights(beep, bop):
    total_weight = beep + bop
    return total_weight
def calc_avg_weight(beep, bop):
    sum_weights(beep, bop)
    avg_weight = sum_weights(beep, bop) / 2
    return avg_weight
def run():
    print("Please enter weight for Beep")
    beep = int(input())
    print("Please enter weight for Bop")
    bop = int(input())
    print("What would you like to calculate (Sum or Average)?")
    calculation = input().lower()
    if calculation == "sum":
        sum_weights(beep, bop)
        print(f"The sum of Beep and Bop weight is {sum_weights(beep, bop)}")
    elif calculation == "average":
        calc_avg_weight(beep, bop)
        print(f"The average weight of Beep and Bop is {calc_avg_weight(beep, bop)}")
    else:
        print("Please re run the program and type either (sum or average) to run the calculation program")
run()







