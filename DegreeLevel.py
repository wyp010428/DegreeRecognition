"""DegreeLevel.py

Reads a single-column Excel of raw degree strings, normalizes them to standard categories,
and writes out a CSV with original and normalized values.
Plots the distribution of normalized degrees.

Usage:
    DegreeRecognition.py 
    --python_version 3.12.9
    --input data.xlsx 
    --output result.csv 
    --plot

Requirements:
    pandas, matplotlib, openpyxl
"""

import re
# import argparse
import warnings
import pandas as pd
from enum import Enum, auto
import matplotlib.pyplot as plt


# suppress openpyxl default-style warning
warnings.filterwarnings('ignore', message='Workbook contains no default style')

class DegreeLevel(Enum):
    """Standardized education levels, ordered by priority."""
    
    PHD = auto()
    MD = auto()
    MASTER = auto()
    BACHELOR = auto()
    ASSOCIATE = auto()
    HIGH_SCHOOL = auto()
    NONE = auto()  # no degree found

    def __str__(self):
        return '' if self is DegreeLevel.NONE else self.name
    

# descending priority patterns
_PATTERNS = [
    (DegreeLevel.PHD,        re.compile(r"(ph|doctor|doctorate|dr|d\.|博)", re.I)),
    (DegreeLevel.MD,         re.compile(r"(md|doctor of medicine|physician)", re.I)),
    (DegreeLevel.MASTER,     re.compile(r"(master(s)?|ms(c)?|m\.s|mba|m\.|m|硕|碩)", re.I)),
    (DegreeLevel.BACHELOR,   re.compile(r"(bachelor(s)?|ba|bs(c)?|b\.a|b\.s|b\.|b|degree|学士|本科)", re.I)),
    (DegreeLevel.ASSOCIATE,  re.compile(r"(associate(s)?)\b", re.I)),
    (DegreeLevel.HIGH_SCHOOL,re.compile(r"(high school|hs diploma|diploma)", re.I)),
]


def normalize_degree(text: str) -> DegreeLevel:
    """Return the highest-priority DegreeLevel matching text, or NONE."""
    
    if not text or not isinstance(text, str):
        return DegreeLevel.NONE
    for level, pat in _PATTERNS:
        if pat.search(text):
            return level
    return DegreeLevel.NONE


def plot_result(df):
    counts = df['normalized'].value_counts().sort_index()
    plt.figure()
    counts.plot(kind='bar')
    plt.title('Degree Distribution')
    plt.xlabel('Degree Level')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('distribution.png')


def main():
    PATH = "./data.xlsx"
    OUTPUT_PATH = "result.csv"

    # read single-column Excel as Series
    df = pd.read_excel(PATH, header=None, dtype=str)
    df.columns = ['degree']
    df['degree'] = df['degree'].fillna('')

    # normalize
    df['normalized'] = df['degree'].apply(lambda x: str(normalize_degree(x)))

    # output CSV
    df[['degree', 'normalized']].to_csv(OUTPUT_PATH, index=False)
    
    # plot distribution
    plot_result(df)
    plt.show()


if __name__ == "__main__":
    main()