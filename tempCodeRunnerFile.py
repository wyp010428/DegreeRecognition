import re
import warnings
import pandas as pd
from enum import StrEnum
import matplotlib.pyplot as plt


# 屏蔽 openpyxl 的警告
warnings.filterwarnings('ignore', message='Workbook contains no default style')

# 初始化标准化学位数据和正则表达式匹配表
degrees_dict = {
    "PHD": r"(ph|doctor|doctorate|dr|d\.|博)",
    "MD": r"(md|doctor of medicine|physician)",
    "MASTER": r"(master(s)?|ms(c)?|m\.s|mba|m\.|m|硕|碩)",
    "BACHELOR": r"(bachelor(s)?|ba|bs(c)?|b\.a|b\.s|b\.|b|degree|学士|本科)",
    "ASSOCIATE": r"(associate(s)?)\b",
    "HIGH_SCHOOL": r"(high school|hs diploma|diploma)",
    "NONE": r"¥",
}
for d in degrees_dict:
    degrees_dict[d] = re.compile(degrees_dict[d], re.I)