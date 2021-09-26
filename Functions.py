import RequestsFunctions


def get_available_pets_count(status):
    """
    Find pets count by status
    :param status: string - status of pets (e.g. sold, pending, available)
    :return: int: the count of the pets by provided status
    """
    data = RequestsFunctions.get_pets_by_status(status)
    count = len(data)

    return count


def get_unique_pet_id():
    """
    Get non-existing pet id by status
    :return: int: unique id by status
    """
    unique_id = 0

    for i in range(1, 100000):
        if RequestsFunctions.get_pet_by_id(i) is None:
            unique_id = i
            break

    return unique_id
