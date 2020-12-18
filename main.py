import unittest, xmlrunner, json, requests

class Tests(unittest.TestCase): pass

def add_test(cls, name, data):
    def abstract_test(self):
        self.assertEqual(requests.request(**data['request']).status_code, data['assert']['statusCode'])
    setattr(cls, name, abstract_test)

with open('tests.json', 'r') as json_file:
    for test_name, test_data in json.load(json_file).items():
        add_test(Tests, test_name, test_data)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner())
