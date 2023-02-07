def calulate(expression):
    # stwórz listę stworzoną z elementów wyrażenia
    temp_list = []
    stack = deque()
    for el in expression:
        if el.isdigit():
            temp_list.append(int(el))
        else:
            temp_list.append(el)
    # obsłuda mnożenia i dzielenia
    #return temp_list
    for i in range(len(temp_list)):
        multiplication = "*"
        if temp_list[i] == multiplication:
            x = temp_list[i - 1] * temp_list[i + 1]
            temp_list[i - 1] = None
            temp_list[i + 1] = None
            temp_list[i] = x
    for el in temp_list:
        if el == None:
            temp_list.remove(el)
    for i in range(len(temp_list)):
        division = "/"
        if temp_list[i] == division:
            x = temp_list[i -1] / temp_list[i+1]
            temp_list[i - 1] = None
            temp_list[i + 1] = None
            temp_list[i] = x

    # dodaj do stosu wszystkie elementy z tablicy tymczasowej
    for el in temp_list:
        if el != None:
            stack.append(el)
    # obsługa dodawania i odejmowania
    result = 0
    znak = '+'
    for el in stack:
        if type(el) == int or type(el) == float:
            if znak == '+':
                result += el
            elif znak == '-':
                result -= el
        else:
            znak = el
    print(result)
    print(stack)