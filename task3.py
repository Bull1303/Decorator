from task2 import logger


@logger('task3.log')
def flat_generator(list_of_lists):
    for list_ in list_of_lists:
        for element in list_:
            yield element


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(list(flat_generator(list_of_lists_1)))


if __name__ == '__main__':
    test_2()
