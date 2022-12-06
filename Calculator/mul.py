#this is for multiplicatin part
def div(*args):
    print("operation type = ", args[0])
    if(args[1] == 0):
        print("operation cant be performed")
    else:
       print(args[1]*args[2])
div("multiplication",6,3)