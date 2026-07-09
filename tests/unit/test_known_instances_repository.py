from tests.data.dataverse_record import DataverseTestRecord
from doiggie_dataverse import KnownInstancesDataverseRepository


def test_sanity_checks(sanity_check_data_repo):
    sanity_check_data_repo(KnownInstancesDataverseRepository)


def test_initialize(known_instances_data_repo_tester):
    # TESTCASE 1: With invalid domain and invalid archive_path -> invalid archive_url
    known_instances_data_repo_tester(
        archive_base_url="https://absfaweijo.com"
    ).assert_repo_does_not_initialize(archive_path="/somevalue/abc")

    # TESTCASE 2: With invalid domain and valid archive_path -> invalid archive_url
    known_instances_data_repo_tester(
        archive_base_url="https://absfaweijo.com"
    ).assert_repo_does_not_initialize(archive_path=DataverseTestRecord.archive_path)

    # TESTCASE 3: With valid domain and invalid archive_path -> invalid archive_url
    known_instances_data_repo_tester(
        archive_base_url="https://heidata.uni-heidelberg.de"
    ).assert_repo_does_not_initialize(archive_path="/somevalue/abc")

    # TESTCASE 4: With valid domain and valid archive_path -> valid archive_url
    known_instances_data_repo_tester(
        archive_base_url="https://heidata.uni-heidelberg.de"
    ).assert_repo_does_initialize(archive_path=DataverseTestRecord.archive_path)
