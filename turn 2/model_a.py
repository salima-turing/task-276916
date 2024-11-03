import unittest
from functools import lru_cache
import time

# Sample Data Source function
data_source = {"key1": "value1", "key2": "value2"}


def fetch_data_from_source(key):
    return data_source[key]


# Caching decorator with TTL
CACHE_TTL = 5  # Seconds


@lru_cache(maxsize=100)
def cached_data_mission(key):
    data = fetch_data_from_source(key)
    # Simulate cache entry with TTL
    cached_data_mission.cache_info()[3][key] = time.time() + CACHE_TTL
    return data


def is_cache_stale(key):
    cache_entry = cached_data_mission.cache_info()[3].get(key)
    if cache_entry and cache_entry < time.time():
        return True
    return False


class TestCachingStrategies(unittest.TestCase):
    def test_lru_cache_stale_data(self):
        key = "key1"
        self.assertEqual(cached_data_mission(key), "value1")

        # Manually update data source to simulate change
        data_source[key] = "new_value1"

        # Wait for cache to expire
        time.sleep(CACHE_TTL + 1)

        self.assertTrue(is_cache_stale(key))
        # Cache should be stale, fetch from source again
        self.assertEqual(cached_data_mission(key), "new_value1")


if __name__ == "__main__":
    unittest.main()
