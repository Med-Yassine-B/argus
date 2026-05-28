# FX Converter Lab

A growing Python project exploring currency conversion, exchange rate APIs, and financial data workflows.

---

## Current Features

- Calculator (GUI and CLI)
- Currency conversion using live exchange rates (REST API)
- Input validation and error handling
- Basic arithmetic operations (+, -, *, /, %, **)

---

## Project Structure

```text
docs/
src/ 
  fx_converter_lab/
    cli/
    clients/
    gui/
    services/
    domain/
    config.py
    main.py
tests/
pyproject.toml
README.md
```

## User Interfaces

The project exposes two interfaces:

- **GUI:** A user-friendly Tkinter desktop app providing Calculator and Currency Converter modes. Implementation: `src/fx_converter_lab/gui/app.py`. See [docs/gui.md](docs/gui.md) for developer details.
- **CLI:** A command-line interface for faster, developer-oriented interaction with the same features (`src/fx_converter_lab/cli/interface.py`). The CLI is useful for development and quick testing but is not a separate dev tool yet.

---

## Tech Stack

- Python
- REST API (ExchangeRate API)
- requests

---

## Roadmap

### Phase 1 (current)

- CLI calculator
- API integration
- basic currency conversion

### Phase 2

- improve conversion logic
- better structure (modules, separation)
- error handling & validation

### Phase 3

- visualization (matplotlib / plotly)
- historical exchange rates
- data analysis features

### Phase 4 (vision)

- web interface (JS / frontend)
- integration with Excel / Power BI
- cloud-based data processing

---

## Goal

This project is not just a calculator.

It is a learning environment to understand:

- API integration
- data processing
- system design
- building useful tools step by step

## Status

Currently under active development.
