from  sort.my_insert import insert_sort


def test_insert():
    assert insert_sort([54,26,93,17,77,31,44,55,20]) == sorted([54,26,93,17,77,31,44,55,20])

def test_false():
    case = insert_sort([26,93,17,77,31,44,55,20]) == sorted([54,26,93,17,77,31,44,55,20])
    assert case == False

def test_str():
    assert insert_sort(['g', 'u', 't', 'g', 's', 'q']) == sorted(['g', 'u', 't', 'g', 's', 'q'])

def test_str_nums():
    assert insert_sort(['g', 'u', 't', 5, 9]) == sorted(['g', 'u', 't', 5, 9])