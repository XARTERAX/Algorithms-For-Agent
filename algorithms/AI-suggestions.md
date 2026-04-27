
学习深度与主题（结合 DMT）——按层次：Intro / Intermediate / Applied
- Foundations (Intro, 必修)
  - Algorithm complexity & reasoning: O/Θ/Ω，简单归纳证明（repo: docs/complexity.md）
  - Arrays, Strings, Hash tables, Two pointers, Sorting, Recursion
  - 学习深度：能用笔和伪代码解释为什么复杂度成立；把每个基本题写成 problem.md + implementation。
- Core patterns (Intermediate)
  - Divide & Conquer, Binary Search, Greedy, Sliding Window, Stack/Queue, DFS/BFS
  - Dynamic Programming（状态抽象、转移、记忆化）
  - Data structures: Heap, BST, Union-Find, Trie
  - 学习深度：能从暴力推导出优化思路，能写状态转移过程并做复杂度分析。
- Media-related algorithms（Applied to DMT）
  - Signal & Transform: FFT/DFT（基础实现与理解） —— 应用于滤波、频谱分析
  - Image processing: convolution, edge detection (Sobel), Gaussian blur，图像金字塔
  - Clustering & segmentation: k-means、graph-cut（基础）、region growing
  - Compression basics: Huffman coding、run-length、简单熵概念
  - Feature extraction & retrieval: SIFT/ORB 思路、局部描述子、布隆/LSH 的近似搜索
  - 图形与几何算法：基础矩形/多边形碰撞、重心、简单光栅化思路
  - 流媒体/网络：缓冲与滑动窗口策略、简单 QoS 思路（可选）
  - 学习深度：实现可运行原型（Python+OpenCV/NumPy），理解数学背后的变换与复杂度，写实验对比（e.g., convolution vs FFT 方法时间复杂度比较）。
- Advanced / Optional（竞赛或研究方向）
  - 高级数据结构（线段树/树链剖分）、最大流/最小割、数位 DP、稀疏表
  - 机器学习相关算法（PCA、k-NN、简单神经网络原理）
  - 学习深度：理解原理，能用它们解决 DMT 的具体问题（如图像分割、内容检索）。

8 周入门到项目结合计划（示例，可根据你的时间调整）
- 预设：每周 8–12 小时（若更少，延长周数）
- Week 1: Complexity, arrays & strings 基本题（10 题），把模板文件放好，熟悉 repo 流程。
  - Repo actions: 新增 README、index、templates（已含）
  - DMT mini-project idea: write a script to read an image and compute per-channel mean/std.
- Week 2: Hash table, two-sum, sliding-window intro（5–8 题）
  - Repo: create problems/arrays、strings
- Week 3: Recursion & trees（BFS/DFS）、basic graph notions（5 题）
- Week 4: Sorting / divide & conquer / binary search（5 题）
- Week 5: Greedy & Heap / priority queue（5 题）
- Week 6: Dynamic Programming 入门（斐波那契、背包、LIS、编辑距离）（4–6 题）
- Week 7: DMT Project 1 — Image filters + convolution vs FFT comparison
  - Tasks: implement spatial convolution, use numpy.fft for convolution; measure runtime & quality.
  - Write a short report in DMT_projects/project1/README.md: algorithm choices, complexity, plots.
- Week 8: DMT Project 2 — Simple compression: implement Huffman coding for grayscale images or RLE and compare compression ratio; add tests.

优先在仓库里创建/填充的具体项（最小可行集）
1. README.md（已给模版）
2. templates/problem-template.md（已给）
3. problems/index.md：空表格，方便逐题登记（id,title,topic,difficulty,status）
4. problems/arrays/ 里填入 5 道入门题的 md（比如：two-sum, reverse-string, valid-parentheses, merge-sorted-array, binary-search），每题用模板。
5. DMT_projects/project1：image-filter demo （Jupyter notebook + scripts）
6. docs/complexity.md、docs/dmt-mapping.md（如何把算法关联到媒体技术问题）

具体 10 道初学题（可直接加入 problems/arrays, problems/strings 等）
- 0001 Two Sum
- 0002 Reverse String
- 0003 Valid Parentheses
- 0004 Merge Two Sorted Arrays
- 0005 Binary Search
- 0006 Max Subarray (Kadane)
- 0007 Move Zeroes (two pointers)
- 0008 Contains Duplicate (hash)
- 0009 Inorder/Preorder tree traversal (recursive + iterative)
- 0010 Breadth-first Search simple graph traversal

与 DMT 直接相关的 5 个小项目（可以作为 repo 中的 DMT_projects）
- Project A: Image convolution filters (box, Gaussian, Sobel) — compare direct conv vs FFT conv.
- Project B: Simple compression (RLE + Huffman) on image sequences — measure ratio & speed.
- Project C: K-means image segmentation + visualize cluster centers.
- Project D: Audio windowed FFT — visualize spectrogram, implement STFT, filter noise.
- Project E: Content-based image retrieval demo: extract simple color histogram or ORB features, do nearest neighbor search.

学习方法与“思路链”实践建议（每日练习要点）
- 每题遵循：理解→举例→暴力解→识别瓶颈→选择模式→证明/不变式→实现→复盘（写 3 行总结）。
- 对媒体算法，用小数据集做实验并记录运行时间/内存/输出质量（图像可视化）。
- 强制把每道题写入 repo，并在题目的 md 最下方写 3 行复盘：关键思路、复杂度、可改进点。

工具与环境建议
- 语言：Python（快速原型 + rich libs），C++（若想练竞赛或高性能）
- Python libs: numpy, scipy, opencv-python, matplotlib, pillow
- 环境：Jupyter Notebook（实验），pytest（单元测试）
- CI: GitHub Actions（后期配置）跑 Python tests

我需要你回复的两件事（来定制执行）
1. 你偏好哪种实现语言？（Python / C++ / Java / 多）
2. 每周能投入多少小时？（例如 6h/10h/15h）

我可以立即为你做的事（选一项）
- A. 把上面的 README、模板与 problems/index.md 生成具体文件并提供你可直接复制粘贴的内容（我已经准备好并贴在这里）。
- B. 为你在 problems/arrays 填充前 5 道题的完整 problem.md（含 pseudocode）和 Python 实现模板。
- C. 直接给出第一个 DMT 项目（Image convolution）的一份 Jupyter notebook 草稿（包含示例代码与说明）。

你选哪一项？如果选 B 或 C，请同时确认实现语言（推荐 Python）。