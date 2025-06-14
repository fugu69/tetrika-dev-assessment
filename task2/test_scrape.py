"""import unittest
from unittest.mock import patch
from scrape import get_all_links, save_counts_to_csv
import os

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://ru.wikipedia.org/fake-url"
        self.mock_links = ["/wiki/Animal1", "/wiki/Animal2", "/wiki/Белка"]
        self.mock_next_url = None

    @patch('scrape.get_links_from_page')
    def test_get_all_links_mocked(self, mock_get_links):
        # Simulate one page of results
        mock_get_links.return_value = (self.mock_links, self.mock_next_url)

        result = get_all_links(self.test_url)
        self.assertEqual(result['A'], 2)
        self.assertEqual(result['Б'], 1)
        self.assertIsInstance(result, dict)

    def test_save_counts_to_csv(self):
        test_data = {'A': 2, 'Б': 1}
        test_filename = 'test_output.csv'

        save_counts_to_csv(test_data, test_filename)
        self.assertTrue(os.path.exists(test_filename))

        with open(test_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)  # Header + 2 rows

        os.remove(test_filename)

if __name__ == '__main__':
    unittest.main()
"""

import unittest
from unittest.mock import patch
from scrape import get_all_links, save_counts_to_csv
import os

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://ru.wikipedia.org/fake-url"
        # Используем русские и английские буквы для теста
        self.mock_links = ["/wiki/Animal1", "/wiki/Арбуз", "/wiki/Белка"]
        self.mock_next_url = None

    @patch('scrape.get_links_from_page')
    def test_get_all_links_mocked(self, mock_get_links):
        # Эмулируем одну страницу с ссылками
        mock_get_links.return_value = (self.mock_links, self.mock_next_url)

        result = get_all_links(self.test_url)
        self.assertEqual(result['A'], 1)
        self.assertEqual(result['А'], 1)  # Кириллическая 'А'
        self.assertEqual(result['Б'], 1)
        self.assertIsInstance(result, dict)

    def test_save_counts_to_csv(self):
        test_data = {'A': 1, 'А': 1, 'Б': 1}
        test_filename = 'test_output.csv'

        save_counts_to_csv(test_data, test_filename)
        self.assertTrue(os.path.exists(test_filename))

        with open(test_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 4)  # Заголовок + 3 строки

        os.remove(test_filename)

if __name__ == '__main__':
    unittest.main()
