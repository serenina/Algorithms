from sort.my_merge2 import mergelists


def test_merge():
    assert mergelists([54,26,93,17,77,31,44,55,20]) == sorted([54,26,93,17,77,31,44,55,20])

def test_false():
    case = mergelists([26,93,17,77,31,44,55,20]) == sorted([54,26,93,17,77,31,44,55,20])
    assert case == False

def test_str():
    try:
        mergelists(['g', 'u', 't', 'g', 's', 'q']) == sorted(['g', 'u', 't', 'g', 's', 'q'])
    except:
        print("An error occurred")
def test_str_nums():
    try:
        mergelists(['g', 'u', 't', 5, 9]) == sorted(['g', 'u', 't', 5, 9])
    except:
        print("An error occurred")
