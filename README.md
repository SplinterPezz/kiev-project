# Kiev Dashboard Project (Abandoned)

> ⚠️ This project was started over 3 years ago and has been **left incomplete** and **not maintained since then**.

Kiev is a data aggregation and visualization dashboard aimed at monitoring various aspects of the Ukraine conflict using public data sources. The project is composed of three main parts:

- A Flask backend (`kievflask`)
- A React frontend (`kievreact`)
- A scraping and preprocessing notebook directory (`kievscrape`)

---

## 📦 Project Structure

### 1. `kievflask` (Backend - Flask API)

This folder contains a **simple backend built with Flask**, intended to expose pre-aggregated data to the frontend through a REST API.

- **Docker image:**  
  `FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7`

- **Core functionality:**
  - Aggregates data from the MongoDB database
  - Provides structured API responses using Marshmallow schemas
  - Exposes Swagger (OpenAPI) documentation via Flasgger

- **Main Python dependencies:**
  - `flask`
  - `flask_cors`
  - `flask_pymongo`
  - `flasgger`
  - `bs4` (BeautifulSoup for parsing HTML)
  - `pandas`
  - `requests`
  - `marshmallow`, `marshmallow_jsonapi`
  - `setuptools`, `livereload`, `json_util`

> Note: The backend is **not complex**, its main role is to **serve structured data** to the frontend through a set of APIs.

---

### 2. `kievreact` (Frontend - React Dashboard)

This folder includes a **React-based dashboard**, designed to display multiple charts and visualizations of the war-related data.

- **Chart components included:**
  - `TotalDeathChart`
  - `DetailDeath` (toggleable between deaths and injured via switch)
  - `TotalEquipmentChart`
  - `TotalEquipmentDeathChart`
  - `Refugees`
  - `FirePower`
  - `ArticleDeathChart`
  - `TreeTagChart`

- **Chart layout example:**
```jsx
<div className="site-layout-background px-0 px-lg-4 pt-0 pt-lg-4" style={{ padding: 24, minHeight: 360 }}>
  <TotalDeathChart />
  <Switch defaultChecked onChange={switchBarChar} style={{ marginTop: 35, marginBottom: 10, marginLeft:25 }} />
  { barCharSwitch && <DetailDeath type="death" /> }
  { !barCharSwitch && <DetailDeath type="injuried"/> }
  <TotalEquipmentChart/>
  <TotalEquipmentDeathChart/>
  <Refugees/>
  <FirePower/>
  <ArticleDeathChart />
  <TreeTagChart/>
</div>
```

- **Frontend dependencies (from `package.json`):**
```json
{
  "dependencies": {
    "@testing-library/jest-dom": "^5.15.0",
    "@testing-library/react": "^11.2.7",
    "@testing-library/user-event": "^12.8.3",
    "antd": "^4.19.2",
    "apexcharts": "^3.33.2",
    "bootstrap": "^5.1.3",
    "react": "^17.0.2",
    "react-apexcharts": "^1.4.0",
    "react-bootstrap": "^2.2.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3",
    "web-vitals": "^1.1.2"
  }
}
```
> Note: The dashboard heavily relies on charting libraries like ApexCharts and Ant Design components for layout and interactivity.


### 3. `kievscrape` (Jupyter Notebooks for Data Collection)

This folder contains a collection of Jupyter notebooks used to scrape and process data from various sources. Each notebook is focused on a specific dataset or API.

#### Included Notebooks:
- `aggregateDataTest.ipynb` — testing aggregated data processing
- `FirePower.ipynb` — working with military firepower stats
- `kaggleEquipment.ipynb` — Kaggle equipment data
- `onuData.ipynb` — refugee and civilian data from the United Nations
- `kievIndipendentAPI.ipynb` — articles and data from the Kyiv Independent API
- `refugeeData.ipynb` — data on refugee flows and counts

These notebooks were manually executed and were not integrated into a production scraping system. Many scripts likely need updates to reflect changes in data sources or formats.

---

## ⚠️ Project Status

> 🛑 **This project was started over 3 years ago and then abandoned.**  
> The codebase has not been maintained since then, and many components are likely outdated or broken due to API or library changes.  

It remains a useful snapshot of a data aggregation pipeline combining scraped and official data, but **it is not ready for use without maintenance and fixes.**

---

## 🚀 Potential Improvements (not implemented)
Here are some ideas that could modernize and improve the project if picked up again:
- Automate data collection using cron jobs or scheduled tasks (e.g., Airflow)
- Introduce error handling and type validation for incoming data
- Dockerize all components with proper health checks and volume mounts
- Set up CI/CD pipeline for deployment
- Migrate frontend to modern React versions or Vite-based tooling

---

## 📄 License

This project has no official license.  
You are free to explore and reuse the code at your own risk.

---