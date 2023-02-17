import sys

memory = 0
msg = ""
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = list(range(0, 10))
msg_.append(msg_10)
msg_.append(msg_11)
msg_.append(msg_12)


def is_one_digit(v):
    v = float(v)
    if -10 < v < 10 and float(v).is_integer():
        output = True
        return output
    else:
        output = False
        return output


def operation(v1, v2, v3):
    if v3 == "+":
        return float(v1) + float(v2)
    if v3 == "-":
        return float(v1) - float(v2)
    if v3 == "*":
        return float(v1) * float(v2)
    if v3 == "/":
        try:
            return float(v1) / float(v2)
        except ZeroDivisionError:
            print("Yeah... division by zero. Smart move...")


def check(v1, v2, v3):
    global msg, msg_6, msg_7, msg_8, msg_9
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
    return msg


def saving_memory():
    global memory, msg_
    if is_one_digit(result):
        msg_index = 10
        while True:
            print(msg_[msg_index])
            answer_s = input()
            if answer_s == "y":
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    if answer_s == "y":
                        memory = result
                        break
            if answer_s == "n":
                break
            else:
                continue
    else:
        memory = result

while True:
    print("Enter an equation")
    x, oper, y = input().split()
    if x == "M":
        x = float(memory)
    if y == "M":
        y = float(memory)
    try:
        x, y == float(x), float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    msg = ""
    check(float(x), float(y), oper)
    result = operation(x, y, oper)
    print(result)
    print("Do you want to store the result? (y / n):")
    answer = input()
    if answer == "y":
        saving_memory()
    if answer == "n":
        pass
    print("Do you want to continue calculations? (y / n):")
    answer = input()
    if answer == "y":
        continue
    if answer == "n":
        sys.exit()
    else:
        continue

