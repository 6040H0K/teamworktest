def recursive_sum (start:int,stop:int)->int:
    """Returns summ of digit range srom start to stop"""
    if stop == start:
        return start
    return stop+recursive_sum(start,stop-1)
