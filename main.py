import unittest, xmlrunner, json, requests, glob

def abstract_test(self, data):
    response: requests.Response = requests.request(**data['request'])
    self.assertEqual(response.status_code, data['assert']['statusCode'])
    self.assertSetEqual(set(response.json().keys()), set(data['assert']['responseKeys']))
    self.assertLessEqual(response.elapsed.total_seconds(), data['assert']['responseTime'])

for file_name in glob.iglob("*.json"):
    with open(file_name, 'r') as json_file:
        test = lambda data: lambda self: abstract_test(self, data)
        suite_name = file_name.split('.')[0]
        globals()[suite_name] = type(suite_name, (unittest.TestCase,), {name: test(data) for name, data in json.load(json_file).items()})

unittest.main(testRunner=xmlrunner.XMLTestRunner())
