import unittest
from functools import lru_cache


# Sample Data Source function
def fetch_data_from_source(key):
    return {"key1": "value1", "key2": "value2"}[key]


# Caching decorator using lru_cache
@lru_cache(maxsize=100)
def cached_data_mission(key):
    return fetch_data_from_source(key)


class TestCachingStrategies(unittest.TestCase):
    def test_cache_invalidation(self):
        key = "key1"
        # First call should fetch data from the source
        self.assertEqual(cached_data_mission(key), "value1")

        # Simulate data update in the source
        data_source = {"key1": "updated_value1"}

        # Invalidate the cache entry for key
        cached_data_mission.cache_clear()  # Clears the entire cache
        # Or you can use cached_data_mission.cache_remove(key) to invalidate specific keys

        # After invalidation, the cache should fetch data from the source again
        self.assertEqual(cached_data_mission(key), "updated_value1")


if __name__ == "__main__":
    unittest.main()
