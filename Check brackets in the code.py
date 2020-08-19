open_list = ["[","{","("] 
close_list = ["]","}",")"]
n = input()
stack = []
for i in n: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
if len(stack) == 0: 
    print("Success")
else:
    print(n.index(i))
