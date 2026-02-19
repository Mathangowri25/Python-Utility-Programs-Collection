def get_students(batch1: set, batch2: set):
    return batch1 | batch2

def get_common_students(batch1: set, batch2: set):
    return batch1 & batch2

def exclusive_students(batch1: set, batch2: set):
    return batch1 - batch2