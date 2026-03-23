import pytest
import pandas as pd
from utils.request_util import RequestUtil

# =============================================
# 必须修改成你真实的秒杀系统地址和接口路径
# =============================================
BASE_URL = "http://127.0.0.1:8000"          # ← 如果本地跑 uvicorn，就保持这个；线上换成真实域名
ENDPOINT  = "/seckill"                      # ← 改成你实际的秒杀接口路径，例如 "/api/seckill/buy" 或 "/order/seckill"
# =============================================

req = RequestUtil(BASE_URL)

@pytest.mark.parametrize("case", pd.read_excel("data/test_data.xlsx").to_dict(orient="records"))
def test_seckill(case):
    """
    参数化测试：从 Excel 读取每行数据，发送 POST 请求到秒杀接口
    """
    print(f"\n测试用例: {case}")
    
    # 发送请求（根据你的接口调整 json 结构）
    response = req.send_request(
        method="POST",
        endpoint=ENDPOINT,
        json=case  # 直接把 Excel 一行转成 JSON body
    )
    
    print(f"响应: {response}")
    
    # 基本断言（根据你接口实际返回调整）
    assert isinstance(response, dict), "响应不是字典"
    assert "error" not in response, f"请求失败: {response.get('error')}"
    
    # 示例断言：假设成功返回 code=200 或 success=True
    success_indicators = [
        response.get("code") == 200,
        response.get("success") is True,
        "成功" in str(response).lower() or "success" in str(response).lower()
    ]
    assert any(success_indicators), f"秒杀未成功: {response}"
    
    # 可选：库存相关预警
    if "stock" in response and isinstance(response["stock"], (int, float)) and response["stock"] < 0:
        pytest.fail(f"库存异常（负值）！响应: {response}")