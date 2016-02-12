'''
Example tests to show that bin/test works.
'''

def test_evens():
    cases = [(1, False),
             (2, True),
             (3, False),
             (4, True)]

    for value, is_even in cases:
        yield lambda x: x%2==0, value

