# import re
# xxx = input("whatever: ")
#
# for x in xxx:
#     mo = re.match(r'[A-Za-z]*$', x)
#
#     if mo:
#         print("allowed {}".format(mo.group(0)))
#     else:
#         print("not allowed {}".format(x))


def add_guest():

    print("Adding an wedding guest:\n")
    grab_data = input("Introduce {}: ".format(x))

    for x in grab_data:
        match_rule1 = re.match(r"[a-zA-Z\-\s]*$", x)
        match_rule2 = re.match(r"[yesnodauYESNODAU]]", grab_data)

        if re.match(r"[a-zA-Z\-\s]*$", grab_data):
            if x in ("First", "Last"):
                dic_guest[x] = grab_data
                continue
            elif x in ("Received","Confirmed") and (re.match(r"[yesnodauYESNODAU]]", grab_data)):
                dic_guest[x] = grab_data
                continue
            else:
                break