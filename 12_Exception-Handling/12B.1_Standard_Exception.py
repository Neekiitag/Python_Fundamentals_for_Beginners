
try:
    raise MemoryError('memory error')                # memory error is a standard built-in exception
except MemoryError as e:
    print(e)

