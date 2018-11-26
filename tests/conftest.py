# read arguments from command line if we want to run a pytest
# the argument is stored and can be given as an argument to tests

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--filepath", action="store", default="Please pass absolute log file path as argument", help="absolute path to log file"
    )

# With scope set to module, the fixture function only gets invoked once per module
@pytest.fixture(scope="module")
def filepath(request):
    return request.config.getoption("--filepath")