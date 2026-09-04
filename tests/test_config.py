"""Config loading tests."""

import yaml


def test_config_parses():
    data = yaml.safe_load("name: sift\nversion: 1\n")
    assert data["name"] == "sift"
