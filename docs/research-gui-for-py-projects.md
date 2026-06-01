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

The research is not only about choosing a GUI framework.  
It is also about choosing an application direction that can grow from a local learning project into a small financial data and analytics platform.

---

# GUI / Frontend Comparison

## Data & Analytics Focus

| Technology | Strengths | Weaknesses | Fit for Project |
| ---------- | --------- | ---------- | --------------- |
| Streamlit | Extremely fast prototyping, very popular in Data Science, easy ML and data app demos | Less flexible for larger application structures, architecture can become limiting | Good |
| Dash | Strong analytics and dashboard ecosystem, widely used for analytical web apps and finance/BI-style dashboards | More complex than Streamlit, dashboard-focused, less suitable as the whole application platform | Very Good |
| Panel | Designed for data exploration and analytical workflows, integrates well with the PyData ecosystem, supports dashboards and complex applications | Smaller community and ecosystem than Streamlit/Dash | Very Good |

## General Application Focus

| Technology | Strengths | Weaknesses | Fit for Project |
| ---------- | --------- | ---------- | --------------- |
| NiceGUI | Python-first, browser-based UI, FastAPI-based, supports dashboards, APIs, routing and multi-page applications | Smaller ecosystem than major frontend frameworks | Excellent |
| Reflex | Modern architecture, scalable web apps | More frontend complexity and abstraction | Good |
| Anvil | Fast development, many built-in features | Less transparent architecture, more platform-oriented | Medium |
| PySide6 | Powerful desktop applications, professional UI capabilities | Higher learning curve, desktop-focused architecture, less aligned with web/dashboard/cloud direction | Good technically, Medium strategically |
| Tkinter | Simple, built into Python, useful for learning GUI basics | Outdated for larger analytics platforms and web deployment | Learning phase only |

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

Tkinter should be finished for the current GUI prototype ticket, but future UI development should move toward NiceGUI.

---

# PySide6 Evaluation

PySide6 is a strong option for professional desktop applications.

It is technically more powerful than Tkinter and suitable for serious desktop software with:

* advanced widgets
* complex layouts
* professional desktop UI patterns
* larger local applications

However, PySide6 introduces a different type of complexity:

* Qt concepts
* signals and slots
* widget hierarchies
* layout management
* desktop-specific UI architecture

This is not necessarily too difficult, but it would cost additional learning time.

For this project, the main direction is not desktop software engineering.  
The project is moving toward data engineering, analytics, dashboards, APIs, ETL, ML and future cloud deployment.

Conclusion:

PySide6 is technically strong, but not the best strategic next step for this project right now.

NiceGUI fits the project direction better because it connects UI work with web apps, dashboards, APIs and future deployment.

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