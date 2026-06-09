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

## Current Features

- Calculator
- Currency conversion using live exchange rates (REST API)
- Input validation and error handling
- Basic arithmetic operations (+, -, *, /, %, **)

---

## Project Structure

```text
docs/
src/ 
  fx_converter_lab/
    clients/
    gui/
    services/
    domain/
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

## Tech Stack

**Language:**

- Python

**Framework:**

- Matplotlib
- Tkinter
- Numpy
- Requests

**API:**

- REST API (ExchangeRate API)

---

## Roadmap (Sprint 1)

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

> [!WARNING]
> This roadmap is outdated. The big roadmap will come with the updates. Stay tuned!

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
