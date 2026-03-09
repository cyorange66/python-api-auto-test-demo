import sys
import os

# 确保脚本工作目录是项目根目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 获取 'utils' 目录的绝对路径，并确保它在 sys.path 中
utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils'))
os.environ['PYTHONPATH'] = utils_path

# 打印当前的 sys.path 和 PYTHONPATH，确保正确设置
print(f"Setting PYTHONPATH to: {utils_path}")
print(f"Current PYTHONPATH: {os.environ.get('PYTHONPATH')}")
print(f"Current sys.path: {sys.path}")

# 运行 pytest，生成 HTML 格式的报告
os.system("pytest tests --html=report/report.html")