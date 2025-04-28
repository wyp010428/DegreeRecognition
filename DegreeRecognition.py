"""DegreeRecognition.py

读取单列Excel学位数据，将数据正则化成标准的学位信息，
包含：PHD，MD，MASTER，BACHELOR，ASSOCIATE，HIGH_SCHOOL, 没有找到学位（空字符串）
并将转换结果输出为CSV文件，包含原始学位信息和正则化后的结果
并将转换后的结果分布画图表示

Example:
    Bachelor's degree -> BACHELOR

Requirements: pandas, matplotlib, openpyxl

-- python_version  3.12.9
-- input           data.xlsx 
-- output          result.csv 
-- plot            distribution.png
"""

import re
import warnings
import pandas as pd
from enum import Enum, auto
import matplotlib.pyplot as plt


# 屏蔽 openpyxl 的警告
warnings.filterwarnings('ignore', message='Workbook contains no default style')

# 所有标准化的学位名称及其正则表达式
degrees = {
    'PHD': re.compile(r"(ph|doctor|doctorate|dr|d\.|博)", re.I),
    'MD': re.compile(r"(md|doctor of medicine|physician)", re.I),
    'MASTER': re.compile(r"(master(s)?|ms(c)?|m\.s|mba|m\.|m|硕|碩)", re.I),
    'BACHELOR': re.compile(r"(bachelor(s)?|ba|bs(c)?|b\.a|b\.s|b\.|b|degree|学士|本科)", re.I),
    'ASSOCIATE': re.compile(r"(associate(s)?)\b", re.I),
    'HIGH_SCHOOL': re.compile(r"(high school|hs diploma|diploma)", re.I),
    'NONE': re.compile(""),
}

# 根据学位的类型生成 DegreeLevel 类，并绑定 __str__ 方法
def _degreelevel_str(self):
    return '' if self is DegreeLevel.NONE else self.name

DegreeLevel = Enum('DegreeLevel', [(name, auto()) for name in degrees])
DegreeLevel.__str__ = _degreelevel_str


def normalize_degree(text: str) -> DegreeLevel:
    """返回最高的学位类型，或者返回 DegreeLevel.NONE 类型"""

    # text不合法时返回 DegreeLevel.NONE
    if not text or not isinstance(text, str):
        return DegreeLevel.NONE

    # text匹配成功返回正则化后的名称
    for level, pat in zip(DegreeLevel, degrees.values()):
        if pat.search(text):
            return level

    # 无匹配则返回 DegreeLevel.NONE
    return DegreeLevel.NONE


def plot_result(df, FIGURE_OUTPUT_PATH):
    """绘制学历分布柱状图"""

    counts = df['normalized'].value_counts().sort_index()
    plt.figure()
    counts.index = counts.index.map(lambda x: 'NO MATCH' if x == '' else x)
    counts.plot(kind='bar')
    plt.title('Degree Distribution')
    plt.xlabel('Degree Level')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(FIGURE_OUTPUT_PATH)
    plt.show()


def get_result(PATH, CSV_OUTPUT_PATH, FIGURE_OUTPUT_PATH):
    """接受待处理文件路径和输出路径，输出正则化后的CSV文件到指定路径，并绘制图像到指定路径"""

    # 读取单列Excel文件
    df = pd.read_excel(PATH, header=None, dtype=str)
    df.columns = ['degree']
    df['degree'] = df['degree'].fillna('')

    # 对学位正则化匹配
    df['normalized'] = df['degree'].apply(lambda x: str(normalize_degree(x)))

    # 输出CSV文件
    df[['degree', 'normalized']].to_csv(CSV_OUTPUT_PATH, index=False)

    # 绘制学位分布图
    plot_result(df, FIGURE_OUTPUT_PATH)


if __name__ == "__main__":
    PATH = "./data.xlsx"
    OUTPUT_PATH = "result.csv"
    FIGURE_OUTPUT_PATH = "distribution.png"
    get_result(PATH, OUTPUT_PATH, FIGURE_OUTPUT_PATH)
