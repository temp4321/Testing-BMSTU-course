import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


from start import start
from unittest import TestCase
from unittest.mock import patch, mock_open, Mock
from tkinter import *

class TestStart(TestCase):
	def setUp(self):
		root = Tk()
		cur = Mock()
		cur.execute.return_value = ""
		cur.fetchall.return_value = [('user1', '2110'), ('user2', '30411'), ('user3', '13105'), ('user4', '45234')]
		self.startpage = start(root, "white", cur)


	def test_init_and_place_widgets(self):
		self.startpage.place_all()

		t1 = self.startpage.loginlabel['state']
		t2 = self.startpage.passwordlabel['state']
		t3 = self.startpage.login['state']
		t4 = self.startpage.password['state']
		t5 = self.startpage.login_button['state']

		answers = ['normal' for i in range(5)]

		self.assertListEqual([t1, t2, t3, t4, t5], answers)

	
	def test_loginevent_button(self):
		self.startpage.place_all()
		with patch.object(self.startpage, 'login') as mock_method1:
			mock_method1.get.return_value = 'user1'
			with patch.object(self.startpage, 'password') as mock_method2:
				mock_method2.get.return_value = '2110'
				with patch.object(self.startpage, 'remove_all', return_value=None) as mock_method3:
					t = self.startpage.loginevent()

		mock_method1.get.assert_called_with('1.0', 'end-1c')
		mock_method2.get.assert_called_with('1.0', 'end-1c')
		self.assertEqual(t, True)


