def check_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if int(i) not in [0,1,2,3,4,5,6,7,8,9]:
                print(i, ":(")
            else:
                continue
        print(":)")
    else:
        print(":(")

pin = "1234"
check_pin(pin)

