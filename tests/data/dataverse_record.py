import dataclasses


class classproperty(property):
    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


@dataclasses.dataclass
class _DataverseEndpoint:
    path: str
    response: dict


class DataverseTestRecord:
    @classproperty
    def doi(cls) -> str:
        return "10.11588/data/TKCFEF"

    @classproperty
    def data_id(cls) -> str:
        return "7131"

    @classproperty
    def archive_path(cls) -> str:
        return f"/data/{cls.data_id}" # TODO: This is correct archive_path
    
    # TODO: Add other API response -> response for single file and response for other API request
    class endpoints:
        data = _DataverseEndpoint(
            path=f"/api/datasets/:persistentId?persistentId=doi:10.11588/data/TKCFEF",
            response=[
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
                                                                [{
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
                                                                                         }}]},
                                                                 {"typeName":"author",
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
                                                                                          }}]},
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
                                                                                             }}]},
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
                                                                                     }}]},
                                                                 {
                                                                     "typeName":"subject",
                                                                     "multiple":True,
                                                                     "typeClass":"controlledVocabulary",
                                                                     "value":["Computer and Information Science"
                                                                              ]},
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
                                                                                             "typeName":"publicationIDNumber",
                                                                                             "multiple":False,
                                                                                             "typeClass":"primitive",
                                                                                             "value":"10.21105/joss.01943"
                                                                                             },
                                                                                         "publicationURL":
                                                                                             {
                                                                                                 "typeName":"publicationURL",
                                                                                                 "multiple":False,
                                                                                                 "typeClass":"primitive",
                                                                                                 "value":"https://doi.org/10.21105/joss.01943"
                                                                                                 }}]},
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
                                                                                     }}]}]},
                                                        "geospatial":
                                                            {
                                                                "displayName":"Geospatial Metadata",
                                                                "name":"geospatial",
                                                                "fields":
                                                                    []}},
                                                "files":
                                                    [{
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
                                                                    }},
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
                                                                     }}]}}}
                    ]
            )
