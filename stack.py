class Stack:
    def __init__(self):
        self.list_ = []

    def __str__(self):
        return str(self.list_)

    def __getitem__(self, index):
        return self.list_[index]

    def isempty(self):
        if self.list_:
            return False
        else:
            return True

    def push(self, item):
        self.list_.append(item)

    def pop(self):
        return self.list_.pop()

    def peek(self):
        return self.list_[-1]

    def size(self):
        return len(self.list_)

    def ext(self, item):
        self.list_.extend(item)


def balanced(bracket_str):
    bracket_list = ['(', ')', '[', ']', '{', '}']

    check_list = Stack()
    open_br_list = Stack()

    check_list.ext(list(bracket_str))
    print(f'Наш изначальный список: {check_list}')

    for i in range(check_list.size()):
        if check_list[i] in ('(', '[', '{'):
            open_br_list.push(check_list[i])
        elif not open_br_list.isempty():
            if check_list[i] == bracket_list[1] and open_br_list.peek() == bracket_list[0]:
                open_br_list.pop()
                continue
            elif check_list[i] == bracket_list[3] and open_br_list.peek() == bracket_list[2]:
                open_br_list.pop()
                continue
            elif check_list[i] == bracket_list[5] and open_br_list.peek() == bracket_list[4]:
                open_br_list.pop()
            else:
                print('Не сбалансировано. Непарная закрывающая скобка.')
                return False
        else:
            print('Не сбалансировано. Непарная закрывающая скобка.')
            return False

    if open_br_list.isempty():
        print('Сбалансировано')
        return True
    else:
        print('Не сбалансировано. Непарная открывающая скобка.')
        return False


if __name__ == '__main__':
    balanced('(((([{}]))))')
    # assert balanced('(((([{}]))))')
    # assert balanced('[([])((([[[]]])))]{()}')
    # assert balanced('{{[()]}}')
    # assert not balanced('}{}')
    # assert not balanced('{{[(])]}}')
    # assert not balanced('[[{())}]')
