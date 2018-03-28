import os

import yaml
import pytest


@pytest.fixture
def yaml_config():
    file_path = os.path.abspath('environment/env.yaml')
    with open(file_path, 'r') as f:
        return yaml.load(f)
