import unittest

class tshirt:
    def size(cms):
        if cms <= 38:
            return 'S'
        elif cms > 38 and cms < 42:
            return 'M'
        else:
            return 'L'
        
    assert(size(37) == 'S')
    assert(size(41) == 'M')
    assert(size(39) == 'M')
    assert(size(43) == 'L')
    assert(size(10) == 'S')
    assert(size(80) == 'L')
    assert(size(38) == 'S')
    print("All is well (maybe!)\n")
    
if __name__ == '__main__' :
    unittest.main()
