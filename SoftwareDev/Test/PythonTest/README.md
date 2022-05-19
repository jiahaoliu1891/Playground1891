#  A gentle introduction into Python test in VSCode

See details in the [Blog](https://code.visualstudio.com/docs/python/testing#_test-configuration-settings).

## 1. Configure tests
You can configure your tests anytime by using the Python: Configure Tests command from the Command Palette. You can also configure testing manually by setting either `python.testing.unittestEnabled` or `python.testing.pytestEnabled` to `true`. Each framework also has specific configuration settings as described under Test configuration settings for their folders and patterns.

**If both frameworks are enabled, then the Python extension will only run `pytest`.**

## 2. Create tests

Note here the testfiles names (`test_unittest.py` and `test_pytest.py`) syntax is defined in the configuration step for auto test discovery.

### Tests in unittest
Create a file named `test_pytest.py` that contains two test methods:

```
import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()
```

### Tests in pytest
Create a file named `test_pytest.py` that contains two test methods:
```
import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 4
```

