import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


from user import user
from unittest import TestCase
from unittest.mock import patch, mock_open, Mock
from tkinter import *

class TestStart(TestCase):
	def setUp(self):
		root = Tk()
		bg_color = "white"
		user_login = "user1"
		cur = Mock()
		cur.fetchall.return_value = [("1"), ()]
		self.t_user = user(root, "white", user_login, cur)


	def test_choose_button(self):
		with patch.object(self.t_user, 'remove_start', return_value=None) as mock_method1:
			with patch.object(self.t_user, 'place_choose', return_value=None) as mock_method2:
				self.t_user.choose()

		mock_method1.assert_called_with()
		mock_method2.assert_called_with()


	def test_show_my_workouts_button(self):
		with patch.object(self.t_user, 'remove_start', return_value=None) as mock_method1:
			with patch.object(self.t_user, 'place_my_worklouts', return_value=None) as mock_method2:
				self.t_user.show_my_workouts()

		mock_method1.assert_called_with()
		mock_method2.assert_called_with()


	def test_back_to_start_button(self):
		with patch.object(self.t_user, 'remove_choose', return_value=None) as mock_method1:
			with patch.object(self.t_user, 'place_start', return_value=None) as mock_method2:
				self.t_user.back_to_start()

		mock_method1.assert_called_with()
		mock_method2.assert_called_with()


	def test_back_to_choose_button(self):
		with patch.object(self.t_user, 'remove_trainlist', return_value=None) as mock_method1:
			with patch.object(self.t_user, 'place_choose', return_value=None) as mock_method2:
				self.t_user.back_to_choose()	

		mock_method1.assert_called_with()
		mock_method2.assert_called_with()

