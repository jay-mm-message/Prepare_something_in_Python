
from datetime import datetime
from time import sleep
from random import randint

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55,
        57, 59 ]

for num in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print(right_this_minute)
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = randint(1, 3)
    print("There will be a few more repetitions left: ", 5 - num)
    print("Wait_time is ", wait_time)
    sleep(wait_time)