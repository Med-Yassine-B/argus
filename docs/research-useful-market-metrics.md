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