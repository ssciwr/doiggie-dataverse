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
"""
# License - > data: latestVersion: license
licenses_testcases = [
    # TESTCASE 1: empty API response
    (
        True,
        {"data": []},
        ValueError() # TODO: Check what kind of value error
    ),
    # TESTCASE 2: malformed API response (empty license)
    (
        True,
        {
            "status":"OK",
            "data":
            {
                "id":7131,
                "identifier":"data/TKCFEF",
                "persistentUrl":"https://doi.org/10.11588/DATA/TKCFEF",
                "protocol":"doi",
                "authority":"10.11588",
                "separator":"/",
                "publisher":"heiDATA",
                "publicationDate":"2022-07-25",
                "storageIdentifier":"file://10.11588/data/TKCFEF",
                "datasetType":"dataset",
                "latestVersion":
                {
                    "id":835,
                    "datasetId":7131,
                    "datasetPersistentId":"doi:10.11588/DATA/TKCFEF",
                    "storageIdentifier":"file://10.11588/data/TKCFEF",
                    "versionNumber":1,
                    "versionMinorNumber":0,
                    "versionState":"RELEASED",
                    "latestVersionPublishingState":"RELEASED",
                    "deaccessionLink":"",
                    "lastUpdateTime":"2022-07-25T07:10:39Z",
                    "releaseTime":"2022-07-25T07:10:39Z",
                    "createTime":"2022-07-22T10:14:58Z",
                    "publicationDate":"2022-07-25",
                    "citationDate":"2022-07-25",
                    "license":
                        {
                        },
                    "fileAccessRequest":True,
                    "metadataBlocks":
                    {
                        "citation":
                        {
                            "displayName":"Citation Metadata",
                            "name":"citation",
                            "fields":
                            [
                                {
                                    "typeName":"title",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"Test data for the Pooch library"
                                },
                                {
                                    "typeName":"otherId",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "otherIdAgency":
                                        {
                                            "typeName":"otherIdAgency",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Zenodo"
                                        },
                                        "otherIdValue":
                                        {
                                            "typeName":"otherIdValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"10.5281/zenodo.4924875"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"author",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "authorName":
                                        {
                                            "typeName":"authorName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, Leonardo"
                                        },
                                        "authorIdentifierScheme":
                                        {
                                            "typeName":"authorIdentifierScheme",
                                            "multiple":False,
                                            "typeClass":"controlledVocabulary",
                                            "value":"ORCID"
                                        },
                                        "authorIdentifier":
                                        {
                                            "typeName":"authorIdentifier",
                                           "multiple":False,
                                           "typeClass":"primitive",
                                          "value":"0000-0001-6123-9515"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"datasetContact",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "datasetContactName":
                                        {
                                            "typeName":"datasetContactName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Kempf, Dominic"
                                        },
                                        "datasetContactAffiliation":
                                        {
                                            "typeName":"datasetContactAffiliation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Scientific Software Center, Heidelberg University"
                                        },
                                        "datasetContactEmail":
                                        {
                                            "typeName":"datasetContactEmail",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"dominic.kempf@iwr.uni-heidelberg.de"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dsDescription",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "dsDescriptionValue":
                                        {
                                            "typeName":"dsDescriptionValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"<a href=\"https://github.com/fatiando/pooch\">Pooch</a> is an open-source Python library for data download. This archive contains testing data for Pooch's DataVerse download functionality."
                                        }
                                    }]
                                },
                                {
                                    "typeName":"subject",
                                    "multiple":True,
                                    "typeClass":"controlledVocabulary",
                                    "value":
                                        [
                                        "Computer and Information Science"
                                        ]   
                                },
                                {
                                    "typeName":"publication",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "publicationCitation":
                                        {
                                            "typeName":"publicationCitation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, L., Soler, S. R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D., Banihirwe, A., & Leeman, J. (2020). Pooch: A friend to fetch your data files. Journal of Open Source Software, 5(45), 1943."
                                        },
                                        "publicationIDType":
                                        {
                                            "typeName":"publicationIDType",
                                            "multiple":False,"typeClass":"controlledVocabulary",
                                            "value":"doi"
                                        },
                                        "publicationIDNumber":
                                        {
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "typeName":"publicationIDNumber",
                                            "value":"10.21105/joss.01943"
                                        },
                                        "publicationURL":
                                        {
                                            "typeName":"publicationURL",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"https://doi.org/10.21105/joss.01943"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dateOfDeposit",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"2022-07-22"
                                },
                                {
                                    "typeName":"software",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "softwareName":
                                        {
                                            "typeName":"softwareName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Pooch"
                                        }
                                    }]
                                }
                            ]
                        },
                        "geospatial":
                        {
                            "displayName":"Geospatial Metadata",
                            "name":"geospatial",
                            "fields":
                            []
                        }
                    },
                    "files":
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
                                },
                                "tabularData":False,
                                "creationDate":"2022-07-22",
                                "publicationDate":"2022-07-25",
                                "fileAccessRequest":True
                            }
                        }
                    ]
                }
            }
        },
        # TODO: What is that error?!
        KeyError("license"),
    ),
    # TESTCASE 3: 1 custom license in API response
    (
        False,
        {
            "status":"OK",
            "data":
            {
                "id":7131,
                "identifier":"data/TKCFEF",
                "persistentUrl":"https://doi.org/10.11588/DATA/TKCFEF",
                "protocol":"doi",
                "authority":"10.11588",
                "separator":"/",
                "publisher":"heiDATA",
                "publicationDate":"2022-07-25",
                "storageIdentifier":"file://10.11588/data/TKCFEF",
                "datasetType":"dataset",
                "latestVersion":
                {
                    "id":835,
                    "datasetId":7131,
                    "datasetPersistentId":"doi:10.11588/DATA/TKCFEF",
                    "storageIdentifier":"file://10.11588/data/TKCFEF",
                    "versionNumber":1,
                    "versionMinorNumber":0,
                    "versionState":"RELEASED",
                    "latestVersionPublishingState":"RELEASED",
                    "deaccessionLink":"",
                    "lastUpdateTime":"2022-07-25T07:10:39Z",
                    "releaseTime":"2022-07-25T07:10:39Z",
                    "createTime":"2022-07-22T10:14:58Z",
                    "publicationDate":"2022-07-25",
                    "citationDate":"2022-07-25",
                    "license":
                        {
                            "name":"Custom License",
                            #"uri":"http://creativecommons.org/licenses/by/4.0",
                            #"iconUri":"https://licensebuttons.net/l/by/4.0/88x31.png"
                        },
                    "fileAccessRequest":True,
                    "metadataBlocks":
                    {
                        "citation":
                        {
                            "displayName":"Citation Metadata",
                            "name":"citation",
                            "fields":
                            [
                                {
                                    "typeName":"title",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"Test data for the Pooch library"
                                },
                                {
                                    "typeName":"otherId",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "otherIdAgency":
                                        {
                                            "typeName":"otherIdAgency",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Zenodo"
                                        },
                                        "otherIdValue":
                                        {
                                            "typeName":"otherIdValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"10.5281/zenodo.4924875"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"author",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "authorName":
                                        {
                                            "typeName":"authorName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, Leonardo"
                                        },
                                        "authorIdentifierScheme":
                                        {
                                            "typeName":"authorIdentifierScheme",
                                            "multiple":False,
                                            "typeClass":"controlledVocabulary",
                                            "value":"ORCID"
                                        },
                                        "authorIdentifier":
                                        {
                                            "typeName":"authorIdentifier",
                                           "multiple":False,
                                           "typeClass":"primitive",
                                          "value":"0000-0001-6123-9515"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"datasetContact",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "datasetContactName":
                                        {
                                            "typeName":"datasetContactName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Kempf, Dominic"
                                        },
                                        "datasetContactAffiliation":
                                        {
                                            "typeName":"datasetContactAffiliation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Scientific Software Center, Heidelberg University"
                                        },
                                        "datasetContactEmail":
                                        {
                                            "typeName":"datasetContactEmail",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"dominic.kempf@iwr.uni-heidelberg.de"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dsDescription",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "dsDescriptionValue":
                                        {
                                            "typeName":"dsDescriptionValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"<a href=\"https://github.com/fatiando/pooch\">Pooch</a> is an open-source Python library for data download. This archive contains testing data for Pooch's DataVerse download functionality."
                                        }
                                    }]
                                },
                                {
                                    "typeName":"subject",
                                    "multiple":True,
                                    "typeClass":"controlledVocabulary",
                                    "value":
                                        [
                                        "Computer and Information Science"
                                        ]   
                                },
                                {
                                    "typeName":"publication",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "publicationCitation":
                                        {
                                            "typeName":"publicationCitation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, L., Soler, S. R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D., Banihirwe, A., & Leeman, J. (2020). Pooch: A friend to fetch your data files. Journal of Open Source Software, 5(45), 1943."
                                        },
                                        "publicationIDType":
                                        {
                                            "typeName":"publicationIDType",
                                            "multiple":False,"typeClass":"controlledVocabulary",
                                            "value":"doi"
                                        },
                                        "publicationIDNumber":
                                        {
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "typeName":"publicationIDNumber",
                                            "value":"10.21105/joss.01943"
                                        },
                                        "publicationURL":
                                        {
                                            "typeName":"publicationURL",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"https://doi.org/10.21105/joss.01943"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dateOfDeposit",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"2022-07-22"
                                },
                                {
                                    "typeName":"software",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "softwareName":
                                        {
                                            "typeName":"softwareName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Pooch"
                                        }
                                    }]
                                }
                            ]
                        },
                        "geospatial":
                        {
                            "displayName":"Geospatial Metadata",
                            "name":"geospatial",
                            "fields":
                            []
                        }
                    },
                    "files":
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
                                    "type":"MD5","value":"7008231125631739b64720d1526619ae"
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
                                    "value":"70e2afd3fd7e336ae478b1e740a5f08e"
                                },
                                "tabularData":False,
                                "creationDate":"2022-07-22",
                                "publicationDate":"2022-07-25",
                                "fileAccessRequest":True
                            }
                        }
                    ]
                }
            }
        },
         licenses = [name="Custom License"],   
    ),
    # TESTCASE 4: 1 license in API response
    (
        False,
        DataverseTestRecord.endpoints.data.response, # actual response only has one license
        licenses = [name="CC BY 4.0", uri="http://creativecommons.org/licenses/by/4.0", iconUri="https://licensebuttons.net/l/by/4.0/88x31.png"],
    )
    ]
"""
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
"""
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
    (
        False,
        {
            "status":"OK",
            "data":
            {
                "id":7131,
                "identifier":"data/TKCFEF",
                "persistentUrl":"https://doi.org/10.11588/DATA/TKCFEF",
                "protocol":"doi",
                "authority":"10.11588",
                "separator":"/",
                "publisher":"heiDATA",
                "publicationDate":"2022-07-25",
                "storageIdentifier":"file://10.11588/data/TKCFEF",
                "datasetType":"dataset",
                "latestVersion":
                {
                    "id":835,
                    "datasetId":7131,
                    "datasetPersistentId":"doi:10.11588/DATA/TKCFEF",
                    "storageIdentifier":"file://10.11588/data/TKCFEF",
                    "versionNumber":1,
                    "versionMinorNumber":0,
                    "versionState":"RELEASED",
                    "latestVersionPublishingState":"RELEASED",
                    "deaccessionLink":"",
                    "lastUpdateTime":"2022-07-25T07:10:39Z",
                    "releaseTime":"2022-07-25T07:10:39Z",
                    "createTime":"2022-07-22T10:14:58Z",
                    "publicationDate":"2022-07-25",
                    "citationDate":"2022-07-25",
                    "license":
                        {
                            "name":"CC BY 4.0",
                            "uri":"http://creativecommons.org/licenses/by/4.0",
                            "iconUri":"https://licensebuttons.net/l/by/4.0/88x31.png"
                        },
                    "fileAccessRequest":True,
                    "metadataBlocks":
                    {
                        "citation":
                        {
                            "displayName":"Citation Metadata",
                            "name":"citation",
                            "fields":
                            [
                                {
                                    "typeName":"title",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"Test data for the Pooch library"
                                },
                                {
                                    "typeName":"otherId",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "otherIdAgency":
                                        {
                                            "typeName":"otherIdAgency",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Zenodo"
                                        },
                                        "otherIdValue":
                                        {
                                            "typeName":"otherIdValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"10.5281/zenodo.4924875"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"author",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "authorName":
                                        {
                                            "typeName":"authorName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, Leonardo"
                                        },
                                        "authorIdentifierScheme":
                                        {
                                            "typeName":"authorIdentifierScheme",
                                            "multiple":False,
                                            "typeClass":"controlledVocabulary",
                                            "value":"ORCID"
                                        },
                                        "authorIdentifier":
                                        {
                                            "typeName":"authorIdentifier",
                                           "multiple":False,
                                           "typeClass":"primitive",
                                          "value":"0000-0001-6123-9515"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"datasetContact",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "datasetContactName":
                                        {
                                            "typeName":"datasetContactName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Kempf, Dominic"
                                        },
                                        "datasetContactAffiliation":
                                        {
                                            "typeName":"datasetContactAffiliation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Scientific Software Center, Heidelberg University"
                                        },
                                        "datasetContactEmail":
                                        {
                                            "typeName":"datasetContactEmail",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"dominic.kempf@iwr.uni-heidelberg.de"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dsDescription",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "dsDescriptionValue":
                                        {
                                            "typeName":"dsDescriptionValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"<a href=\"https://github.com/fatiando/pooch\">Pooch</a> is an open-source Python library for data download. This archive contains testing data for Pooch's DataVerse download functionality."
                                        }
                                    }]
                                },
                                {
                                    "typeName":"subject",
                                    "multiple":True,
                                    "typeClass":"controlledVocabulary",
                                    "value":
                                        [
                                        "Computer and Information Science"
                                        ]   
                                },
                                {
                                    "typeName":"publication",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "publicationCitation":
                                        {
                                            "typeName":"publicationCitation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, L., Soler, S. R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D., Banihirwe, A., & Leeman, J. (2020). Pooch: A friend to fetch your data files. Journal of Open Source Software, 5(45), 1943."
                                        },
                                        "publicationIDType":
                                        {
                                            "typeName":"publicationIDType",
                                            "multiple":False,"typeClass":"controlledVocabulary",
                                            "value":"doi"
                                        },
                                        "publicationIDNumber":
                                        {
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "typeName":"publicationIDNumber",
                                            "value":"10.21105/joss.01943"
                                        },
                                        "publicationURL":
                                        {
                                            "typeName":"publicationURL",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"https://doi.org/10.21105/joss.01943"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dateOfDeposit",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"2022-07-22"
                                },
                                {
                                    "typeName":"software",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "softwareName":
                                        {
                                            "typeName":"softwareName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Pooch"
                                        }
                                    }]
                                }
                            ]
                        },
                        "geospatial":
                        {
                            "displayName":"Geospatial Metadata",
                            "name":"geospatial",
                            "fields":
                            []
                        }
                    },
                    "files":
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
                                    "type":"MD5","value":"7008231125631739b64720d1526619ae"
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
                                    "value":"70e2afd3fd7e336ae478b1e740a5f08e"
                                },
                                "tabularData":False,
                                "creationDate":"2022-07-22",
                                "publicationDate":"2022-07-25",
                                "fileAccessRequest":True
                            }
                        }
                    ]
                }
            }
        },
        "store.zip","tiny-data.txt", # TODO: Handle multiple file names
        # TODO: response
    ),
    # TESTCASE 4: valid API response with invalid filename
    
    (   
        False,
        
        ValueError(f"File 'invalid_file' not found in data archive {DataverseTestRecord.archive_path} (doi:{DataverseTestRecord.doi})")  
    ),
    
]
"""
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
        {"data": []},
        {}, # registry will be empty
    ),
    
    # TESTCASE 2: malformed API response (no checksum given)
    (
      True,
        {
            "status":"OK",
            "data":
            {
                "id":7131,
                "identifier":"data/TKCFEF",
                "persistentUrl":"https://doi.org/10.11588/DATA/TKCFEF",
                "protocol":"doi",
                "authority":"10.11588",
                "separator":"/",
                "publisher":"heiDATA",
                "publicationDate":"2022-07-25",
                "storageIdentifier":"file://10.11588/data/TKCFEF",
                "datasetType":"dataset",
                "latestVersion":
                {
                    "id":835,
                    "datasetId":7131,
                    "datasetPersistentId":"doi:10.11588/DATA/TKCFEF",
                    "storageIdentifier":"file://10.11588/data/TKCFEF",
                    "versionNumber":1,
                    "versionMinorNumber":0,
                    "versionState":"RELEASED",
                    "latestVersionPublishingState":"RELEASED",
                    "deaccessionLink":"",
                    "lastUpdateTime":"2022-07-25T07:10:39Z",
                    "releaseTime":"2022-07-25T07:10:39Z",
                    "createTime":"2022-07-22T10:14:58Z",
                    "publicationDate":"2022-07-25",
                    "citationDate":"2022-07-25",
                    "license":
                        {
                            "name":"CC BY 4.0",
                            "uri":"http://creativecommons.org/licenses/by/4.0",
                            "iconUri":"https://licensebuttons.net/l/by/4.0/88x31.png"
                        },
                    "fileAccessRequest":True,
                    "metadataBlocks":
                    {
                        "citation":
                        {
                            "displayName":"Citation Metadata",
                            "name":"citation",
                            "fields":
                            [
                                {
                                    "typeName":"title",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"Test data for the Pooch library"
                                },
                                {
                                    "typeName":"otherId",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "otherIdAgency":
                                        {
                                            "typeName":"otherIdAgency",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Zenodo"
                                        },
                                        "otherIdValue":
                                        {
                                            "typeName":"otherIdValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"10.5281/zenodo.4924875"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"author",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "authorName":
                                        {
                                            "typeName":"authorName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, Leonardo"
                                        },
                                        "authorIdentifierScheme":
                                        {
                                            "typeName":"authorIdentifierScheme",
                                            "multiple":False,
                                            "typeClass":"controlledVocabulary",
                                            "value":"ORCID"
                                        },
                                        "authorIdentifier":
                                        {
                                            "typeName":"authorIdentifier",
                                           "multiple":False,
                                           "typeClass":"primitive",
                                          "value":"0000-0001-6123-9515"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"datasetContact",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "datasetContactName":
                                        {
                                            "typeName":"datasetContactName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Kempf, Dominic"
                                        },
                                        "datasetContactAffiliation":
                                        {
                                            "typeName":"datasetContactAffiliation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Scientific Software Center, Heidelberg University"
                                        },
                                        "datasetContactEmail":
                                        {
                                            "typeName":"datasetContactEmail",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"dominic.kempf@iwr.uni-heidelberg.de"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dsDescription",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "dsDescriptionValue":
                                        {
                                            "typeName":"dsDescriptionValue",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"<a href=\"https://github.com/fatiando/pooch\">Pooch</a> is an open-source Python library for data download. This archive contains testing data for Pooch's DataVerse download functionality."
                                        }
                                    }]
                                },
                                {
                                    "typeName":"subject",
                                    "multiple":True,
                                    "typeClass":"controlledVocabulary",
                                    "value":
                                        [
                                        "Computer and Information Science"
                                        ]   
                                },
                                {
                                    "typeName":"publication",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "publicationCitation":
                                        {
                                            "typeName":"publicationCitation",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Uieda, L., Soler, S. R., Rampin, R., van Kemenade, H., Turk, M., Shapero, D., Banihirwe, A., & Leeman, J. (2020). Pooch: A friend to fetch your data files. Journal of Open Source Software, 5(45), 1943."
                                        },
                                        "publicationIDType":
                                        {
                                            "typeName":"publicationIDType",
                                            "multiple":False,"typeClass":"controlledVocabulary",
                                            "value":"doi"
                                        },
                                        "publicationIDNumber":
                                        {
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "typeName":"publicationIDNumber",
                                            "value":"10.21105/joss.01943"
                                        },
                                        "publicationURL":
                                        {
                                            "typeName":"publicationURL",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"https://doi.org/10.21105/joss.01943"
                                        }
                                    }]
                                },
                                {
                                    "typeName":"dateOfDeposit",
                                    "multiple":False,
                                    "typeClass":"primitive",
                                    "value":"2022-07-22"
                                },
                                {
                                    "typeName":"software",
                                    "multiple":True,
                                    "typeClass":"compound",
                                    "value":
                                    [{
                                        "softwareName":
                                        {
                                            "typeName":"softwareName",
                                            "multiple":False,
                                            "typeClass":"primitive",
                                            "value":"Pooch"
                                        }
                                    }]
                                }
                            ]
                        },
                        "geospatial":
                        {
                            "displayName":"Geospatial Metadata",
                            "name":"geospatial",
                            "fields":
                            []
                        }
                    },
                    "files":
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
                                },
                                "tabularData":False,
                                "creationDate":"2022-07-22",
                                "publicationDate":"2022-07-25",
                                "fileAccessRequest":True
                            }
                        }
                    ]
                }
            }
        },
      KeyError("checksum"),
    ),
    # TESTCASE 3: valid API response
    (
        False, 
        DataverseTestRecord.endpoints.data.response,
        {
            "store.zip": "md5:7008231125631739b64720d1526619ae",
            "tiny-data.txt": "md5:70e2afd3fd7e336ae478b1e740a5f08e"
        },
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