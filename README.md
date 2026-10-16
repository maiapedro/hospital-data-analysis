# Hospital Data Analysis

A Python-based data analysis project focused on data cleaning, preprocessing, statistical analysis, and visualization of hospital patient datasets.

Developed as part of the **Hyperskill (JetBrains Academy)** curriculum.

## Project Overview

This project explores patient information collected from three different hospitals: general, prenatal, and sports.

The datasets contain information about patient demographics, medical examinations, diagnoses, and other health-related variables.

The objective is to combine these datasets, improve data quality, perform exploratory data analysis (EDA), and generate visualizations to identify patterns and differences across hospitals.

## Technologies Used

- **Python** — Data processing and analysis
- **Pandas** — Data manipulation, cleaning, and statistical calculations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization

## Features

### Data Loading and Integration

- Import multiple CSV datasets using Pandas.
- Standardize inconsistent column names.
- Combine datasets using `pd.concat()`.
- Remove unnecessary index columns.

### Data Cleaning and Preprocessing

- Identify and remove empty rows.
- Handle missing values.
- Standardize categorical variables.
- Normalize gender labels.
- Prepare datasets for statistical analysis.

### Statistical Analysis

The project performs several statistical calculations, including:

- Identification of the hospital with the highest number of patients.
- Calculation of the proportion of stomach-related diagnoses.
- Calculation of the proportion of dislocation-related diagnoses.
- Comparison of median patient ages between hospitals.
- Identification of the hospital with the highest number of blood tests.

### Data Visualization

Three types of visualizations are generated:

**1. Histogram — Patient Age Distribution**

Examines the distribution of patient ages and identifies the most common age group.

**2. Pie Chart — Diagnosis Distribution**

Displays the relative frequency of medical diagnoses across hospitals.

**3. Violin Plot — Height Distribution**

Compares patient height distributions across hospitals and highlights differences in the recorded measurements.

## Project Structure

```text
hospital-data-analysis/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

The program generates an `outputs/` directory containing:

```text
outputs/
├── age_distribution.png
├── diagnosis_distribution.png
└── height_distribution.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/hospital-data-analysis.git
```

Navigate to the project directory:

```bash
cd hospital-data-analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The original datasets are not included in this repository.

To execute the program, place the required CSV files in a local `test/` directory:

```text
test/
├── general.csv
├── prenatal.csv
└── sports.csv
```

Run the analysis:

```bash
python main.py
```

The program will:

1. Load and combine the datasets.
2. Clean and preprocess patient information.
3. Calculate descriptive statistics.
4. Generate three data visualizations.
5. Save the generated charts to the `outputs/` directory.

## Skills Demonstrated

- Data Analysis
- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization
- Python Programming
- Data Manipulation with Pandas

## Dataset Availability

The datasets used in this project were provided through the Hyperskill educational platform.

They are intentionally excluded from this repository to avoid redistributing educational materials without authorization.

The project can be executed locally when the required datasets are available.

## Acknowledgments

This project was developed as part of the **Hospital Data Analysis** project on **Hyperskill (JetBrains Academy)**.

The original project concept and educational requirements were provided by Hyperskill.

This repository documents the implementation and the programming and data analysis skills practiced during the course.
