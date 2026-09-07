# OpenCV 计算机视觉学习笔记

> 基于 Python + OpenCV 的计算机视觉入门学习系列，从读图、显示窗口、鼠标交互，到实时画图程序的完整实践。

## 环境要求

- Python 3.11+
- OpenCV（`opencv-python`）
- NumPy

```bash
pip install opencv-python numpy
```

## 目录结构

```
计算机视觉/
├── 1.py                     # 入门：读图 + 显示
├── leran opencv/            # 主要学习代码
│   ├── imread.py            # 读图、显示、按键保存
│   ├── win.py               # 窗口基础
│   ├── mouse.py             # 鼠标回调
│   ├── trackbar.py          # 滑动条（调色板）
│   ├── color.py             # 颜色空间转换 + 滑动条
│   ├── copy_img.py          # NumPy 拷贝 vs 引用
│   ├── testnumpy.py         # NumPy 基础（zeros、ROI 区域）
│   ├── video.py             # 摄像头读取 + 保存视频
│   ├── TASK1.PY             # ★ 综合练习：实时画图程序
│   └── 画图程序笔记.md        # 画图程序详细笔记
├── 大作业/                   # 课程大作业
└── 笔记/                    # 学习笔记
```

## 各模块说明

| 文件 | 知识点 | 说明 |
|------|--------|------|
| `1.py` | `imread` / `imshow` | 最基础的读图显示 |
| `imread.py` | `imread` / `imshow` / `imwrite` / `waitKey` | 读图、按键 `q` 退出、`s` 保存 |
| `win.py` | `namedWindow` / `resizeWindow` | 创建和调整窗口大小 |
| `mouse.py` | `setMouseCallback` | 鼠标事件回调，打印坐标 |
| `trackbar.py` | `createTrackbar` / `getTrackbarPos` | 三个滑动条调节 RGB 背景色 |
| `color.py` | `cvtColor` | 颜色空间转换（BGR→RGB/GRAY/HSV/YUV） |
| `copy_img.py` | NumPy 数组赋值 | 理解 `=` 是引用、`.copy()` 才是拷贝 |
| `testnumpy.py` | `np.zeros` / ROI 切片 | NumPy 创建矩阵、区域操作 |
| `video.py` | `VideoCapture` / `VideoWriter` | 读摄像头、旋转画面、存成 mp4 |
| `TASK1.PY` | 综合应用 | 鼠标交互 + 实时画图（见下） |

## 重点：实时画图程序 `TASK1.PY`

一个支持**按住拖动、实时预览**的小画板。

### 功能按键

| 按键 | 功能 |
|------|------|
| `l` | 画直线 |
| `c` | 画圆（按下为圆心，拖出为半径） |
| `r` | 画矩形 |
| `x` | 关闭绘图 |
| `d` | 清除画面 |
| `q` | 退出 |

### 核心设计

**1. 单一状态变量 `mode`** 表示当前模式，比多个布尔标志更清晰。

**2. `draw_shape(canvas, p1, p2, mode)` 把"画什么"和"怎么交互"分开**：

```python
def draw_shape(canvas, p1, p2, m):
    if m == 'line':
        cv2.line(canvas, p1, p2, (0, 0, 255), 2)
    elif m == 'circle':
        radius = int(np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2))
        cv2.circle(canvas, p1, radius, (255, 255, 0), 2)
    elif m == 'rect':
        cv2.rectangle(canvas, p1, p2, (0, 255, 0), 2)
```

预览和定稿复用同一段代码，加新图形只需加一个 `elif`。

**3. 实时预览靠"两张图"**：拖动时画在临时副本上，松手才落到正式画布：

```python
if drawing:
    temp = img.copy()                              # 复制干净底图
    draw_shape(temp, start_pos, cur_pos, mode)     # 画预览
    cv2.imshow('img', temp)
else:
    cv2.imshow('img', img)                         # 显示正式画布
```

**4. 鼠标事件驱动**：

| 事件 | 作用 |
|------|------|
| `EVENT_LBUTTONDOWN` | 记起点，开始拖拽 |
| `EVENT_MOUSEMOVE` | 更新当前坐标，触发预览重绘 |
| `EVENT_LBUTTONUP` | 定稿画到正式画布 |

## 学习要点总结

### 常用 API 速查

| API | 作用 |
|-----|------|
| `cv2.namedWindow(name, flag)` | 创建窗口 |
| `cv2.imshow(name, img)` | 显示图像 |
| `cv2.waitKey(ms)` | 等待按键（`0` 无限等） |
| `cv2.setMouseCallback(name, func)` | 注册鼠标回调 |
| `cv2.createTrackbar(name, win, val, max, cb)` | 创建滑动条 |
| `cv2.cvtColor(img, code)` | 颜色空间转换 |
| `cv2.line / circle / rectangle` | 画线 / 圆 / 矩形 |
| `cv2.VideoCapture(n)` | 打开摄像头 |
| `cv2.VideoWriter(...)` | 保存视频 |

### 踩坑记录

1. **Python 逻辑运算用单词**：`and` / `or` / `not`，不是 `&&` / `||` / `!`。
2. **`**` 才是幂**：`x ** 2` 是平方，`x ^ 2` 是异或。
3. **`&` 优先级高于 `==`**：`key & 0xFF == ord('q')` 等价于 `(key & 0xFF) == ord('q')`。
4. **文件名别撞标准库**：不要用 `copy.py`、`cv2.py`、`numpy.py` 等命名，会引发循环导入。
5. **代码标点用半角**：中文输入法会打出全角逗号 `，`，Python 不识别。
6. **清除画面用 `img[:] = 0`**：原地涂黑；`img = np.zeros(...)` 是重新绑定，在函数里会失效。
7. **颜色是 BGR**：`(0, 0, 255)` 是红色，不是蓝色。
8. **坐标是 `(x, y)`**：先横后纵，与 NumPy 的 `[行, 列]` 相反。
9. **`imread` 读不到返回 `None`**：后续切片操作会报 `'NoneType' object is not subscriptable`。

## 运行方式

```bash
cd "leran opencv"
python TASK1.PY
```

> 摄像头相关脚本（`video.py`）需根据本机设备编号调整 `VideoCapture` 的参数。
