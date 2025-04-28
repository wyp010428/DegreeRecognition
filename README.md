# 学位识别

DegreeRecognition.py

**输入数据：**数据中的学历学位一项，填写了各种数据，将数据正则化成：

PHD，MD，MASTER，BACHELOR，ASSOCIATE，HIGH_SCHOOL, 没有找到学位（在输出数据中为空字符串），并绘制学历分布图像。

**输入数据示例：**

<img src="/Users/wangyupeng/Library/Application Support/typora-user-images/image-20250428161505167.png" alt="image-20250428161505167" style="zoom:50%;" />

**输出数据：**正则化后的CSV文件。

**输出数据示例：**

<img src="/Users/wangyupeng/Library/Application Support/typora-user-images/image-20250428161544566.png" alt="image-20250428161544566" style="zoom:50%;" />

**输出图片示例：**

<img src="/Users/wangyupeng/Downloads/DegreeRecognition/distribution.png" alt="distribution" style="zoom:72%;" />

**使用方法：**

```python
from DegreeRecognition import get_result

PATH = "./data.xlsx" # 待处理数据路径
CSV_OUTPUT_PATH = "result.csv" # CSV输出路径
FIGURE_OUTPUT_PATH = "distribution.png" # 学历分布柱状图输出路径

get_result(PATH, CSV_OUTPUT_PATH, FIGURE_OUTPUT_PATH)
```
