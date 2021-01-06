import unittest
import xmlrunner
import json
import requests
import glob

for file_name in glob.iglob("*.json"):
    with open(file_name, 'r') as json_file:
        tests_dict = {name: (lambda data: lambda self: self.assertEqual(
            requests.request(**data['request']).status_code, data['assert']['statusCode']))(data)
                      for name, data in json.load(json_file).items()}
        suite_name = file_name.split('.')[0]
        globals()[suite_name] = type(suite_name, (unittest.TestCase,), tests_dict)

unittest.main(testRunner=xmlrunner.XMLTestRunner())
