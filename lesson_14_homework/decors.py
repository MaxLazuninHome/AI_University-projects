def decor(f):
    def inner(*args, **kwargs):
        print('-' * 45)
        res = f(*args, **kwargs)
        print('-' * 45)
        return res
    return inner