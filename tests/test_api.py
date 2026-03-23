import pytest
import pandas as pd
from utils.request_util import RequestUtil

# 实例化请求工具
req = RequestUtil("https://httpbin.org")

# 动态读取 Excel 数据
def get_test_data():
    return pd.read_excel("data/test_cases.xlsx").to_dict("records")

@pytest.mark.parametrize("row", get_test_data())
def test_interface(row):
    method = row["method"]
    endpoint = row["endpoint"]
    
    # 根据方法决定是否传 body
    payload = {"test": "data"} if method == "POST" else None
    
    response = req.request(method, endpoint, json=payload)
    
    # 打印调试信息
    print(f"\n[Case {row['case_id']}] 执行 {method} {endpoint}")
    
    # 断言逻辑：httpbin 返回的 json 里必然包含 url 字段
    assert "url" in response, f"测试失败，响应内容为: {response}"