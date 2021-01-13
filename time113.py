import time

initial = time.time()

for i in range(20):
    print("hello wolrd")
    print("for loop ttime:", time.time() - initial, "Seconds")

    initial2 = time.time()
    j = 0
    while j < 20:
        print("hello wolrd")
        time.sleep(2)
        j = j + 1
        print("while loop time:", time.time() - initial2, "secoonds")


"""localtime=time.asctime(time.localtime(time.time()))
print(localtime)"""