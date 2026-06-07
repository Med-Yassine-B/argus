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

## Movement & Performance Metrics (Sprint 2)

These metrics provide additional context about exchange-rate behavior.

---

### Absolute Change

* **What it is**: Measures the raw difference between two exchange-rate values.
* **Why it is useful**:
  * Easy to understand
  * Complements percentage change
  * Useful for quick comparisons
* **Chart Idea**: Additional line or metric card.
* **Priority**: Sprint 2

---

### Cumulative Return

* **What it is**: Measures the total percentage change between the first and last value in the selected period.
* **Why it is useful**:
  * Shows overall performance
  * Easy for users to interpret
  * Useful for comparing periods
* **Chart Idea**: Performance chart from a normalized starting value.
* **Priority**: Sprint 2

---

### Strongest / Weakest Movement

* **What it is**: Identifies the largest positive and largest negative daily movement.
* **Why it is useful**:
  * Highlights important events
  * Creates interesting insights for users
  * Easy to calculate
* **Chart Idea**: Top / Bottom movement table or bar chart.
* **Priority**: Sprint 2

### Volatility (Standard Deviation)

* **What it is**: Measures how strongly exchange rates fluctuate over time. Volatility is commonly approximated using the standard deviation of returns and is one of the most widely used measures of financial risk.
* **Why it is useful**:
  * Introduces risk analysis
  * Provides a bridge toward forecasting and ML
  * Commonly used in financial analytics
* **Chart Idea**: Rolling volatility chart.

```text
Date
↓
Volatility
```

* **Priority**: Sprint 2

---

## Recommended Sprint 2 Visualization

### Performance Chart

```text
Cumulative Return
+
Strongest Day Marker
+
Weakest Day Marker
```

Why?

* Cumulative Return already visualizes overall performance.
* Strongest and weakest movements are events, not standalone time series.
* Marking them on the same chart avoids creating unnecessary additional charts.

---

### Risk Chart

```text
Rolling Volatility
```

Why?

* Volatility represents a different analytical dimension.
* It focuses on risk and fluctuation intensity rather than trend or performance.
* Keeping it separate improves readability.

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

---

#### Performance Analytics

```text
Cumulative Return
+
Strongest Day
+
Weakest Day
```

---

#### Risk Analytics

```text
Rolling Volatility
```

This structure keeps the dashboard compact while still allowing future expansion.
