# GUI / Frontend Research for FX Converter Lab

## Goal

Evaluate possible GUI and frontend technologies for the future direction of the project.

The project is evolving from a simple currency converter into a larger financial data and analytics platform with:

* API integrations
* data processing
* ETL pipelines
* dashboards
* machine learning experiments
* Power BI connectors
* future RAG and data lake concepts

The selected UI technology should support this long-term direction without creating unnecessary complexity.

---

# GUI / Frontend Comparison

## Data & Analytics Focus

| Technology | Strengths                                                                                      | Weaknesses                                                              | Fit for Project |
| ---------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------- |
| Streamlit  | Extremely fast prototyping, very popular in Data Science, easy ML demos                        | Less flexible for larger applications, architecture can become limiting | Good            |
| Dash       | Strong analytics and dashboard ecosystem, widely used in finance and BI contexts               | More complex than Streamlit, dashboard-focused                          | Very Good       |
| Panel      | Designed for data exploration and analytical workflows, integrates well with Pandas and Plotly | Smaller community and ecosystem                                         | Very Good       |

## General Application Focus

| Technology | Strengths                                                                          | Weaknesses                                                 | Fit for Project |
| ---------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------- |
| NiceGUI    | Python-first, FastAPI-based, supports dashboards, APIs and multi-page applications | Smaller ecosystem than major frontend frameworks           | Excellent       |
| Reflex     | Modern architecture, scalable web apps                                             | More frontend complexity and abstraction                   | Good            |
| Anvil      | Fast development, many built-in features                                           | Less transparent architecture, more platform-oriented      | Medium          |
| PySide6    | Powerful desktop applications, professional UI capabilities                        | Higher learning curve, desktop-focused architecture        | Medium          |
| Tkinter    | Simple, built into Python, useful for learning GUI basics                          | Outdated for larger analytics platforms and web deployment | Low (long-term) |

---

# Tkinter Evaluation

Tkinter is suitable for:

* learning GUI fundamentals
* event handling
* desktop application basics
* small internal tools
* simple data visualization with Pandas and Matplotlib

Tkinter can support:

* CSV imports
* financial calculations
* charts
* small analytics tools

However, the project vision includes:

* dashboards
* web access
* cloud deployment
* ETL pipelines
* machine learning services
* Power BI integrations

For these goals, Tkinter becomes increasingly limiting.

Conclusion:

Tkinter is useful as a learning step and prototype phase, but should not become the long-term platform architecture.

---

# Recommended Project Structure

```text
src/
│
├─ clients/
├─ services/
├─ pipelines/
├─ analytics/
├─ ml/
├─ storage/
├─ api/
│
└─ ui/
     │
     ├─ tkinter_legacy/
     └─ nicegui/
```

Long-term direction:

```text
CLI
 ↓
Tkinter Prototype
 ↓
NiceGUI Dashboard
 ↓
Analytics Platform
 ↓
ETL + ML + Connectors
```

NiceGUI becomes the main UI layer.

Plotly, Pandas and analytics modules remain independent from the UI implementation.

---

# Recommended Technology Direction

## Primary Choice

### NiceGUI

Reasons:

* Python-first workflow
* built on FastAPI
* easy transition into APIs and web services
* suitable for dashboards and analytics tools
* supports future deployment and scaling
* aligns with data engineering and AI-oriented goals

NiceGUI is currently the best balance between:

* learning value
* development speed
* long-term scalability

## Secondary Future Addition

### Panel

Panel can later be integrated for:

* research dashboards
* advanced analytics views
* experimentation environments
* data exploration interfaces

This makes NiceGUI the platform layer and Panel the analytics layer.

---

# Concrete Next Steps

1. Finish current Tkinter prototype ticket.
2. Keep business logic separated from UI code.
3. Create a new research branch for NiceGUI exploration.
4. Build a minimal NiceGUI dashboard:

   * currency conversion
   * API request
   * result display
5. Add a simple Plotly chart.
6. Reuse existing service layer instead of rewriting logic.
7. Evaluate deployment with Docker after the first dashboard prototype.
8. Investigate Panel integration after analytics features are introduced.

---

# Final Recommendation

Use Tkinter as a temporary learning and prototype step.

Adopt NiceGUI as the primary UI architecture for future development.

Introduce Panel later if the project grows into a stronger analytics and research platform.

Avoid committing to PySide6, Reflex or Anvil for now because they provide less direct value for the project's current direction and learning goals.
