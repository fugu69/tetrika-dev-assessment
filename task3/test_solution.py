import unittest

from solution import appearance

class TestAppearanceFunction(unittest.TestCase):

    def test_empty_intervals(self):
        intervals = {'lesson': [1000, 2000], 'pupil': [], 'tutor': []}
        self.assertEqual(appearance(intervals), 0)

    def test_no_overlap(self):
        intervals = {'lesson': [1000, 2000],
                     'pupil': [1000, 1500],
                     'tutor': [1501, 2000]}
        self.assertEqual(appearance(intervals), 0)

    def test_pupil_outside_lesson(self):
        intervals = {'lesson': [1000, 2000],
                     'pupil': [900, 950],
                     'tutor': [1000, 2000]}
        self.assertEqual(appearance(intervals), 0)

    def test_exact_lesson_bounds(self):
        intervals = {'lesson': [1000, 2000],
                     'pupil': [1000, 2000],
                     'tutor': [1000, 2000]}
        self.assertEqual(appearance(intervals), 1000)

    def test_partial_overlap(self):
        intervals = {'lesson': [1000, 2000],
                     'pupil': [1100, 1500],
                     'tutor': [1200, 1600]}
        self.assertEqual(appearance(intervals), 300)  # Overlap is 1200 to 1500

if __name__ == '__main__':
    unittest.main()
