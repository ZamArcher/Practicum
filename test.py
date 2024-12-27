"""Оптимизируем решение."""


def decode_string(s):
    stack = []
    current_num = 0
    current_str = ''
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char.isalpha():
            current_str += char
        elif char == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ''
        elif char == ']':
            num, prev_str = stack.pop()
            current_str = prev_str + num * current_str
            
    return current_str


if __name__ == '__main__':
    # short_msg = '1[' + input() + ']'
    # print(decrypt_messages(short_msg)[0])

    test_1 = ''
    test_2 = '2[a]'
    test_3 = '3[a]2[bc]'
    test_4 = '2[abc]3[cd]ef'
    test_5 = '2[с]3[в]ш'
    test_6 = '3[a2[c]]'
    test_7 = '2[в3[ш]]с'

    print(decode_string(test_6))

    # assert decode_string(test_1) == ''
    # assert decode_string(test_2) == 'aa'
    # assert decode_string(test_3) == 'aaabcbc'
    # assert decode_string(test_4) == 'abcabccdcdcdef'
    # assert decode_string(test_5) == 'ссвввш'
    # assert decode_string(test_6) == 'accaccacc'
    # assert decode_string(test_7) == 'вшшшвшшшс'

    # assert decode_string(test_3) == 'aaabcbc'
