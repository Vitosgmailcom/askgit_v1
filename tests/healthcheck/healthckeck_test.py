import pytest
import logging as log

@pytest.mark.healthcheck
@pytest.mark.hc1
def test_healthcheck():
    log.info("Running Healthcheck test")
    log.debug("Hello world")

@pytest.mark.healthcheck
@pytest.mark.hc2
def test_database_connection_healthcheck():
    pass
