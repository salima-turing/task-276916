import unittest
from typing import Dict


class DataMission:
    def __init__(self):
        self.cache: Dict[str, int] = {}

    def execute_data_mission(self, data_source: str) -> int:
        # Simulate data retrieval and processing
        if data_source in self.cache:
            print(f"Returning cached result for {data_source}")
            return self.cache[data_source]

        result = self.fetch_data(data_source)
        self.cache[data_source] = result
        return result

    def fetch_data(self, data_source: str) -> int:
        # Simulate data fetch
        if data_source == "slow_data":
            return 42
        return len(data_source)


class TestDataMissionWithCaching(unittest.TestCase):
    def setUp(self):
        self.mission = DataMission()

    def test_data_mission_without_caching(self):
        result = self.mission.execute_data_mission("fast_data")
        self.assertEqual(result, 8)

        result = self.mission.execute_data_mission("slow_data")
        self.assertEqual(result, 42)

    def test_data_mission_with_caching(self):
        # First execution with caching
        result = self.mission.execute_data_mission("fast_data")
        self.assertEqual(result, 8)

        # Second execution should return the cached result
        result = self.mission.execute_data_mission("fast_data")
        self.assertEqual(result, 8)

        # Clear cache to isolate test
        self.mission.cache.clear()
        result = self.mission.execute_data_mission("slow_data")
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
