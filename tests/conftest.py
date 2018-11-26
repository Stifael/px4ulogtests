# read arguments from command line if we want to run a pytest
# the argument is stored and can be given as an argument to tests

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--filepath", action="store", default="Please pass absolute log file path as argument", help="absolute path to log file"
    )

@pytest.fixture
def filepath(request):
    return request.config.getoption("--filepath")