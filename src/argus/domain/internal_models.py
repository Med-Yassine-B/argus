from dataclasses import dataclass
from datetime import datetime,date
@dataclass
class DataSource:
    name: str
    provider_kind: str
    requires_api_key: bool = False

@dataclass
class Instruments:
    symbol: str
    name: str
    assetclass: str
    currency: str
    exchange: str
    base_currency: str
    quote_currency: str

@dataclass
class PriveBars:
    timestamp: date
    timeframe: str
    open: float
    high: float
    low: float
    close: float
    adjusted_close: float
    volume: float