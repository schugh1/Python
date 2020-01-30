def semiperimeter(side1, side2, side3):
    ''' (number, number, nummber) -> float

    Return the semiperimeter of a triangle with
    sides of length side1, side2, side3.
    
    >>>semiperimter(3, 4, 5)
    6.0
    >>>semiperimeter(10.5, 6, 9.3)
    12.9
    '''

    return perimeter(side1, side2, side3) / 2
