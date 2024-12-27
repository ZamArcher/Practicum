"""Оптимизируем решение."""


def decrypt_messages(
    short_msg: str,
    temp_num: int = 1,
    temp_msg: str = '',
) -> str:
    """Функция расшифровки коротких сообщений."""
    if not short_msg:
        return temp_msg

    token = short_msg[0]
    if token.isdigit():
        open_brace = short_msg.index('[')
        close_brace = short_msg.index(']')

        return temp_num * (
            temp_msg
            + decrypt_messages(
                short_msg[open_brace + 1 :], int(short_msg[:open_brace])
            )
        ) + decrypt_messages(short_msg[close_brace + 1 :])

    elif token == ']':
        # return temp_num * temp_msg + decrypt_messages(short_msg[1:])
        return temp_num * temp_msg
    else:
        temp_msg += token
        return decrypt_messages(short_msg[1:], temp_num, temp_msg)


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

    print(decrypt_messages(test_7))

    assert decrypt_messages(test_1) == ''
    assert decrypt_messages(test_2) == 'aa'
    assert decrypt_messages(test_3) == 'aaabcbc'
    assert decrypt_messages(test_4) == 'abcabccdcdcdef'
    assert decrypt_messages(test_5) == 'ссвввш'
    assert decrypt_messages(test_6) == 'accaccacc'
    # assert decrypt_messages(test_7) == 'вшшшвшшшс'
