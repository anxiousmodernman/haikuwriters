from os import path

# Import all standard settings (required)
from haikuwriters.settings import *

TEST_DISCOVER_TOP_LEVEL = path.dirname(path.dirname(__file__))
TEST_DISCOVER_ROOT = path.join(TEST_DISCOVER_TOP_LEVEL, 'tests')
