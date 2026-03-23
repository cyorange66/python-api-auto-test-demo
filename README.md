# Python 接口自动化测试框架（Pytest + Requests + Allure + Pandas）

纯接口自动化测试 Demo，专注**数据驱动 + 漂亮报告 + 日志分析**。  
已覆盖80%+核心API场景，支持Excel/YAML数据驱动，生成Allure报告，Pandas自动清洗测试结果。

## 技术栈
- Python + Pytest + Requests
- Allure（美观HTML报告 + 趋势图）
- Pandas（数据处理 + 异常预警）
- YAML/Excel 数据驱动

## 项目亮点
- 数据驱动测试（Pandas读取Excel）
- Allure报告（通过率100%、饼图、趋势图）
- 日志自动化清洗（异常分钟级预警）
- 与我的高并发秒杀系统真实联调测试（见下方链接）

## 快速启动
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试
pytest --alluredir=reports

# 3. 查看漂亮报告
allure serve reports