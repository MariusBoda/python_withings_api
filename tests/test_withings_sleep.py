import time
import unittest

from withings_api import WithingsSleep, WithingsSleepSeries


class TestWithingsSleep(unittest.TestCase):
    def test_attributes(self):
        data = {
            "series": [{
                "startdate": 1387235398,
                "state": 0,
                "enddate": 1387235758
            }, {
                "startdate": 1387243618,
                "state": 1,
                "enddate": 1387244518
            }],
            "model": 16
        }
        sleep = WithingsSleep(data)
        self.assertEqual(sleep.model, data['model'])
        self.assertEqual(type(sleep.series), list)
        self.assertEqual(len(sleep.series), 2)
        self.assertEqual(type(sleep.series[0]), WithingsSleepSeries)
        self.assertEqual(sleep.series[0].startdate.timestamp,
                         data['series'][0]['startdate'])
        self.assertEqual(sleep.series[0].enddate.timestamp,
                         data['series'][0]['enddate'])
