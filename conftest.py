# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--filename", action="store", default="test_1.xml")
