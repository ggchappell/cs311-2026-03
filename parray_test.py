#!/usr/bin/env python3
# parray_test.py
# Glenn G. Chappell
# Started: 2026-10-23
# Updated: 2026-10-30
"""Test program for class PArray.
For CS 311 Fall 2026

For Assignment 5, Exercise A
Requires parray.py, allocator.py
"""

# Import for code to be tested
import parray     # For .PArray

# Import for testing framework
import unittest   # For .TestCase, .main

# Other imports for test suite


# **********************************************************************
# Test Cases
# **********************************************************************


# ***** Tests that pass in "HAND-OFF" version of parray.py *****


class Test00ReturnTypes(unittest.TestCase):
    """Test PArray method return types."""

    def test_00_len_return_type(self):
        p1 = parray.PArray([1,2,3])
        result = p1.__len__()

        self.assertIsInstance(result, int,
            "PArray.__len__ must return int")

    def test_01_bool_return_type(self):
        p1 = parray.PArray([1,2,3])
        result = p1.__bool__()

        self.assertIsInstance(result, bool,
            "PArray.__bool__ must return bool")

    def test_02_str_return_type(self):
        p1 = parray.PArray([1,2,3])
        result = p1.__str__()

        self.assertIsInstance(result, str,
            "PArray.__str__ must return str")

    def test_03_repr_return_type(self):
        p1 = parray.PArray([1,2,3])
        result = p1.__repr__()

        self.assertIsInstance(result, str,
            "PArray.__repr__ must return str")

    def test_04_index_return_type(self):
        p1 = parray.PArray([1,2,3])
        result = p1.index(2)

        self.assertIsInstance(result, int,
            "PArray.index must return int")


class Test01BracketOpRead(unittest.TestCase):
    "Test PArray bracket operator read (__getitem__)."""

    def test_00_read_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[0]

        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_01_read_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[1]

        self.assertIsInstance(result, float)
        self.assertEqual(result, 2.2)

    def test_02_read_c(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[2]

        self.assertIsInstance(result, str)
        self.assertEqual(result, "3")

    def test_03_neg_index_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[-1]

        self.assertIsInstance(result, str)
        self.assertEqual(result, "3")

    def test_04_neg_index_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[-2]

        self.assertIsInstance(result, float)
        self.assertEqual(result, 2.2)

    def test_05_neg_index_c(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        result = p1[-3]

        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_06_out_of_range_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises(IndexError):
            result = p1[3]

    def test_07_out_of_range_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises(IndexError):
            result = p1[100]

    def test_08_out_of_range_c(self):
        p1 = parray.PArray()
        self.assertEqual(len(p1), 0)
        with self.assertRaises(IndexError):
            result = p1[0]

    def test_09_out_of_range_neg_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises(IndexError):
            result = p1[-4]

    def test_10_out_of_range_neg_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises(IndexError):
            result = p1[-100]

    def test_11_out_of_range_neg_c(self):
        p1 = parray.PArray()
        self.assertEqual(len(p1), 0)
        with self.assertRaises(IndexError):
            result = p1[-1]

    def test_12_non_int_index_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises((TypeError, AssertionError)):
            result = p1[2.0]

    def test_13_non_int_index_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        with self.assertRaises((TypeError, AssertionError)):
            result = p1["x"]


class Test02BracketOpWrite(unittest.TestCase):
    "Test PArray bracket operator write (__setitem__) & read."""

    def test_00_write_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        p1[0] = True

        self.assertEqual(list(p1), [True,2.2,"3"])

    def test_01_write_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        p1[1] = (3,4)

        self.assertEqual(list(p1), [1,(3,4),"3"])

    def test_02_write_c(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        p1[2] = [6]

        self.assertEqual(list(p1), [1,2.2,[6]])

    def test_03_write_neg_index(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)
        p1[-2] = (3,)

        self.assertEqual(list(p1), [1,(3,),"3"])

    def test_04_write_out_of_range_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises(IndexError):
            p1[3] = True

    def test_05_write_out_of_range_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises(IndexError):
            p1[100] = True

    def test_06_write_out_of_range_neg_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises(IndexError):
            p1[-4] = True

    def test_07_write_out_of_range_neg_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises(IndexError):
            p1[-100] = True

    def test_08_write_non_int_index_a(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises((TypeError, AssertionError)):
            p1[1.0] = True

    def test_09_write_non_int_index_b(self):
        p1 = parray.PArray([1,2.2,"3"])
        self.assertEqual(len(p1), 3)

        with self.assertRaises((TypeError, AssertionError)):
            p1["abc"] = True


class Test03LenBool(unittest.TestCase):
    """Test PArray methods __len__, __bool__."""

    def test_00_len_bool_a(self):
        p1 = parray.PArray()

        self.assertIsInstance(p1.__len__(), int)
        self.assertEqual(p1.__len__(), 0)
        self.assertIsInstance(p1.__bool__(), bool)
        self.assertEqual(p1.__bool__(), False)

    def test_01_len_bool_b(self):
        p1 = parray.PArray([])

        self.assertIsInstance(p1.__len__(), int)
        self.assertEqual(p1.__len__(), 0)
        self.assertIsInstance(p1.__bool__(), bool)
        self.assertEqual(p1.__bool__(), False)

    def test_02_len_bool_c(self):
        p1 = parray.PArray([1])

        self.assertIsInstance(p1.__len__(), int)
        self.assertEqual(p1.__len__(), 1)
        self.assertIsInstance(p1.__bool__(), bool)
        self.assertEqual(p1.__bool__(), True)

    def test_03_len_bool_d(self):
        bignum = 10_000
        p1 = parray.PArray(range(10_000))

        self.assertIsInstance(p1.__len__(), int)
        self.assertEqual(p1.__len__(), bignum)
        self.assertIsInstance(p1.__bool__(), bool)
        self.assertEqual(p1.__bool__(), True)


class Test04Str(unittest.TestCase):
    """Test PArray method __str__."""

    def test_00_str_a(self):
        p1 = parray.PArray()

        self.assertIsInstance(p1.__str__(), str)
        self.assertEqual(p1.__str__(), "[]")

    def test_01_str_b(self):
        p1 = parray.PArray(["a"])

        self.assertIsInstance(p1.__str__(), str)
        self.assertEqual(p1.__str__(), "['a']")

    def test_02_str_c(self):
        p1 = parray.PArray(["a","b",3])

        self.assertIsInstance(p1.__str__(), str)
        self.assertEqual(p1.__str__(), "['a', 'b', 3]")

    def test_03_str_d(self):
        bignum = 10_000
        p1 = parray.PArray(["a"]*bignum)

        self.assertIsInstance(p1.__str__(), str)
        self.assertEqual(p1.__str__(),
                         "[" + "'a', " * (bignum-1) + "'a']")


class Test05Repr(unittest.TestCase):
    """Test PArray method __repr__."""

    def test_00_repr_a(self):
        p1 = parray.PArray()

        self.assertIsInstance(p1.__repr__(), str)
        self.assertEqual(p1.__repr__(), "PArray([])")

    def test_01_repr_b(self):
        p1 = parray.PArray(["a"])

        self.assertIsInstance(p1.__repr__(), str)
        self.assertEqual(p1.__repr__(), "PArray(['a'])")

    def test_02_repr_c(self):
        p1 = parray.PArray(["a","b",3])

        self.assertIsInstance(p1.__repr__(), str)
        self.assertEqual(p1.__repr__(), "PArray(['a', 'b', 3])")

    def test_03_repr_d(self):
        bignum = 10_000
        p1 = parray.PArray(["a"]*bignum)

        self.assertIsInstance(p1.__repr__(), str)
        self.assertEqual(p1.__repr__(),
                         "PArray([" + "'a', " * (bignum-1) + "'a'])")


class Test06Sort(unittest.TestCase):
    """Test PArray method sort."""

    def test_00_sort_empty_a(self):
        p1 = parray.PArray()
        p1.sort()

        self.assertEqual(list(p1), [])

    def test_01_sort_empty_b(self):
        p1 = parray.PArray()
        p1.sort(reverse=False)

        self.assertEqual(list(p1), [])

    def test_02_sort_empty_c(self):
        p1 = parray.PArray()
        p1.sort(reverse=True)

        self.assertEqual(list(p1), [])

    def test_03_sort_empty_d(self):
        p1 = parray.PArray()
        p1.sort(key=str)

        self.assertEqual(list(p1), [])

    def test_04_sort_empty_e(self):
        p1 = parray.PArray()
        p1.sort(reverse=False, key=str)

        self.assertEqual(list(p1), [])

    def test_05_sort_empty_f(self):
        p1 = parray.PArray()
        p1.sort(reverse=True, key=str)

        self.assertEqual(list(p1), [])

    def test_06_sort_len_1_a(self):
        p1 = parray.PArray([12])
        p1.sort()

        self.assertEqual(list(p1), [12])

    def test_07_sort_len_1_b(self):
        p1 = parray.PArray([12])
        p1.sort(reverse=False)

        self.assertEqual(list(p1), [12])

    def test_08_sort_len_1_c(self):
        p1 = parray.PArray([12])
        p1.sort(reverse=True)

        self.assertEqual(list(p1), [12])

    def test_09_sort_len_1_d(self):
        p1 = parray.PArray([12])
        p1.sort(key=str)

        self.assertEqual(list(p1), [12])

    def test_10_sort_len_1_e(self):
        p1 = parray.PArray([12])
        p1.sort(reverse=False, key=str)

        self.assertEqual(list(p1), [12])

    def test_11_sort_len_1_f(self):
        p1 = parray.PArray([12])
        p1.sort(reverse=True, key=str)

        self.assertEqual(list(p1), [12])

    def test_12_sort_len_2_a(self):
        p1 = parray.PArray([12,100])
        p1.sort()

        self.assertEqual(list(p1), [12, 100])

    def test_13_sort_len_2_b(self):
        p1 = parray.PArray([12,100])
        p1.sort(reverse=False)

        self.assertEqual(list(p1), [12, 100])

    def test_14_sort_len_2_c(self):
        p1 = parray.PArray([12,100])
        p1.sort(reverse=True)

        self.assertEqual(list(p1), [100, 12])

    def test_15_sort_len_2_d(self):
        p1 = parray.PArray([12,100])
        p1.sort(key=str)

        self.assertEqual(list(p1), [100, 12])

    def test_16_sort_len_2_e(self):
        p1 = parray.PArray([12,100])
        p1.sort(reverse=False, key=str)

        self.assertEqual(list(p1), [100, 12])

    def test_17_sort_len_2_f(self):
        p1 = parray.PArray([12,100])
        p1.sort(reverse=True, key=str)

        self.assertEqual(list(p1), [12, 100])

    def test_18_sort_len_5_a(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort()

        self.assertEqual(list(p1), [1, 12, 21, 100, 200])

    def test_19_sort_len_5_b(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort(reverse=False)

        self.assertEqual(list(p1), [1, 12, 21, 100, 200])

    def test_20_sort_len_5_c(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort(reverse=True)

        self.assertEqual(list(p1), [200, 100, 21, 12, 1])

    def test_21_sort_len_5_d(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort(key=str)

        self.assertEqual(list(p1), [1, 100, 12, 200, 21])

    def test_22_sort_len_5_e(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort(reverse=False, key=str)

        self.assertEqual(list(p1), [1, 100, 12, 200, 21])

    def test_23_sort_len_5_f(self):
        p1 = parray.PArray([100, 21,  1, 200, 12])
        p1.sort(reverse=True, key=str)

        self.assertEqual(list(p1), [21, 200, 12, 100, 1])


class Test07Index(unittest.TestCase):
    """Test PArray method index."""

    def test_00_empty(self):
        p1 = parray.PArray()
        with self.assertRaises(ValueError):
            result = p1.index(1)

    def test_01_len_1_present(self):
        p1 = parray.PArray([2])
        result = p1.index(2)

        self.assertEqual(result, 0)

    def test_02_len_1_not_present(self):
        p1 = parray.PArray([2])
        with self.assertRaises(ValueError):
            result = p1.index(1)

    def test_03_len_100_present(self):
        p1 = parray.PArray(range(1,201,2))
        result = p1.index(83)

        self.assertEqual(result, 41)

    def test_04_len_100_not_present(self):
        p1 = parray.PArray(range(1,201,2))
        with self.assertRaises(ValueError):
            result = p1.index(84)


# ***** Tests that do not pass in "HAND-OFF" version of parray.py *****


class Test08Add(unittest.TestCase):
    """Test PArray binary + operator (method __add__)."""

    def test_00_add_short(self):
        it1 = range(1,4)
        it2 = range(5)
        p1 = parray.PArray(it1)
        p2 = p1 + it2

        self.assertEqual(list(p1), list(it1))
        self.assertEqual(list(p2), list(it1) + list(it2))

    def test_01_add_long(self):
        bignum = 10_000
        it1 = range(bignum)
        it2 = range(3,2*bignum,2)
        p1 = parray.PArray(it1)
        p2 = p1 + it2

        self.assertEqual(list(p1), list(it1))
        self.assertEqual(list(p2), list(it1) + list(it2))

    def test_02_add_1st_empty(self):
        it1 = []
        it2 = range(7)
        p1 = parray.PArray(it1)
        p2 = p1 + it2

        self.assertEqual(list(p1), list(it1))
        self.assertEqual(list(p2), list(it1) + list(it2))

    def test_03_add_2nd_empty(self):
        it1 = range(3,6)
        it2 = []
        p1 = parray.PArray(it1)
        p2 = p1 + it2

        self.assertEqual(list(p1), list(it1))
        self.assertEqual(list(p2), list(it1) + list(it2))

    def test_04_add_both_empty(self):
        it1 = []
        it2 = []
        p1 = parray.PArray(it1)
        p2 = p1 + it2

        self.assertEqual(list(p1), list(it1))
        self.assertEqual(list(p2), list(it1) + list(it2))


class Test09IAdd(unittest.TestCase):
    """Test PArray += operator (method __iadd__)."""

    def test_00_iadd_short(self):
        it1 = range(1,4)
        it2 = range(5)
        p1 = parray.PArray(it1)
        p1 += it2

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_01_iadd_long(self):
        bignum = 10_000
        it1 = range(bignum)
        it2 = range(3,2*bignum,2)
        p1 = parray.PArray(it1)
        p1 += it2

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_02_iadd_1st_empty(self):
        it1 = []
        it2 = range(7)
        p1 = parray.PArray(it1)
        p1 += it2

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_03_iadd_2nd_empty(self):
        it1 = range(3,6)
        it2 = []
        p1 = parray.PArray(it1)
        p1 += it2

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_04_iadd_both_empty(self):
        it1 = []
        it2 = []
        p1 = parray.PArray(it1)
        p1 += it2

        self.assertEqual(list(p1), list(it1) + list(it2))


class Test10Copy(unittest.TestCase):
    """Test PArray method copy."""

    def test_00_copy_short(self):
        p1 = parray.PArray([1,2,3])
        p2 = p1.copy()

        self.assertEqual(list(p1), [1,2,3])
        self.assertEqual(list(p2), [1,2,3])

        p1[0] = 11
        p2[1] = 22

        self.assertEqual(list(p1), [11,2,3])
        self.assertEqual(list(p2), [1,22,3])

    def test_01_copy_long(self):
        bignum = 10_000
        p1 = parray.PArray(range(bignum))
        p2 = p1.copy()

        self.assertEqual(list(p1), list(range(bignum)))
        self.assertEqual(list(p2), list(range(bignum)))

        p1[0] = 11
        p2[1] = 22

        self.assertEqual(list(p1), [11] + list(range(1,bignum)))
        self.assertEqual(list(p2), [0,22] + list(range(2, bignum)))


class Test11Resize(unittest.TestCase):
    """Test PArray method resize."""

    def test_00_resize_simple_smaller(self):
        p1 = parray.PArray(range(100))
        p1.resize(50)

        self.assertEqual(len(p1), 50)
        self.assertEqual(list(p1), list(range(50)))

    def test_01_resize_simple_larger(self):
        p1 = parray.PArray(range(100))
        p1.resize(2000)

        self.assertEqual(len(p1), 2000)
        self.assertEqual(list(p1)[:100], list(range(100)))

    def test_02_resize_simple_same(self):
        p1 = parray.PArray(range(100))
        p1.resize(100)

        self.assertEqual(len(p1), 100)
        self.assertEqual(list(p1), list(range(100)))

    def test_03_resize_alloc(self):
        bignum = 10_000
        global last_alloc
        last_alloc = None
        p1 = parray.PArray(alloc=Alloc2)
        self.assertIsInstance(last_alloc, int)

        last_alloc = None
        p1.resize(bignum)
        cap1 = last_alloc

        self.assertEqual(len(p1), bignum)
        self.assertIsInstance(cap1, int)
        self.assertTrue(bignum <= cap1 <= bignum*5)

        last_alloc = None
        p1.resize(1)
        self.assertIs(last_alloc, None)

        last_alloc = None
        p1.resize(cap1-2)
        self.assertIs(last_alloc, None)

        last_alloc = None
        p1.resize(cap1-1)
        self.assertIs(last_alloc, None)

        last_alloc = None
        p1.resize(cap1)
        self.assertIs(last_alloc, None)

        last_alloc = None
        p1.resize(cap1+1)
        cap2 = last_alloc

        self.assertIsInstance(cap2, int)
        self.assertTrue(cap2 > cap1 and cap2 >= cap1*2)

        last_alloc = None
        p1.resize(cap2-1)
        self.assertIs(last_alloc, None)


class Test12Insert(unittest.TestCase):
    """Test PArray method insert."""

    def test_00_insert_empty(self):
        p1 = parray.PArray()
        p1.insert(0, 9)

        self.assertEqual(len(p1), 1)
        self.assertEqual(list(p1), [9])

    def test_01_insert_a(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(0, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [9,1,2,3,4])

    def test_02_insert_b(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(1, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,9,2,3,4])

    def test_03_insert_c(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(2, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,2,9,3,4])

    def test_04_insert_d(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(3, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,2,3,9,4])

    def test_05_insert_e(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(4, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,2,3,4,9])

    def test_06_insert_neg_index(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(-2, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,2,9,3,4])

    def test_07_insert_lo_index(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(-100, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [9,1,2,3,4])

    def test_08_insert_hi_index(self):
        p1 = parray.PArray([1,2,3,4])
        p1.insert(100, 9)

        self.assertEqual(len(p1), 5)
        self.assertEqual(list(p1), [1,2,3,4,9])

    def test_09_insert_alloc(self):
        global last_alloc
        last_alloc = None
        p1 = parray.PArray([1,2], alloc=Alloc2)
        cap1 = last_alloc
        self.assertIsInstance(cap1, int)

        for i in range(3, 1+cap1):
            last_alloc = None
            p1.insert(0, 9)
            self.assertIs(last_alloc, None)

        last_alloc = None
        p1.insert(0, 9)
        cap2 = last_alloc
        self.assertIsInstance(cap2, int)
        self.assertTrue(cap2 > cap1 and cap2 >= cap1 * 2)


class Test13Del(unittest.TestCase):
    """Test del on PArray item (method __delitem__)."""

    def test_00_del_short_a(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        del p1[0]
        self.assertIs(last_alloc, None)

        self.assertEqual(list(p1), [2,3])

    def test_01_del_short_b(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        del p1[1]
        self.assertIs(last_alloc, None)

        self.assertEqual(list(p1), [1,3])

    def test_02_del_short_c(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        del p1[2]
        self.assertIs(last_alloc, None)

        self.assertEqual(list(p1), [1,2])

    def test_03_del_short_negative(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        del p1[-2]
        self.assertIs(last_alloc, None)

        self.assertEqual(list(p1), [1,3])

    def test_04_del_long_a(self):
        global last_alloc
        bignum = 10_000
        p1 = parray.PArray(range(0,bignum), alloc=Alloc2)
        last_alloc = None
        del p1[bignum//2]
        self.assertIs(last_alloc, None)

        self.assertEqual(list(p1),
            list(range(0,bignum//2)) + list(range(bignum//2+1,bignum)))

    def test_05_del_out_of_range_a(self):
        p1 = parray.PArray()
        with self.assertRaises(IndexError):
            del p1[0]

    def test_06_del_out_of_range_b(self):
        p1 = parray.PArray([1,2,3])
        with self.assertRaises(IndexError):
            del p1[3]

    def test_07_del_out_of_range_c(self):
        p1 = parray.PArray([1,2,3])
        with self.assertRaises(IndexError):
            del p1[-4]


class Test14Pop(unittest.TestCase):
    """Test PArray method pop."""

    def test_00_pop_no_arg(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        popped = p1.pop()
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, 3)
        self.assertEqual(list(p1), [1,2])

    def test_01_pop_short_a(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        popped = p1.pop(0)
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, 1)
        self.assertEqual(list(p1), [2,3])

    def test_02_pop_short_b(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        popped = p1.pop(1)
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, 2)
        self.assertEqual(list(p1), [1,3])

    def test_03_pop_short_c(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        popped = p1.pop(2)
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, 3)
        self.assertEqual(list(p1), [1,2])

    def test_04_pop_short_negative(self):
        global last_alloc
        p1 = parray.PArray([1,2,3], alloc=Alloc2)
        last_alloc = None
        popped = p1.pop(-2)
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, 2)
        self.assertEqual(list(p1), [1,3])

    def test_05_pop_long_a(self):
        global last_alloc
        bignum = 10_000
        p1 = parray.PArray(range(0,bignum), alloc=Alloc2)
        last_alloc = None
        popped = p1.pop(bignum//2)
        self.assertIs(last_alloc, None)

        self.assertEqual(popped, bignum//2)
        self.assertEqual(list(p1),
            list(range(0,bignum//2)) + list(range(bignum//2+1,bignum)))

    def test_06_pop_out_of_range_a(self):
        p1 = parray.PArray()
        with self.assertRaises(IndexError):
            _ = p1.pop(0)

    def test_07_pop_out_of_range_b(self):
        p1 = parray.PArray([1,2,3])
        with self.assertRaises(IndexError):
            _ = p1.pop(3)

    def test_08_pop_out_of_range_c(self):
        p1 = parray.PArray([1,2,3])
        with self.assertRaises(IndexError):
            _ = p1.pop(-4)


class Test15Append(unittest.TestCase):
    """Test PArray method append."""

    def test_00_append_a(self):
        p1 = parray.PArray()
        p1.append(7)

        self.assertEqual(len(p1), 1)
        self.assertEqual(list(p1), [7])

    def test_01_append_b(self):
        p1 = parray.PArray([1,2,3])
        p1.append(8)

        self.assertEqual(len(p1), 4)
        self.assertEqual(list(p1), [1,2,3,8])


class Test16Extend(unittest.TestCase):
    """Test PArray method extend."""

    def test_00_extend_short(self):
        it1 = range(1,4)
        it2 = range(5)
        p1 = parray.PArray(it1)
        p1.extend(it2)

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_01_extend_long(self):
        bignum = 10_000
        it1 = range(bignum)
        it2 = range(3,2*bignum,2)
        p1 = parray.PArray(it1)
        p1.extend(it2)

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_02_extend_1st_empty(self):
        it1 = []
        it2 = range(7)
        p1 = parray.PArray(it1)
        p1.extend(it2)

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_03_extend_2nd_empty(self):
        it1 = range(3,6)
        it2 = []
        p1 = parray.PArray(it1)
        p1.extend(it2)

        self.assertEqual(list(p1), list(it1) + list(it2))

    def test_04_extend_both_empty(self):
        it1 = []
        it2 = []
        p1 = parray.PArray(it1)
        p1.extend(it2)

        self.assertEqual(list(p1), list(it1) + list(it2))


# **********************************************************************
# Helper Code
# **********************************************************************


last_alloc = None  # Size for last call to Alloc2


class Alloc2:
    """Allocator class; saves size in global last_alloc."""

    def __init__(self, size):
        """Allocate list of specified size."""

        assert isinstance(size, int)
        assert size >= 0

        global last_alloc
        last_alloc = size
        self._data = [ None for _ in range(size) ]

    def __getitem__(self, ix):
        """Return item in array with given index.
        Return None on out-of-range index.
        """

        assert isinstance(ix, int)

        try:
            return self._data[ix]
        except:
            return None  # Fail silently

    def __setitem__(self, ix, val):
        """Set item in array with given index to given value.
        Does nothing on out-of-range index.
        """

        assert isinstance(ix, int)

        try:
            self._data[ix] = val
        except:
            pass         # Fail silently


# **********************************************************************
# Main Program
# **********************************************************************


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program

if __name__ == '__main__':
    # Printable name for this test suite
    test_suite_name = "Class PArray - CS 311 Assn 5, Ex A"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

