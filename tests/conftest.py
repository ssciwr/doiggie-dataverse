import pytest
from pooch_dataverse.repository import (
    DataverseRepository,
)
from tests.data.dataverse_record import DataverseTestRecord

pytest_plugins = ["pooch_doi.testkit"]


@pytest.fixture(scope="session")
def data_repo_tester(create_data_repo_tester_type):
    return create_data_repo_tester_type(
        DataverseRepository, base_url_fallback="https://dataverse.org"
    )

"""
@pytest.fixture
def create_initialized_data_repo_tester(data_repo_tester):
    def _func(record_id):
        instance = data_repo_tester()
        with instance.endpoint_mocker() as m:
            m.get(
                f"/api/datasets/:persistentId?persistentId={record_id!s}",
                json=DataverseTestRecord.endpoints.files.response,
            )
            instance.initialize_repo("doi", f"/records/{record_id}")
        return instance

    return _func
"""