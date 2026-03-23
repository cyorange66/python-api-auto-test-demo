# Python API Automation Test Demo
> 基于 Pytest + Requests + Pandas 的数据驱动接口自动化测试框架

---

## 🌟 项目亮点
- **数据驱动 (DDT)**：使用 Excel 存储用例，实现测试脚本与测试数据完全分离。
- **持久化连接**：封装 Requests Session，自动处理 Cookie 及 Header 传递。
- **可视化报告**：集成 Allure 报告，支持通过率统计及详细请求日志记录。
- **工程化结构**：严格的分层设计，易于维护和扩展。

---

## 📂 项目结构
```text
.
├── data/               # 测试数据 (Excel/YAML)
│   └── test_cases.xlsx # 接口测试用例集
├── report/             # 测试报告输出
│   ├── allure_results/ # Allure 原始数据
│   └── report.html    # Pytest-html 独立报告
├── tests/              # 测试脚本
│   └── test_api.py     # 核心测试逻辑 (参数化驱动)
├── utils/              # 核心组件
│   ├── __init__.py
│   └── request_util.py # Requests 请求二次封装
├── requirements.txt    # 依赖库清单
└── run_tests.py        # 脚本启动入口

类别,技术,说明
语言,Python 3.11+,核心开发语言
框架,Pytest,测试组织与断言
库,Requests,HTTP 接口请求
数据,Pandas,Excel 数据解析
报告,Allure,交互式测试报告

🚀 快速上手
1. 环境准备
Bash
# 安装依赖
pip install -r requirements.txt
2. 执行测试
Bash
# 运行并生成报告
pytest tests/test_api.py -v --alluredir=report/allure_results --html=report/report.html --self-contained-html
📊 运行效果展示
1. Allure 报告总览
report/result.png

2. 用例执行详情
展示数据驱动下，各用例的参数传递情况。

🔧 后续规划
[ ] 接入 CI/CD (GitHub Actions) 自动化执行。

[ ] 增加 JSON Schema 字段类型校验。

[ ] 支持多环境 (Dev/Test/Prod) 快速切换。