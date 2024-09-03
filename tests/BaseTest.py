import pytest
from utilities import ExcelReader
from utilities import CustomLogger

@pytest.mark.usefixtures("setup_and_teardown")

class BaseTest:

    logger = CustomLogger.Logger.gen_Log()
    pass
