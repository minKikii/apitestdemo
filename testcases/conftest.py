import  pytest
from common.yaml_util import YamlUtil
@pytest.fixture(scope="session",autouse=True)
def clear_extract():
    YamlUtil.clean_extract_yaml()