TEST_CARD = "1234567890123452"


def is_real_card(pan: str):
    sum_ = 0
    for num in pan[0::2]:
        if int(num) * 2 > 9:
            sum_ += int(num) * 2 - 9
        else:
            sum_ += int(num) * 2
    for num_ in pan[1::2]:
        sum_ += int(num_)

    return bool(sum_ % 10 == 0)


print(is_real_card(TEST_CARD))


