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
        return f"/data/{cls.data_id}"
