# DegreeRecognition

一个用于对原始学位数据进行正则化处理，并可视化学位分布的 Python 工具。

## 功能特点

- 从单列 Excel 文件（`.xlsx`）读取各种学位字符串。
- 将学位信息标准化为以下类别（优先级从高到低）：
  1. `PHD`（博士）
  2. `MD`（医学博士）
  3. `MASTER`（硕士）
  4. `BACHELOR`（学士）
  5. `ASSOCIATE`（副学士）
  6. `HIGH_SCHOOL`（高中及以下）
  7. 空字符串 — 未匹配到任何学位
- 输出 CSV 文件，包含原始学位文本和标准化结果。
- 生成柱状图，直观展示各学位类型的数量分布。

## 安装

1. 确保已安装 Python 3.8 及以上版本。
2. 使用 pip 安装依赖包：
   ```bash
   pip install pandas matplotlib openpyxl
   ```

## 使用说明

1. 将待处理的 Excel 文件（例如 `data.xlsx`）放在项目根目录，确保文件只有一列，且无表头。
2. 运行脚本：
   ```bash
   python DegreeRecognition.py
   ```
3. 脚本运行完毕后，会生成：
   - `result.csv`：两列数据，第一列为原始学位文本 `degree`，第二列为标准化结果 `normalized`。
   - `distribution.png`：学位分布的柱状图。

### 自定义输入/输出路径

可根据需求自行改为命令行参数传入，使用方法：
```python
from DegreeRecognition import get_result

PATH = "./data.xlsx" # 待处理数据路径
CSV_OUTPUT_PATH = "result.csv" # CSV输出路径
FIGURE_OUTPUT_PATH = "distribution.png" # 学历分布柱状图输出路径

get_result(PATH, CSV_OUTPUT_PATH, FIGURE_OUTPUT_PATH)
```

## 代码结构

- **`DegreeRecognition.py`**：主脚本文件。
  - **`DegreeLevel` 枚举**：标准化的学位名称和对应的正则表达式键值对。
  - **`normalize_degree(text)`**：匹配并返回最高优先级的学位类型。
  - **`plot_result(df, FIGURE_OUTPUT_PATH)`**：绘制并保存学位分布图。
  - **`get_result(PATH, CSV_OUTPUT_PATH, FIGURE_OUTPUT_PATH)`**：执行文件读取、正则化处理、CSV 输出和绘图。
  

## 扩展性

- 可在 `DegreeLevel` 枚举中添加新学位类别。
- 可在 `PATTERNS` 中调整或新增正则表达式，以优化识别逻辑。