import pytest

from tests.data.dataverse_record import DataverseTestRecord

from doiggie.license import *  # Commented out for quick testing, TODO: Comment back in when importing error has been fixed
from doiggie_dataverse.repository import DataverseRepository


def test_sanity_checks(sanity_check_data_repo):
    sanity_check_data_repo(DataverseRepository)


def test_initialize(data_repo_tester):
    # TESTCASE 1: With valid archive_url  but invalid api response
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=True) as m:
        m.get(DataverseTestRecord.endpoints.data.path, status_code=404)
        repo_tester.assert_repo_does_not_initialize(
            doi=DataverseTestRecord.doi, archive_path=DataverseTestRecord.archive_path
        )

    # TESTCASE 2: With valid archive_url and valid api response -> valid archive_url
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=True) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json={"key": "valid response"})
        repo_tester.assert_repo_does_initialize(
            doi=DataverseTestRecord.doi, archive_path=DataverseTestRecord.archive_path
        )


# License - > data: latestVersion: license
licenses_testcases = [
    # TESTCASE 1: empty API response
    (True, {}, KeyError("data")),
    # TESTCASE 2: malformed API response (empty license)
    (
        True,
        {
            "status": "OK",
            "data": {
                "latestVersion": {
                    "license": {},
                }
            },
        },
        list(),
    ),
    # TESTCASE 3: 1 custom license in API response
    (
        True,
        {
            "status": "OK",
            "data": {
                "latestVersion": {
                    "license": {
                        "name": "Custom License",
                        # "uri":"http://creativecommons.org/licenses/by/4.0",
                        # "iconUri":"https://licensebuttons.net/l/by/4.0/88x31.png"
                    }
                }
            },
        },
        License(name="Custom License"),
    ),
    # TESTCASE 4: 1 license in API response
    (
        False,
        DataverseTestRecord.endpoints.data.response,  # actual response only has one license
        License(
            name="CC BY 4.0",
            identifiers=[
                LicenseIdentifier(
                    scheme=LicenseIdentifierScheme.URL,
                    value="http://creativecommons.org/licenses/by/4.0",
                )
            ],
        ),
        # ["CC BY 4.0","http://creativecommons.org/licenses/by/4.0", "https://licensebuttons.net/l/by/4.0/88x31.png"],
    ),
]


@pytest.mark.parametrize("always_mock,json_resp,result", licenses_testcases)
def test_licenses(data_repo_tester, always_mock, json_resp, result):
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(
            doi=DataverseTestRecord.doi, archive_path=DataverseTestRecord.archive_path
        )  # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.licenses()
        else:
            assert repo_tester.repo.licenses() == result


download_url_testcases = [
    # TESTCASE 1: empty API response
    (True, {}, "file1", KeyError("data")),
    # TESTCASE 2: malformed API response
    # TESTCASE 2.5: malformed article_search response
    # what happens with artile_search respones has no "id" key
    # TESTCASE 3: valid API response with valid filename
    (
        False,
        DataverseTestRecord.endpoints.data.response,
        "store.zip",
        f"{DataverseTestRecord.base_url}/api/access/datafile/7133",
    ),
    # TESTCASE 4: valid API response with invalid filename
    (
        False,
        DataverseTestRecord.endpoints.data.response,
        "wrongFileName.zip",
        ValueError(f"File 'wrongFileName.zip' not found in data archive"),
    ),
]


@pytest.mark.parametrize(
    "always_mock,json_resp,filename,result", download_url_testcases
)
def test_download_url(data_repo_tester, always_mock, json_resp, filename, result):
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(
            doi=DataverseTestRecord.doi, archive_path=DataverseTestRecord.archive_path
        )  # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.download_url(filename)
        else:
            assert repo_tester.repo.download_url(filename) == result


create_registry_testcases = [
    # TESTCASE 1: empty API response
    (
        True,
        {},
        # {}, # registry will be empty
        KeyError("data"),
    ),
    # TESTCASE 2: malformed API response (no checksum given)
    (
        True,
        {
            "status": "OK",
            "data": {
                "latestVersion": {
                    "files": [
                        {"dataFile": {"checksum": {}}},
                        {"dataFile": {"checksum": {}}},
                    ]
                }
            },
        },
        KeyError("md5"),
    ),
    # TESTCASE 3: valid API response
    (
        False,
        DataverseTestRecord.endpoints.data.response,
        {
            "store.zip": "md5:7008231125631739b64720d1526619ae",
            "tiny-data.txt": "md5:70e2afd3fd7e336ae478b1e740a5f08e",
        },
    ),
]


@pytest.mark.parametrize("always_mock,,json_resp,result", create_registry_testcases)
def test_create_registry(data_repo_tester, always_mock, json_resp, result):
    repo_tester = data_repo_tester()
    with repo_tester.endpoint_mocker(always_mock=always_mock) as m:
        m.get(DataverseTestRecord.endpoints.data.path, json=json_resp)
        repo_tester.initialize_repo(
            doi=DataverseTestRecord.doi, archive_path=DataverseTestRecord.archive_path
        )  # doi is given as string because it's unimportant in current context
        if isinstance(result, Exception):
            with pytest.raises(type(result), match=str(result)):
                repo_tester.repo.create_registry()
        else:
            assert repo_tester.repo.create_registry() == result
