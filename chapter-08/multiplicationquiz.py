import time, random

correctans = 0

for i in range(10):
    n1 = random.randint(0,9)
    n2 = random.randint(0,9)

    print(f"Q{i+1}: {n1}*{n2}: ")
    startTime = time.time()
    for j in range(3):
        ans = int(input(f"Try #{j+1}: "))
        if (time.time() - startTime) > 8:
            print("TimeOut")
            break
        if ans == n1*n2:
          correctans += 1
          print("Correct!")
          time.sleep(1)
          break

    print()  

print("Correct answers: %s"%(correctans))
    