import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('testCases')
    runner = unittest.TextTestRunner()
    runner.run(suite)