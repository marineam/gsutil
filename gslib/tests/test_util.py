# Copyright 2013 Google Inc. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""Tests for gsutil utility functions."""

from gslib import util
import gslib.tests.testcase as testcase


class TestUtil(testcase.GsUtilUnitTestCase):
  """Tests for utility functions."""

  def test_MakeHumanReadable(self):
    self.assertEqual(util.MakeHumanReadable(0), '0 B')
    self.assertEqual(util.MakeHumanReadable(1023), '1023 B')
    self.assertEqual(util.MakeHumanReadable(1024), '1 KB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 2), '1 MB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 3), '1 GB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 3 * 5.3), '5.3 GB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 4 * 2.7), '2.7 TB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 5), '1 PB')
    self.assertEqual(util.MakeHumanReadable(1024 ** 6), '1 EB')

  def test_MakeBitsHumanReadable(self):
    self.assertEqual(util.MakeBitsHumanReadable(0), '0 bit')
    self.assertEqual(util.MakeBitsHumanReadable(1023), '1023 bit')
    self.assertEqual(util.MakeBitsHumanReadable(1024), '1 Kbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 2), '1 Mbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 3), '1 Gbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 3 * 5.3), '5.3 Gbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 4 * 2.7), '2.7 Tbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 5), '1 Pbit')
    self.assertEqual(util.MakeBitsHumanReadable(1024 ** 6), '1 Ebit')

  def test_HumanReadableToBytes(self):
    self.assertEqual(util.HumanReadableToBytes('1'), 1)
    self.assertEqual(util.HumanReadableToBytes('15'), 15)
    self.assertEqual(util.HumanReadableToBytes('15.3'), 15)
    self.assertEqual(util.HumanReadableToBytes('15.7'), 16)
    self.assertEqual(util.HumanReadableToBytes('1023'), 1023)
    self.assertEqual(util.HumanReadableToBytes('1k'), 1024)
    self.assertEqual(util.HumanReadableToBytes('2048'), 2048)
    self.assertEqual(util.HumanReadableToBytes('1 K'), 1024)
    self.assertEqual(util.HumanReadableToBytes('1 mb'), 1024 ** 2)
    self.assertEqual(util.HumanReadableToBytes('1 GB'), 1024 ** 3)
    self.assertEqual(util.HumanReadableToBytes('1T'), 1024 ** 4)
    self.assertEqual(util.HumanReadableToBytes('1\t   pb'), 1024 ** 5)
    self.assertEqual(util.HumanReadableToBytes('1e'), 1024 ** 6)
