import unittest
from tkinter import Tk
import final




root = Tk()
gui = final.Std_information(root)


class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):

        array_test = [('1', 'Tsering','mahankal','security','1234567890'),('2', 'Dolma','Kathmandu','Computing','9866889900')]
        expected_result = [('1','Tsering','mahankal','security','1234567890'),('2', 'Dolma','Kathmandu','Computing','9866889900')]

        gui.sortcombo.set('Ascending')
        ac_result=gui.bubbleSort(array_test)
        self.assertEqual(expected_result,ac_result)


    def test_search(self):
        array_test = [('1', 'Tsering','mahankal','security','1234567890'),('2', 'Dolma','Kathmandu','Computing','9866889900')]
        expected_result = ('1', 'Tsering','mahankal','security','1234567890')
        gui.searchentry.delete(0, 'end')
        gui.searchentry.insert(0, 'Tsering')
        ac_result = gui.search(array_test)
        self.assertEqual(expected_result, ac_result)

if __name__=='_main_':
    unittest.main()
