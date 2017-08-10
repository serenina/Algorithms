# this file creates the stack class and contains some function at the end to work with it
class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

# parChecker balances symbols
def parChecker(par):
    s = Stack()
    for i in range(0, len(par)):
        if par[i] == "(" or par[i] == "[" or par[i] == "{":
            s.push('(')
        elif s.is_empty() == False:
            s.pop()
        else:
            print ('Parentheses do not match')
            return

if s.is_empty() == True:
    print ('All the parentheses matched')
    else:
        print ('Parentheses do not match')


# devide_by_2 converts decimal numbers to binary
def devide_by_2(decimal):
    s = Stack()
    binary = ''
    temp = decimal
    while  decimal != 0:
        s.push(decimal % 2)
        decimal = decimal // 2
    while not s.is_empty():
        binary = binary + str(s.pop())
    print (str(temp) + ' in binary is: ' + binary)
    return binary





# parChecker('{{([][])}()}')
# parChecker('[{()]')


#devide_by_2(42)


