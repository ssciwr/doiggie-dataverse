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
    
    # License - > data: latestVersion: license
licenses_testcases = [
    # TESTCASE 1: empty API response
    
    # TESTCASE 2: malformed API response
    
    # TESTCASE 3: 1 custom license in API response
    
    # TESTCASE 4: 1 license in API response
    
    
]

@pytest.mark.parametrize(
    "always_mock,json_resp,result", licenses_testcases
)
def test_licenses(
    data_repo_tester, 
    always_mock,
    json_resp,  
    result
    ): 
    repo_tester = data_repo_tester() 
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(doi="doi", archive_path=DataverseTestRecord.archive_path) # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.licenses()
        else:
            assert repo_tester.repo.licenses() == result

download_url_testcases =  [
    # TESTCASE 1: empty API response
    (
        True,
        {"data": []},
        "file1",
        ValueError(f"File 'file1' not found in data archive {DataverseTestRecord.archive_path} (doi:{DataverseTestRecord.doi})."),
    ),
    
    # TESTCASE 2: malformed API response
    
    
    # TESTCASE 2.5: malformed article_search response
    # what happens with artile_search respones has no "id" key
    
    # TESTCASE 3: valid API response with valid filename
    
    # TESTCASE 4: valid API response with invalid filename
    
]

@pytest.mark.parametrize(
    "always_mock,json_resp,filename,result", download_url_testcases
)
def test_download_url(
    data_repo_tester, 
    always_mock,
    json_resp,  
    filename,
    result
    ): 
    repo_tester = data_repo_tester() 
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(doi="doi", archive_path=DataverseTestRecord.archive_path) # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.download_url(filename)
        else:
            assert repo_tester.repo.download_url(filename) == result


create_registry_testcases = [
    # TESTCASE 1: empty API response
    (
        True,
        DataverseTestRecord.endpoints.data.response,
        {}
    ),
    
    # TESTCASE 2: malformed API response (no checksum given)
    (
        True,
        {
            "files": # TODO: access how? ( me dumb dumb brain not work right)
            [
            {
                "label":"store.zip",
                "restricted":False,
                "version":1,
                "datasetVersionId":835,
                "dataFile":
                {
                    "id":7133,
                    "persistentId":"doi:10.11588/DATA/TKCFEF/AUYGU0",
                    "pidURL":"https://doi.org/10.11588/DATA/TKCFEF/AUYGU0",
                    "filename":"store.zip",
                    "contentType":"application/zip",
                    "friendlyType":"ZIP Archive",
                    "filesize":780,
                    "storageIdentifier":"file://182256820cb-1b809ce28540",
                    "rootDataFileId":-1,
                    "md5":"7008231125631739b64720d1526619ae",
                    "checksum":
                    {
                        "type":"MD5","value":""
                    },
                    "tabularData":False,
                    "creationDate":"2022-07-22",
                    "publicationDate":"2022-07-25",
                    "fileAccessRequest":True
                }
            },
            {
                "label":"tiny-data.txt",
                "restricted":False,
                "version":1,
                "datasetVersionId":835,
                "dataFile":
                {
                    "id":7132,
                    "persistentId":"doi:10.11588/DATA/TKCFEF/B6S0HJ",
                    "pidURL":"https://doi.org/10.11588/DATA/TKCFEF/B6S0HJ",
                    "filename":"tiny-data.txt",
                    "contentType":"text/plain",
                    "friendlyType":"Plain Text",
                    "filesize":59,
                    "storageIdentifier":"file://18225682036-a6b8da436c53",
                    "rootDataFileId":-1,
                    "md5":"70e2afd3fd7e336ae478b1e740a5f08e",
                    "checksum":
                    {
                        "type":"MD5",
                        "value":""
                    },
                    "tabularData":False,
                    "creationDate":"2022-07-22",
                    "publicationDate":"2022-07-25",
                    "fileAccessRequest":True
                }
            }
            ]
        },
        KeyError("checksum"),
    ),
    # TESTCASE 3: valid API response
    (
        False, 
        DataverseTestRecord.endpoints.data.response,
        
    ),
    
    ]


@pytest.mark.parametrize(
    "always_mock,,json_resp,result", 
    create_registry_testcases
)
def test_create_registry(
    data_repo_tester, 
    always_mock,
    json_resp,  
    result
    ): 
    repo_tester = data_repo_tester() 
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(doi="doi", archive_path=DataverseTestRecord.archive_path) # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.create_registry()
        else:
            assert repo_tester.repo.create_registry() == result