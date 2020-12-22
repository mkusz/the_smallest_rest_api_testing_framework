import unittest, xmlrunner, json, requests

with open('tests.json', 'r') as json_file:
    Tests = type("Tests", (unittest.TestCase,), {name: (lambda data: lambda self: self.assertEqual(requests.request(**data['request']).status_code, data['assert']['statusCode']))(data) for name, data in json.load(json_file).items()})

unittest.main(testRunner=xmlrunner.XMLTestRunner())
