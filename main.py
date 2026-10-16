"""
Hospital Data Analysis

A Python project for cleaning, processing, analyzing, and visualizing
hospital patient data.

Developed as part of the Hyperskill (JetBrains Academy) curriculum.

The original datasets are not included in this repository.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "test"
OUTPUT_DIR = BASE_DIR / "outputs"

DATA_FILES = ["general.csv", "prenatal.csv", "sports.csv"]

COLUMNS_TO_FILL = [
    "bmi",
    "diagnosis",
    "blood_test",
    "ecg",
    "ultrasound",
    "mri",
    "xray",
    "children",
    "months",
]


def load_data():
    """Load hospital datasets from local CSV files."""

    datasets = []

    for filename in DATA_FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {filename}\n"
                "Place the required CSV files inside the 'test' directory."
            )

        datasets.append(pd.read_csv(file_path))

    return datasets


def preprocess_data(datasets):
    """Merge datasets and standardize patient information."""

    general, prenatal, sports = datasets

    prenatal = prenatal.rename(
        columns={
            "HOSPITAL": "hospital",
            "Sex": "gender",
        }
    )

    sports = sports.rename(
        columns={
            "Hospital": "hospital",
            "Male/female": "gender",
        }
    )

    data = pd.concat(
        [general, prenatal, sports],
        ignore_index=True,
    )

    data.drop(
        columns=["Unnamed: 0"],
        errors="ignore",
        inplace=True,
    )

    data.dropna(how="all", inplace=True)

    data["gender"] = data["gender"].replace(
        {
            "male": "m",
            "man": "m",
            "boy": "m",
            "female": "f",
            "woman": "f",
            "girl": "f",
        }
    )

    prenatal_mask = data["hospital"] == "prenatal"

    data.loc[prenatal_mask, "gender"] = (
        data.loc[prenatal_mask, "gender"].fillna("f")
    )

    data[COLUMNS_TO_FILL] = (
        data[COLUMNS_TO_FILL].fillna(0)
    )

    return data


def analyze_data(data):
    """Calculate descriptive statistics across hospitals."""

    hospital_counts = data["hospital"].value_counts()

    largest_hospital = hospital_counts.idxmax()

    general = data[data["hospital"] == "general"]
    sports = data[data["hospital"] == "sports"]

    stomach_share = (
        general["diagnosis"].eq("stomach").mean()
    )

    dislocation_share = (
        sports["diagnosis"].eq("dislocation").mean()
    )

    median_age_difference = (
        general["age"].median()
        - sports["age"].median()
    )

    blood_test_counts = (
        data[data["blood_test"] == "t"]
        .groupby("hospital")
        .size()
        .sort_values(ascending=False)
    )

    top_blood_test_hospital = blood_test_counts.idxmax()
    top_blood_test_count = int(blood_test_counts.max())

    print("\nHOSPITAL DATA ANALYSIS")
    print("=" * 50)

    print(f"\nDataset shape: {data.shape}")

    print("\nHospital Patient Counts:")
    print(hospital_counts)

    print("\nStatistical Results:")
    print(f"Hospital with most patients: {largest_hospital}")

    print(f"Stomach-related diagnoses: {stomach_share:.3f}")

    print(f"Dislocation-related diagnoses: {dislocation_share:.3f}")

    print(f"Median age difference: {median_age_difference:g}")

    print(
        f"Most blood tests: {top_blood_test_hospital} "
        f"({top_blood_test_count} tests)"
    )


def visualize_age_distribution(data):
    """Generate a histogram of patient ages."""

    age_bins = [0, 15, 35, 55, 70, 80]

    age_labels = [
        "0-15",
        "15-35",
        "35-55",
        "55-70",
        "70-80",
    ]

    age_groups = pd.cut(
        data["age"].dropna(),
        bins=age_bins,
        labels=age_labels,
        include_lowest=True,
        right=False,
    )

    most_common_age = age_groups.value_counts().idxmax()

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        data["age"].dropna(),
        bins=age_bins,
        color="steelblue",
        edgecolor="white",
        alpha=0.85,
    )

    ax.set_title(
        "Patient Age Distribution",
        fontsize=16,
        fontweight="bold",
    )

    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Patients")

    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "age_distribution.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)

    return most_common_age


def visualize_diagnosis_distribution(data):
    """Generate a pie chart of patient diagnoses."""

    diagnosis_counts = (
        data.loc[data["diagnosis"] != 0, "diagnosis"]
        .value_counts()
    )

    most_common_diagnosis = diagnosis_counts.idxmax()

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.pie(
        diagnosis_counts.values,
        labels=diagnosis_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white"},
    )

    ax.set_title(
        "Diagnosis Distribution Across Hospitals",
        fontsize=16,
        fontweight="bold",
    )

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "diagnosis_distribution.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)

    return most_common_diagnosis


def visualize_height_distribution(data):
    """Generate a violin plot of hospital height distributions."""

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.violinplot(
        data=data,
        x="hospital",
        y="height",
        inner="quartile",
        ax=ax,
    )

    ax.set_title(
        "Height Distribution by Hospital",
        fontsize=16,
        fontweight="bold",
    )

    ax.set_xlabel("Hospital")
    ax.set_ylabel("Recorded Height")

    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "height_distribution.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)


def generate_visualizations(data):
    """Create visualizations and summarize the findings."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    most_common_age = visualize_age_distribution(data)

    most_common_diagnosis = visualize_diagnosis_distribution(data)

    visualize_height_distribution(data)

    print("\nVisualization Results:")
    print(f"Most common age range: {most_common_age}")

    print(f"Most common diagnosis: {most_common_diagnosis}")

    print(
        "Height distribution: Differences in measurement units "
        "across hospitals create distinct peaks in the data."
    )

    print("\nVisualizations saved to:")
    print(OUTPUT_DIR)


def main():
    """Execute the hospital data analysis workflow."""

    datasets = load_data()

    data = preprocess_data(datasets)

    analyze_data(data)

    generate_visualizations(data)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
