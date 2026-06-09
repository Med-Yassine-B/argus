# FX Converter Lab

A growing Python project exploring currency conversion, exchange rate APIs, and financial data workflows.

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

The project currently offers an user-friendly Tkinter GUI. You can access a simple calculator, a currency converter and a trendchchart with basic metrices.

> [!NOTE]
> Implementation: `src/fx_converter_lab/gui/app.py`. See [docs/gui.md](docs/gui.md) for developer details.
>
> There is a command-line interface beside the Tkinter GUI. It's an legacy component and will depraced with the 3.Sprint. The CLI is developer-oriented and simply for debugging. You can find here the implementation: `src/legacy/cli/interface.py`

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


