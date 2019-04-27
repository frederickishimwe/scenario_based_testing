import unittest
from scenario import SCENARIOS_TO_TEST
from base import ScenarioMeta, ScenerioTest


# These are functions you can use during the tests, it applies to all scenarios#
def postman_get(request_data):
    response = {"status":200}
    return response
def car_automation(test):
    print(test)
    return test

# Test Case #
class TestScenarioMethods(unittest.TestCase):
    __metaclass__ = ScenarioMeta

    class postman_sampletest(ScenerioTest):
        scenarios = SCENARIOS_TO_TEST

        def __test__(self, name, match, request_data, response_data):
            response_json = car_automation(request_data)
            if match:
                self.assertEqual(response_json, response_data)
            else:
                response_json = postman_get(request_data)
                self.assertNotEqual(response_json, response_data)


if __name__ == "__main__":
    unittest.main()
