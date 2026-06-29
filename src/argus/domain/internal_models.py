from dataclasses import dataclass


@dataclass
class DataSource:
    name: str
    provider_kind: str
    requires_api_key: bool = False