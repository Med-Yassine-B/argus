# ARGUS Storage Research

## Goal

Research what ARGUS should store and which database/storage approach fits the project.

ARGUS is moving from live API requests and in-memory analytics toward real data workflows.  
The first storage decision should support local market analytics, SQL practice and future dashboard features without adding unnecessary infrastructure too early.

---

## Storage Use Cases

ARGUS should eventually store different kinds of data, but not all of them need to be implemented at once.

Relevant storage use cases are:

* historical exchange rates
* cleaned historical market data
* source information
* instruments that ARGUS can analyze
* later watchlists
* later generated reports
* later macroeconomic data
* later paper-trading history

The first implementation should focus on historical market data and the basic entities needed to query it.

---

## Storage Candidates

| Option | Best Use Case | Strengths | Limitations | Fit for ARGUS |
|---|---|---|---|---|
| SQLite | Small local app storage | Very simple, serverless, good for settings and watchlists | Less analytics-focused | Good later for app-state, not first choice |
| DuckDB | Local analytical storage | SQL-based, local, strong for analytical queries, good with Python/notebooks | Not a server database | Best first choice |
| PostgreSQL | Server/product database | Strong relational database, good for web apps, users, reports and cloud setups | More setup and infrastructure | Very good later |
| Parquet | Export/archive format | Efficient columnar format for analytical data | Not a database by itself | Useful later, not first storage layer |

---

## Local, Server and Cloud Options

| Option | Meaning | Fit Now | Fit Later |
|---|---|---:|---:|
| Local storage | Database or files run locally in the project | High | High |
| Server database | Database runs as a separate service, e.g. PostgreSQL | Medium | High |
| Cloud storage/database | Managed storage or database in the cloud | Low | High |

ARGUS should start with local storage.

Reason:

* simpler setup
* easier learning curve
* good fit for a Python analytics project
* no cloud or server infrastructure required yet
* enough for historical data, metrics and dashboard development

Server and cloud storage should come later when ARGUS has stronger product features such as reports, user state, paper-trading history or deployment needs.

---

## Recommended Decision

DuckDB should be the first storage technology for ARGUS.

Why:

* ARGUS currently needs local analytical storage
* DuckDB is designed for analytical SQL workflows
* it does not require a database server
* it works well with Python and notebook-based exploration
* it fits historical time-series and market-data analysis
* it keeps the first implementation manageable

PostgreSQL should be introduced later when ARGUS moves toward a more product-like architecture.

SQLGate should also be kept for that later PostgreSQL phase, not for the first DuckDB phase.

---

## First Data Model Direction

The first data model should support FX data now and broader market data later.

ARGUS should not use a narrow `date | value` table as the main market-data model.

That would work for simple exchange rates, but it would become limiting once ARGUS adds stocks, ETFs, indices or broader market APIs.

The first model should focus on three tables:

```text
data_sources
instruments
price_bars
```
