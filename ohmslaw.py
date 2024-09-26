def ohm_law_calc():
    
    print("What do you want to calculate: Voltage, Current, Resistance")
    print("V for voltage, C for current, and R for Resistance")
    print("use caps for choices ")
    choices = input("Please enter a choice: V, I, or R: ").strip()

    if choices == "V":
        current = float(input("please enter a current: "))
        resistance = float(input("please enter a resistance: "))
        voltage = current * resistance
        print(f"the voltage is {voltage}")

    elif choices == "I":
        voltage = float(input("please enter a voltage: "))
        resistance = float(input("please enter a resistance: "))
        if resistance == 0:
            print("error, resistance can not be 0 ")
        else:
            current = voltage / resistance
            print("the current is {current} amperes")
    elif choices == "R":
        voltage = float(input("please enter a voltage: "))
        current = float(input("please enter a current: "))
        if current == 0:
            print("Error current can not be 0 ")
        else:
            resistance = voltage / current
            print(f"the resistance is {resistance}")
    else:
        print("invalid input please try again")

ohm_law_calc()        