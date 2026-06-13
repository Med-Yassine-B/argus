# Useful metrics for the fx market

## Intro To Research

Identify simple but meaningful metrics for analyzing exchange-rate data.

It should be a beginner-friendly analytics that:

* provide useful insights
* are easy to implement in Python
* work well with charts
* as less as possible number of diffrent charts - as much as necessary for user-friendly visibility
* create a foundation for future ETL, ML and signal-generation features

---

## Overview of decided metrics for this project

### This sprint

* Daily Percentage Change
* Min/Max
* Rolling Average

### Next Sprint

* Volatility
* Strongest / Weakest Day
* Cumulative Return

---

## Core Trend Metrics (Sprint 1)

These metrics provide immediate value, are easy to understand, and work well for visualizations.

They should be implemented first.

---

### Daily Percentage Change

* **What it is**: Measures how much the exchange rate changed compared to the previous day.
* **Why it is useful**:
  * Normalizes movements across different currency pairs
  * Shows whether a currency strengthened or weakened
  * Serves as the foundation for several future metrics
* **Chart Idea**: Bar chart below the main exchange-rate chart.

```text
Positive movement → above zero
Negative movement → below zero
```

* **Priority**: Sprint 1

---

### Rolling Average (Moving Average)

* **What it is**: A moving average smooths daily fluctuations and highlights the underlying trend. It is commonly used in time-series analysis to reduce noise and reveal longer-term patterns.
* **Why it is useful**:
  * Makes trends easier to identify
  * Reduces short-term noise
  * Introduces basic time-series analysis concepts
* **Chart Idea**: Display together with the exchange-rate line.

```text
Exchange Rate
+
7-Day Rolling Average
```

* **Priority**: Sprint 1

---

### Min / Max Rate

* **What it is**: Identifies the lowest and highest exchange rate within the selected period.
* **Why it is useful**:
  * Very intuitive for users
  * Common metric in financial applications
  * Useful for understanding the range of movements
* **Chart Idea**: Show markers directly on the main chart.

```text
● Highest Rate
● Lowest Rate
```

* **Priority**: Sprint 1

---

## Recommended Sprint 1 Visualization

All Sprint 1 metrics can be displayed within a single dashboard.

### Main Chart

```text
Exchange Rate Line
+
Rolling Average Line
+
Min / Max Markers
```

### Secondary Chart

```text
Daily Percentage Change
```

---

## Movement, Performance & Risk Metrics (Sprint 2)

These metrics provide additional context about exchange-rate behavior.

They should extend the existing dashboard without adding too many separate charts.

---

### Cumulative Return

* **What it is**: Measures the total percentage change between the first and last value in the selected period.
* **Why it is useful**:
  * Shows overall performance
  * Easy for users to interpret
  * Useful for comparing periods
  * Works well as a higher-level performance metric
* **Chart Idea**:
  * Cumulative Return
  * Strongest Day Marker
  * Weakest Day Marker
* **Priority**: Sprint 2

---

### Strongest / Weakest Day

* **What it is**: Identifies the largest positive and largest negative daily percentage movement in the selected period.
* **Why it is useful**:
  * Highlights important events
  * Creates interesting insights for users
  * Easy to calculate from daily percentage change
  * Works best as markers instead of a separate chart
* **Chart Idea**:
  * Performance Chart
  * Strongest Day Marker
  * Weakest Day Marker
* **Priority**: Sprint 2

---

### Volatility (Standard Deviation)

* **What it is**: Measures how strongly exchange rates fluctuate over time. Volatility is commonly approximated using the standard deviation of returns and is one of the most widely used measures of financial risk.
* **Why it is useful**:
  * Introduces risk analysis
  * Provides a bridge toward forecasting and ML
  * Commonly used in financial analytics
  * Adds a different perspective than trend or performance metrics
* **Chart Idea**:
  * Date
  * Rolling Volatility
* **Priority**: Sprint 2

---

## Recommended Sprint 2 Visualization

Sprint 2 should extend the dashboard with one performance chart and one risk chart.

The goal is to keep the number of charts low while still making the metrics visually useful.

### Performance Chart

Contains:

* Cumulative Return
* Strongest Day Marker
* Weakest Day Marker

Why?

* Cumulative Return shows the overall movement during the selected period.
* Strongest and weakest days are events, not standalone time series.
* Showing them as markers avoids adding another unnecessary chart.

---

### Risk Chart

Contains:

* Rolling Volatility

Why?

* Volatility describes fluctuation intensity.
* It answers a different question than trend or performance.
* Keeping it separate improves readability.

---

### Resulting Sprint 2 Dashboard

#### Performance Analytics

* Cumulative Return
* Strongest Day Marker
* Weakest Day Marker

#### Risk Analytics

* Rolling Volatility

---

### Resulting Dashboard Structure

#### Trend Analytics

```text
Exchange Rate
+
Rolling Average
+
Min / Max
```

```text
Daily Percentage Change
```

This structure keeps the dashboard compact while still allowing future expansion.

## Explaination for the decision

### First Implementation

The first implementation should include:

1. Daily Percentage Change
2. Rolling Average
3. Min / Max Rate

Reasons:

* Easy to calculate with Pandas
* Easy to visualize with Plotly
* Provide immediate analytical value
* Introduce core time-series concepts
* Create a strong foundation for future metrics

### Future Direction

Potential future additions:

* Volatility
* Currency rankings
* Multi-currency comparisons
* Signal generation
* Forecasting experiments
* ML features

These features should be added only after the core analytical dashboard is completed.

## Analytics Architecture

The analytics layer should remain independent from the UI layer.

Future metrics should be implemented inside a dedicated analytics package rather than directly inside GUI code.

### Suggested Structure

```text
docs/

src/
  fx_converter_lab/
    cli/
    clients/
    gui/
    services/
    analytics/
      metrics/
      charts/
    domain/
    config.py
    main.py

tests/
```

### Responsibilities

* **analytics/metrics/**
  
  *Contains metric calculations:*

  * daily percentage change
  * rolling average
  * min / max
  * cumulative return
  * volatility
  * strongest / weakest day

* **analytics/charts/**

  *Contains chart preparation logic:*

  * trend charts
  * performance charts
  * risk charts

* **gui/**

  *Responsible only for just displaying data.*

---

### Long-Term Direction

```text
clients
↓
services
↓
analytics
  ├─ metrics
  └─ charts
↓
gui
```
