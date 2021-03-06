class CreateItemError(Exception):
    """"创建 Item 失败时抛出的异常"""
    pass


def create_item(name):
    """创建一个新的 Item
    :raises: 当无法创建时抛出 CreateItemError
    """

    if len(name) > 3:
        print(len(name))
        raise CreateItemError('name of item is too long')

    if len(name) > 5:
        raise CreateItemError('items is full')
    return ['ok']


def create_for_input():


    try:
        rst = create_item('name')
        print(rst)
    except CreateItemError as e:
        print(f'create item failed: {err_msg}', e)

    else:
        print(f'item<{name}> created')
