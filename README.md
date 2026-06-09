# ARGUS

**Automated Research & Guidance Utility for Signals**
ARGUS is a Python-based market analytics project evolving from a small FX converter into a broader data-oriented platform for exchange rates, market data, analytics, dashboards, and future AI-assisted monitoring workflows.

> [!NOTE]
> This project started as **FX Converter Lab** and is being renamed to **ARGUS** as the scope grows beyond simple currency conversion.

ARGUS is currently focused on building a clean local foundation:

- currency conversion using live exchange-rate data
- calculator and conversion logic
- input validation and error handling
- Tkinter GUI prototype
- legacy CLI/debug interface
- first pandas/matplotlib-based analytics prototype
- tests and documentation

> [!IMPORTANT]
> ARGUS is not a finished trading tool or financial advisor.  
> It is a portfolio and learning project for building reliable data, analytics, visualization and future automation workflows.

---

## Project Direction

ARGUS is designed to grow step by step from a local Python application into a market analytics and monitoring system.

The long-term direction includes:

- market data ingestion
- historical FX and market data analysis
- reusable analytics and metric layers
- dashboards and visualizations
- local and cloud-based storage
- data quality checks
- reporting workflows
- future AI-assisted research and agentic monitoring

> [!TIP]
> The goal is to keep each development step usable and testable instead of building a large system all at once.

---

## Current Features

- Calculator
- Currency conversion using live exchange rates
- Input validation and error handling
- Tkinter GUI prototype
- Legacy CLI/debug interface
- Basic pandas-based trend metrics
- Matplotlib-based trend visualization
- Mock time-series data for early analytics development
- Basic test suite

> [!CAUTION]
> Historical market data support is still limited.  
> The current live exchange-rate client is useful for simple conversion, but future analytics work will require additional data sources such as Frankfurter or yfinance.

---

## Project Structure

```text
docs/
src/
  fx_converter_lab/
    analytics/
      charts/
      metrics/
    clients/
    domain/
    gui/
    services/
    config.py
    main.py
  legacy/
    cli/
tests/
pyproject.toml
README.md
```

## User Interface

The project currently offers a user-friendly Tkinter GUI. You can access a simple calculator, a currency converter and a trend chart with basic metrics.

> [!NOTE]
> Implementation: `src/fx_converter_lab/gui/app.py`. See [docs/gui.md](docs/gui.md) for developer details.
>
> A command-line interface still exists as a legacy component for local debugging and quick checks.
> It is no longer the main user-facing interface and is expected to be deprecated around Sprint 3.
> Implementation: `src/legacy/cli/interface.py`.

---

## Current Tech Stack

### Language

- Python 3.11+

### Core libraries

- requests
- python-dotenv
- pandas
- NumPy
- matplotlib
- Tkinter
- pytest

### Current data source

- ExchangeRate API for live currency conversion

---

## Planned / Future Tech Stack

ARGUS is expected to grow into a broader data and analytics system.

Planned or likely future technologies include:

### Data sources

- Frankfurter API for historical FX data
- yfinance for broader market data
- possible additional market-data APIs later

### Data processing

- pandas
- NumPy
- possibly Polars later for larger datasets

### Storage

- PostgreSQL
- DuckDB
- Parquet
- optional cloud storage

### Visualization and UI

- matplotlib
- Plotly
- NiceGUI

### DevOps and deployment

- GitHub Actions
- Docker
- Docker Compose
- cloud deployment later

### Cloud and data engineering

- Azure, GCP or AWS depending on project direction
- scheduled ingestion
- data quality checks
- reporting pipelines

### AI and agentic workflows

- LLM-assisted summaries
- RAG over stored reports or notes
- agentic data checks
- anomaly monitoring
- human-in-the-loop signal review

> [!CAUTION]
> AI and agentic features are future-stage ideas.  
> They should only be added after the data, storage, service and reporting layers are stable.

---

## Setup

Clone the repository:

```bash
git clone https://github.com/BytecodeBrewer/fx-converter-lab.git
cd fx-converter-lab
---
Create a virtual environment:
python -m venv .venv

## Status

ARGUS is under active development.

The project is currently transitioning from a small FX converter into a broader market analytics platform.

Current focus:

- finish Sprint 1 foundation
- prepare first public release
- improve README and project documentation
- keep the application runnable and testable
- prepare the next analytics and data-source expansion
