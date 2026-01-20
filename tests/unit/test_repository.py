import pytest

from tests.data.dataverse_record import DataverseTestRecord

#from pooch_doi.license import * #Commented out for quick testing, TODO: Comment back in when importing error has been fixed
from pooch_dataverse.repository import DataverseRepository

def test_sanity_checks(sanity_check_data_repo):
    sanity_check_data_repo(DataverseRepository)
    
def test_initialize(data_repo_tester):
    # TESTCASE 1: With invalid archive_path -> invalid archive_url
    data_repo_tester().assert_repo_does_initialize(archive_path="/somevalue/abc")

    # TESTCASE 2: With valid archive_url  but invalid api response
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=True) as m:
        m.get(DataverseTestRecord.endpoints.data.path, status_code=404) # TODO: Is this access correct?
        repo_tester.assert_repo_does_not_initialize(
            archive_path=DataverseTestRecord.archive_path
        )
        
    # TESTCASE 3: With valid archive_url and valid api response -> valid archive_url
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker() as m:
        m.get(DataverseTestRecord.endpoints.data.path, json={"key": "valid response"})
        repo_tester.assert_repo_does_initialize(
            archive_path=DataverseTestRecord.archive_path
        )
    
licenses_testcases = [
    # TESTCASE 1: empty API response
    
    # TESTCASE 2: malformed API response
    
    # TESTCASE 3: 1 custom license in API response
    
    # TESTCASE 4: 1 license in API response
    
    
]

@pytest.mark.parametrize(
    "always_mock,record_id,status_code,json_resp,result", licenses_testcases
)
def test_licenses(
    data_repo_tester, 
    always_mock,
    record_id,
    json_resp, 
    filename, 
    result
    ):
    repo_tester = data_repo_tester() # TODO: Fit to Dataverse
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(f"/api/records/{record_id}/files", json=json_resp)
        repo_tester.initialize_repo(doi="doi", archive_path=f"/records/{record_id!s}")
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.download_url(filename)
        else:
            assert repo_tester.repo.download_url(filename) == result
                
create_registry_testcases = [
    # TESTCASE 1: empty API response
    
    # TESTCASE 2: malformed API response (no checksum given)
    
    # TESTCASE 3: valid API response
    
]


@pytest.mark.parametrize(
    "always_mock,record_id,json_resp,result", 
    create_registry_testcases
)
def test_create_registry(
    data_repo_tester, 
    always_mock, 
    record_id, 
    json_resp, 
    result
    ):
    repo_tester = data_repo_tester() # TODO: Fit to Dataverse
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(f"/api/records/{record_id}/files", json=json_resp)
        repo_tester.initialize_repo(doi="doi", archive_path=f"/records/{record_id}")
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.create_registry()
        else:
            assert repo_tester.repo.create_registry() == result