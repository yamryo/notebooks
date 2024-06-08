#!/usr/bin/env python
# coding: utf-8

# # Importing modules

import sys; sys.path.append("../modules")
from nanoword import *

import unittest
from unittest.mock import patch  # For mocking and patching

from random import Random

# # Unit tests

random = Random()
MYWORD = "ABCDAECBFDFE"
MYALPH = [Letter("A",'b+'), Letter("B", 'b-'), Letter("C", 'a+'), Letter("D", 'a-'), Letter("E", 'b+'), Letter("F", 'a-')]
MYNW = Nanoword(MYWORD, MYALPH)


# ### Basics of nanowords

# In[ ]:


class TestBasics(unittest.TestCase):
    def setUp(self):
        self.alph = [Letter("A",'b+'), Letter("B", 'b-'), Letter("C", 'a+'), Letter("D", 'a-'), Letter("E", 'b+'), Letter("F", 'a-')]
    def tearDown(self):
        del self.alph
        
#----------------------
    def test_initialize__not_gauss(self):
        with self.assertRaises(ValueError):
            Nanoword('ABC', self.alph[:3])

    def test_initialize__invalid_alphabet(self):
        with self.assertRaises(ValueError):
            Nanoword('ABCBAC', self.alph[:4])

#----------------------
    def test_equal(self):
        alph = self.alph[:3]
        w1, w2 = Nanoword('ABCCBA', alph), Nanoword('ABCCBA', alph)
        self.assertEqual(w1, w2)
        
    def test_equal_w_dif_words(self):
        alph = self.alph[:3]
        w1, w2 = Nanoword('ABCCBA', alph), Nanoword('AACBCB', alph)
        self.assertNotEqual(w1, w2)


# ### Reidemeister moves

class TestReidemeisterMoves(unittest.TestCase):
    def setUp(self):
        self.nw = Nanoword.random_generator(6)
        self.ls = [Letter("X", 'a+'), Letter("Y", 'b-'), Letter("Z", 'b+')]
        # #---
        # global random
        # random = Random(666)
    def tearDown(self):
        del self.nw
        del self.ls
        
#--- Reidemeister I ---
# #    @patch("random.randint")
#     def test_rmi_inv(self):
# #        mock_randint.return_value = 1
#         expected = "AGGBCDAECBFDFE" 
#         actual = self.nw.rmi_inv().word
#         self.assertEqual(expected, actual)
        
    def test_rmi_inv__w_char_and_index(self):
        expected = self.nw.word[:4]+"XX"+self.nw.word[4:]
        actual = R.I(self.nw, reverse=True, letter=self.ls[0], index=4).word
        self.assertEqual(expected, actual)
        
    def test_rmi__w_letter(self):
        mnw = R.I(self.nw, reverse=True)
        expected = self.nw
        actual = R.I(mnw, char='G')
        self.assertEqual(expected, actual)

    def test_rmi__w_letter_o_None_01(self):
        actual = R.I(self.nw, char="A")
        if not 'AA' in self.nw.word:
            self.assertIsNone(actual)
        else:
            expected = self.nw.word.replace('AA', '')
            self.assertEqual(expected, actual.word)

    def test_rmi__w_letter_o_None_02(self):
        self.assertIsNone(R.I(self.nw, char="G"))

#--- Reidemeister II ---
# #    @patch("random.randint")
#     def test_rmii_inv(self):
# #        mock_randint.return_value = [1, 5]
#         expected = "AGHBCDAHGECBFDFE" 
#         actual = self.nw.rmii_inv().word
#         self.assertEqual(expected, actual)
        
    def test_rmii_inv__w_letters_and_indices(self):
        expected = "XY" + self.nw.word[:4]+"YX"+self.nw.word[4:]
        actual = R.II(self.nw, reverse=True, letters=self.ls[:2], indices=[0,4]).word
        self.assertEqual(expected, actual)
        
    def test_rmii(self):
        mnw = Nanoword(MYWORD, MYALPH)
        expected = MYWORD.replace('BC', '').replace('CB', '')
        actual = R.II(mnw)
        self.assertEqual(expected, actual.word)

    def text_rmii__o_None(self):
        mnw = Nanoword("ABDCAECBFDFE", self.nw.alphabet)
        self.assertIsNone(R.II(mnw))

    def test_rmii__w_chars(self):
        expected = self.nw.word.replace('BC','').replace('CB','')
        actual = R.II(self.nw, chars=['B','C'])
        if len(self.nw.word) - len(expected) == 4:
            self.assertEqual(expected, actual.word)
        else:
            self.assertIsNone(actual)

    def test_rmii__w_chars_o_None(self):
        actual = R.II(self.nw, chars=['A','B'])
        self.assertIsNone(actual)

#     def test_rmi__w_letter_and_index(self):
#         expected = None
#         actual = self.nw.rmi(char="A", index=2)
#         self.assertEqual(expected, actual)

#--- Reidemeister III ---
    def test_rmiii(self):
        mnw = Nanoword("EBCEABADCD",
                       [Letter('A','b-'), Letter('B','b-'), Letter('C','a-'), Letter('D','b+'), Letter('E','b+')])
        expected = mnw.word.replace('EB', 'BE').replace('EA', 'AE').replace('BA', 'AB')
        actual = R.III(mnw).word
        self.assertEqual(expected, actual)


# ### self_linking

class Test_self_linking(unittest.TestCase):
    def setUp(self):
        self.nw = MYNW
    def tearDown(self):
        del self.nw
        
    def test_self_linking(self):
        ltrA = MYALPH[0]
        expected = {'a': 0, 'b': -1}
        actual = self.nw.self_linking(ltrA)
        self.assertEqual(expected, actual)        


# ### section

class Test_section(unittest.TestCase):
    def setUp(self):
        self.nw = MYNW
    def tearDown(self):
        del self.nw
        
    def test_section_a_posi(self):
        mysign = Sign('a+')
        expected = [{'a': 1, 'b': 0}]
        actual = self.nw.section(mysign)
        self.assertEqual(expected, actual)
        
    def test_section_b_nega(self):
        mysign = Sign('b-')
        expected = [{'a': 1, 'b': 0}]
        actual = self.nw.section(mysign)
        self.assertEqual(expected, actual)        
        
    def test_section_b_posi(self):
        mysign = Sign('b+')
        expected = [{'a': 0, 'b': -1},{'a': 0, 'b': 1}]
        actual = self.nw.section(mysign)
        self.assertEqual(expected, actual)        
        
    def test_section_a_nega(self):
        mysign = Sign('a-')
        expected = [{'a': 0, 'b': -1},{'a': 0, 'b': 1}]
        actual = self.nw.section(mysign)
        self.assertEqual(expected, actual)


# ### self linking function

class Test_self_linking_function(unittest.TestCase):
    def setUp(self):
        self.nw = MYNW
    def tearDown(self):
        del self.nw

    def test_self_linking_function__a(self):
        expected = {'var': 'a', 'd&c': []}
        actual = self.nw.self_linking_function('a')
        self.assertEqual(expected, actual)
        
    def test_self_linking_function__b(self):
        expected = {'var': 'b', 'd&c': []}
        actual = self.nw.self_linking_function('b')
        self.assertEqual(expected, actual)
        
    def test_sl_polynomial__a(self):
        expected = ''
        actual = self.nw.sl_polynomial('b')
        self.assertEqual(expected, actual)        
        
    def test_sl_polynomial__b(self):
        expected = ''
        actual = self.nw.sl_polynomial('b')
        self.assertEqual(expected, actual)
        
    def test_ab_polynomial(self):
        expected = ['','']
        actual = self.nw.ab_polynomials()
        self.assertEqual(expected, actual)        


# ### writhe polynomial

class Test_writhe_polynomial(unittest.TestCase):
    def setUp(self):
        self.nw = Nanoword("ABCDACEEBD", [Letter('A','a+'),Letter('B','b-'),Letter('C','b-'),Letter('D','b-'),Letter('E','b+')])
    def tearDown(self):
        del self.nw
        
    def test_ind(self):
        inds = [3,2,2,-1,0]
        for i, ltr in enumerate(self.nw.alphabet):
            with self.subTest(ltr = ltr):
                expected = inds[i]
                actual = self.nw.ind(ltr)
                self.assertEqual(expected, actual)
                
    def test_writhe_polynomial(self):
        expected = "(1)t^3+(-2)t^2+(2)+(-1)t^-1"
        actual = self.nw.writhe_polynomial()
        self.assertEqual(expected, actual)


# ### Invariance

class Test_invariance(unittest.TestCase):
    def setUp(self):
        self.nw = Nanoword.random_generator(7)
        self.nw_for_riii = Nanoword("EBCEABADCD",
                                    [Letter('A','b-'), Letter('B','b-'), Letter('C','a-'), Letter('D','b+'), Letter('E','b+')])
    def tearDown(self):
        del self.nw
    #---
    def test_invariance_of_self_linking_under_rmi(self):
        for ltr in self.nw.alphabet:
            with self.subTest(ltr = ltr):
                expected = self.nw.self_linking(ltr)
                actual = R.I(self.nw, reverse=True).self_linking(ltr)
                self.assertEqual(expected, actual) 
                
    def test_invariance_of_self_linking_function_under_rmii(self):
        for x in ['a', 'b']:
            with self.subTest(x = x):
                expected = self.nw.self_linking_function(x)
                actual = R.II(self.nw, reverse=True).self_linking_function(x)
                self.assertEqual(expected, actual)
                
    def test_invariance_of_self_linking_function_under_rmiii(self):
        mnw = self.nw_for_riii
        for x in ['a', 'b']:
            with self.subTest(x = x):
                expected = mnw.self_linking_function(x)
                actual = R.III(mnw).self_linking_function(x)
                self.assertEqual(expected, actual)     
    #---
    def test_invariance_of_sl_polynomial_under_rmi(self):
        for x in ['a', 'b']:
            with self.subTest(x = x):
                expected = self.nw.sl_polynomial(x)
                actual = R.I(self.nw, reverse=True).sl_polynomial(x)
                self.assertEqual(expected, actual) 
                
    def test_invariance_of_sl_polynomial_under_rmii(self):
        for x in ['a', 'b']:
            with self.subTest(x = x):
                expected = self.nw.sl_polynomial(x)
                actual = R.II(self.nw, reverse=True).sl_polynomial(x)
                self.assertEqual(expected, actual) 

    def test_invariance_of_sl_polynomial_under_rmiii(self):
        mnw = self.nw_for_riii
        for x in ['a', 'b']:
            with self.subTest(x = x):
                expected = mnw.sl_polynomial(x)
                actual = R.III(mnw).sl_polynomial(x)
                self.assertEqual(expected, actual) 
    #---
    def test_invariance_of_ab_polynomials_under_rmi(self):
        expected = self.nw.ab_polynomials()
        actual = R.I(self.nw, reverse=True).ab_polynomials()
        self.assertEqual(expected, actual)                 
        
    def test_invariance_of_ab_polynomials_under_rmii(self):
        expected = self.nw.ab_polynomials()
        actual = R.II(self.nw, reverse=True).ab_polynomials()
        self.assertEqual(expected, actual)
    def test_invariance_of_ab_polynomials_under_rmiii(self):
        mnw = self.nw_for_riii
        expected = mnw.ab_polynomials()
        actual = R.III(mnw).ab_polynomials()
        self.assertEqual(expected, actual)
    #---
    def test_invariance_of_writhe_polynomial_under_rmi(self):
        expected = self.nw.writhe_polynomial()
        actual = R.I(self.nw, reverse=True).writhe_polynomial()
        self.assertEqual(expected, actual)
        
    def test_invariance_of_writhe_polynomial_under_rmii(self):
        expected = self.nw.writhe_polynomial()
        actual = R.II(self.nw, reverse=True).writhe_polynomial()
        self.assertEqual(expected, actual) 
        
    def test_invariance_of_writhe_polynomial_under_rmiii(self):
        mnw = self.nw_for_riii
        expected = mnw.writhe_polynomial()
        actual = R.III(mnw).writhe_polynomial()
        self.assertEqual(expected, actual)        


# ## Running tests

if __name__ == "__main__":
    unittest.main()

### End of File