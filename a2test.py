"""
Unit Test for Assignment A2

This module implements several test cases for a2.  It is incomplete.  You should look
though this file for places to add tests.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import introcs
import a2

def test_complement():
    """
    Test function complement
    """
    introcs.assert_equals(introcs.RGB(255-250, 255-0, 255-71),
                          a2.complement_rgb(introcs.RGB(250, 0, 71)))
    introcs.assert_equals(introcs.RGB(255-92, 255-128, 255-255),
                          a2.complement_rgb(introcs.RGB(92, 128, 255)))

    # Make sure we are not modifying the color
    rgb = introcs.RGB(128,128,128)
    introcs.assert_not_equals(id(rgb),id(a2.complement_rgb(rgb)))


def test_round():
    """
    Test function round (a2 version)
    """
    introcs.assert_equals(130.6,   a2.round(130.59,1))
    introcs.assert_equals(130.5,   a2.round(130.54,1))
    introcs.assert_equals(100.0,   a2.round(100,1))
    introcs.assert_equals(100.6,   a2.round(100.55,1))
    introcs.assert_equals(99.57,   a2.round(99.566,2))
    introcs.assert_equals(99.99,   a2.round(99.99,2))
    introcs.assert_equals(100.00,  a2.round(99.995,2))
    introcs.assert_equals(22.00,   a2.round(21.99575,2))
    introcs.assert_equals(21.99,   a2.round(21.994,2))
    introcs.assert_equals(10.01,   a2.round(10.013567,2))
    introcs.assert_equals(10.00,   a2.round(10.000000005,2))
    introcs.assert_equals(10.00,   a2.round(9.9999,3))
    introcs.assert_equals(9.999,   a2.round(9.9993,3))
    introcs.assert_equals(1.355,   a2.round(1.3546,3))
    introcs.assert_equals(1.354,   a2.round(1.3544,3))
    introcs.assert_equals(0.046,   a2.round(.0456,3))
    introcs.assert_equals(0.045,   a2.round(.0453,3))
    introcs.assert_equals(0.006,   a2.round(.0056,3))
    introcs.assert_equals(0.001,   a2.round(.0013,3))
    introcs.assert_equals(0.000,   a2.round(.0004,3))
    introcs.assert_equals(0.001,   a2.round(.0009999,3))


def test_str5():
    """
    Test function str5
    """
    introcs.assert_equals('130.6',  a2.str5(130.59))
    introcs.assert_equals('130.5',  a2.str5(130.54))
    introcs.assert_equals('100.0',  a2.str5(100))
    introcs.assert_equals('100.6',  a2.str5(100.55))
    introcs.assert_equals('99.57',  a2.str5(99.566))
    introcs.assert_equals('99.99',  a2.str5(99.99))
    introcs.assert_equals('100.0',  a2.str5(99.995))
    introcs.assert_equals('22.00',  a2.str5(21.99575))
    introcs.assert_equals('21.99',  a2.str5(21.994))
    introcs.assert_equals('10.01',  a2.str5(10.013567))
    introcs.assert_equals('10.00',  a2.str5(10.000000005))
    introcs.assert_equals('10.00',  a2.str5(9.9999))
    introcs.assert_equals('9.999',  a2.str5(9.9993))
    introcs.assert_equals('1.355',  a2.str5(1.3546))
    introcs.assert_equals('1.354',  a2.str5(1.3544))
    introcs.assert_equals('0.046',  a2.str5(.0456))
    introcs.assert_equals('0.045',  a2.str5(.0453))
    introcs.assert_equals('0.006',  a2.str5(.0056))
    introcs.assert_equals('0.001',  a2.str5(.0013))
    introcs.assert_equals('0.000',  a2.str5(.0004))
    introcs.assert_equals('0.001',  a2.str5(.0009999))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a2.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0)))

    # Tests for str5_hsv (add two)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a2.rgb_to_cmyk(rgb)
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    introcs.assert_equals('0.000', a2.str5(cmyk.black))

    rgb = introcs.RGB(0, 0, 0)
    cmyk = a2.rgb_to_cmyk(rgb)
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    introcs.assert_equals('100.0', a2.str5(cmyk.black))

    rgb = introcs.RGB(217, 43, 164)
    cmyk = a2.rgb_to_cmyk(rgb)
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    introcs.assert_equals('80.18', a2.str5(cmyk.magenta))
    introcs.assert_equals('24.42', a2.str5(cmyk.yellow))
    introcs.assert_equals('14.90', a2.str5(cmyk.black))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    pass # ADD TESTS TO ME


def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    pass # ADD TESTS TO ME


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    pass # ADD TESTS TO ME


def test_to_float_list():
    """
    Test conversion function to_float_list
    """
    seq = ['1.0', '2.2', '3.5']
    lst = a2.to_float_list(seq)
    introcs.assert_floats_equal(1.0, lst[0])
    introcs.assert_floats_equal(2.2, lst[1])
    introcs.assert_floats_equal(3.5, lst[2])

    seq = ['2.2', '3.5']
    lst = a2.to_float_list(seq)
    introcs.assert_floats_equal(2.2, lst[0])
    introcs.assert_floats_equal(3.5, lst[1])

    seq = ['1.0', '2.2', '3.5', '-7.5']
    lst = a2.to_float_list(seq)
    introcs.assert_floats_equal(1.0, lst[0])
    introcs.assert_floats_equal(2.2, lst[1])
    introcs.assert_floats_equal(3.5, lst[2])
    introcs.assert_floats_equal(-7.5, lst[3])


def test_file_to_data():
    """
    Test file function file_to_data
    """
    file = 'colorblind/normal.dat'
    data = a2.file_to_data(file)
    introcs.assert_equals('Normal',data[0])
    introcs.assert_float_lists_equal([1,0,0],data[1])
    introcs.assert_float_lists_equal([0,1,0],data[2])
    introcs.assert_float_lists_equal([0,0,1],data[3])

    file = 'colorblind/tritanomaly.dat'
    data = a2.file_to_data(file)
    introcs.assert_equals('Tritanomaly',data[0])
    introcs.assert_float_lists_equal([0.967, 0.033, 0],data[1])
    introcs.assert_float_lists_equal([0, 0.733, 0.267],data[2])
    introcs.assert_float_lists_equal([0, 0.183, 0.817],data[3])


def test_files_to_dictionary():
    """
    Test loading function files_to_dictionary
    """
    files = ['colorblind/normal.dat','colorblind/tritanomaly.dat']
    maps = a2.files_to_dictionary(files)

    introcs.assert_equals(2,len(maps))
    introcs.assert_true('Normal' in maps)
    introcs.assert_true('Tritanomaly' in maps)
    introcs.assert_float_lists_equal([1,0,0],maps['Normal'][0])
    introcs.assert_float_lists_equal([0,1,0],maps['Normal'][1])
    introcs.assert_float_lists_equal([0,0,1],maps['Normal'][2])
    introcs.assert_float_lists_equal([0.967, 0.033, 0],maps['Tritanomaly'][0])
    introcs.assert_float_lists_equal([0, 0.733, 0.267],maps['Tritanomaly'][1])
    introcs.assert_float_lists_equal([0, 0.183, 0.817],maps['Tritanomaly'][2])


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    # Execute the tests
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_to_float_list()
    test_file_to_data()
    test_files_to_dictionary()
    print('Module a2 is working correctly')
