from unittest.mock import Mock
import pytest
from pooch_dataverse import repository
from pooch_dataverse import utils

valid_dataverse_doi: str = "doi:10.11588/data/TKCFEF/" #utils.pooch_test_dataverse_doi()
valid_dataverse_url: str = "https://dataverse.org/doi:10.11588/data/TKCFEF/" #utils.pooch_test_dataverse_url()

def test_download_url():
    #archive_url = "https://dataverse.example.org/dataset.xhtml?persistentId=doi:10.1234/ABC"
    
    fake_api_json = {
        "data": {
            "latestVersion": {
                "files": [
                    {
                        "dataFile": {
                            "id": 12345,
                            "filename": "testfile.txt"
                        }
                    }
                ]
            }
        }
    }
    
    mock_response = Mock()
    mock_response.json.return_value = fake_api_json
    
    repo = repository.DataverseRepository.initialize(
                archive_url=valid_dataverse_url,
                doi=valid_dataverse_doi,
            )
    
    download_url = repo.download_url("testfile.txt")
    
    assert download_url == (
        "https://dataverse.example.org/api/access/datafile/12345"
    )
