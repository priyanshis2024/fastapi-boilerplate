import uuid


def generate_random_uuid():
    """
    Generate a random UUID.

    Returns:
        str: Random UUID as a string.
    """
    random_uuid = uuid.uuid4()
    return str(random_uuid)
