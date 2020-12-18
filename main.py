import unittest, xmlrunner, json, requests

data = json.load(open('tests.json', 'r'))

class Tests(unittest.TestCase): pass

def add_test(cls, name):
    def abstract_test(self):
        self.assertEqual(requests.request(**data[name]['request']).status_code, data[name]['assert']['statusCode'])
    setattr(cls, name, abstract_test)

for test_name in data.keys():
    add_test(Tests, test_name)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner())