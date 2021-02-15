import re
# for i in "5363737","Bird1 !", "Bird1", "Bird1923812", "Bird":
for i in input("bla bla bla: "):

        mo = re.match(r'[A-Za-z]+[0-9]*$',i)

        if mo:
            print("allowed {}".format(mo.group(0)))
        else:
            print("not allowed {}".format(i))