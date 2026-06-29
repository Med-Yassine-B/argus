from argus.domain.internal_models import DataSource,Instrument,PriceBar
from datetime import date

def test_data_source_can_be_created() -> None:
    source = DataSource(
        name="yfinance",
        provider_kind="fx_rates",
    )

    assert source.name == "yfinance"
    assert source.provider_kind == "fx_rates"
    assert source.requires_api_key is False

def test_instrument_can_be_created() -> None:
    instrument = Instrument(
        symbol="EUR/USD",
        name="Euro / US Dollar",
        asset_class="fx",
        base_currency="EUR",
        quote_currency="USD"
    )

    assert instrument.symbol == "EUR/USD"
    assert instrument.name == "Euro / US Dollar"
    assert instrument.asset_class == "fx"
    assert instrument.base_currency == "EUR"
    assert instrument.quote_currency == "USD"
    assert instrument.currency is None
    assert instrument.exchange is None

def test_price_bar_can_be_created() -> None:
    source = DataSource(
        name="yfinance",
        provider_kind="fx_rates",
    )
    instrument_rate = Instrument(
        symbol="EUR/USD",
        name="Euro / US Dollar",
        asset_class="fx",
        base_currency="EUR",
        quote_currency="USD"
    )
    pricebar = PriceBar(
        source=source,
        instrument=instrument_rate,
        timestamp=date(2026, 1, 1),
        timeframe="1D",
        close=1.89
    )

    assert pricebar.source == "yfinance"
    assert pricebar.instrument == "fx_rates"
    assert pricebar.timestamp == date(2026, 1, 1)
    assert pricebar.timeframe == "1D"
    assert pricebar.close == 1.89
    assert pricebar.open is None
    assert pricebar.high is None
    assert pricebar.low is None
    assert pricebar.adjusted_close is None
    assert pricebar.volume is None