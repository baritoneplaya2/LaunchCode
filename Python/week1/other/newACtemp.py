#For each click variable, calculate the temperature and print it as shown in the instructions
basetemp = 40
reset = 50

click_1 = 0
click_2 = 49
click_3 = 74
click_4 = 51
click_5 = -1
click_6 = 200

clicks = [click_1, click_2, click_3, click_4, click_5, click_6]

for click in clicks:
    newtemp = click % reset + basetemp
    print("The temperature is", newtemp)
