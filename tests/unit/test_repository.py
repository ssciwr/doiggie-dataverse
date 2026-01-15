from unittest.mock import Mock
import pytest
from pooch_dataverse import repository
from pooch_dataverse import utils

valid_dataverse_doi: str = "doi:10.11588/data/TKCFEF/" #utils.pooch_test_dataverse_doi()
valid_dataverse_url: str = "https://dataverse.org/doi:10.11588/data/TKCFEF/" #utils.pooch_test_dataverse_url()

