def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    brackets=[]
    for i in brackets_row:
        if i=="(":
            brackets.append(i)
        if i==")":
            if len(brackets)==0:
                return False
            brackets.pop(-1)
    if len(brackets)!=0:
        return False
    return True
if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets("(((()())()))"))