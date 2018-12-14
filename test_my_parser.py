from my_parser import *
from unittest import TestCase
from unittest.mock import patch, mock_open


class TestParser(TestCase):
	def setUp(self):
		create_file = (
            'CREATE TABLE club (club_id INTEGER NOT NULL,\n'
                   'club_name CHAR(25) NOT NULL,\n'
                   'club_city CHAR(25) NOT NULL,\n'
                   'club_addr CHAR(100) NOT NULL,\n'
                   'club_guest_count INTEGER NOT NULL,\n'
                   'PRIMARY KEY(club_id));\n\n'
            'CREATE TABLE sport (sport_id INTEGER NOT NULL,\n'
                    'sport_name CHAR(25) NOT NULL,\n'
                    'PRIMARY KEY(sport_id));'
        )

		self.mock_open = mock_open(read_data = create_file)


	def test_isnum(self):
		t1 = is_number("123")
		t2 = is_number("12.32")
		t3 = is_number("-123")
		t4 = is_number("-123.3434")
		t5 = is_number("23a4")
		t6 = is_number("sdsdsd")

		self.assertEqual(t1, True)
		self.assertEqual(t2, True)
		self.assertEqual(t3, True)
		self.assertEqual(t4, True)
		self.assertEqual(t5, False)
		self.assertEqual(t6, False)


	def test_convert(self):
		t1 = convert_base("A", to_base=10, from_base=16)
		t2 = convert_base("3", to_base=10, from_base=16)
		t3 = convert_base("AB", to_base=10, from_base=16)

		self.assertEqual(t1, '10')
		self.assertEqual(t2, '3')
		self.assertEqual(t3, '171')


	def test_get_from_file(self):
		with patch('builtins.open', self.mock_open):
			queries = get_create_table_queries('path/to/file')
			answer = []
			answer.append("CREATE TABLE club (club_id INTEGER NOT NULL,club_name CHAR(25) NOT NULL,club_city CHAR(25) NOT NULL,club_addr CHAR(100) NOT NULL,club_guest_count INTEGER NOT NULL,PRIMARY KEY(club_id))")
			answer.append("CREATE TABLE sport (sport_id INTEGER NOT NULL,sport_name CHAR(25) NOT NULL,PRIMARY KEY(sport_id))")
			self.assertListEqual(queries, answer)


	def test_get_format(self):
		data1 = "1|Box " 
		data2 = "2|Football "

		t1 = get_necessary_format(data1)
		t2 = get_necessary_format(data2)

		self.assertEqual(t1, "1,'Box')")
		self.assertEqual(t2, "2,'Football')")		