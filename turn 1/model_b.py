import unittest
from functools import lru_cache

# Sample Data Source function
def fetch_data_from_source(key):
    # Simulate expensive data retrieval
    return {"key1": "value1", "key2": "value2"}[key]

# Simple in-memory cache
class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

# Caching decorator using lru_cache
@lru_cache(maxsize=100)  # Cache up to 100 entries
def cached_data_mission(key):
    return fetch_data_from_source(key)

#Unit test class
class TestCachingStrategies(unittest.TestCase):
    def test_lru_cache(self):
        # Test with lru_cache
        key = "key1"
        # First call should fetch data from the source
        self.assertEqual(cached_data_mission(key), "value1")
        # Subsequent calls should retrieve from the cache
        self.assertEqual(cached_data_mission(key), "value1")

    def test_simple_cache(self):
        # Test with simple_cache
        cache = SimpleCache()
        key = "key2"
        # First call should fetch data from the source and store in the cache
        result = fetch_data_from_source(key)
        cache.set(key, result)
        self.assertEqual(cache.get(key), result)
        # Second call should retrieve from the cache
        self.assertEqual(cache.get(key), result)

if __name__ == "__main__":
    unittest.main()
