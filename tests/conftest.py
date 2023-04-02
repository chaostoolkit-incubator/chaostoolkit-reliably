import io
import logging
import logging.handlers
from typing import Generator

import pytest


@pytest.fixture
def reconfigure_chaostoolkit_logger() -> Generator[logging.Logger, None, None]:
    ctk_logger = logging.getLogger("logzero_default")

    for handler in list(ctk_logger.handlers):
        ctk_logger.removeHandler(handler)

    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)
    ctk_logger.addHandler(handler)

    try:
        yield ctk_logger
    finally:
        stream.close()
