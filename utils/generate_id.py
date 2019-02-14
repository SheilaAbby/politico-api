

def generate_id(collection):
    if len(collection) == 0:
        return 1

    else:
        return collection[-1]['id']+1  # add a 1 to the last value in the collection(-1)

