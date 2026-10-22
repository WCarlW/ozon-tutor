"""
Ozon Seller API 客户端（阶段 2 启用）

出第一单后，使用此模块对接 Ozon API，自动同步订单、库存、广告数据到飞书 Base。

API 文档：https://docs.ozon.ru/global/zh-hans/api/intro/
认证方式：Client-Id + Api-Key（在 Ozon 卖家后台设置中获取）

使用前需配置环境变量：
    OZON_CLIENT_ID=your_client_id
    OZON_API_KEY=your_api_key

注意：API Key 不要写入代码或提交到 Git。
"""

import os
import requests
from typing import Optional


class OzonClient:
    """Ozon Seller API 客户端"""

    BASE_URL = "https://api-seller.ozon.ru"

    def __init__(self, client_id: Optional[str] = None, api_key: Optional[str] = None):
        self.client_id = client_id or os.getenv("OZON_CLIENT_ID")
        self.api_key = api_key or os.getenv("OZON_API_KEY")
        if not self.client_id or not self.api_key:
            raise ValueError(
                "请设置环境变量 OZON_CLIENT_ID 和 OZON_API_KEY"
            )
        self.headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key,
            "Content-Type": "application/json",
        }

    def _request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, json=data, timeout=30
        )
        response.raise_for_status()
        return response.json()

    def get_products(self, limit: int = 100) -> dict:
        """获取商品列表"""
        return self._request("POST", "/v2/product/list", {"limit": limit})

    def get_orders(self, status: str = "") -> dict:
        """获取订单列表"""
        data = {}
        if status:
            data["filter"] = {"status": status}
        return self._request("POST", "/v3/posting/fbs/list", data)

    def update_stock(self, product_id: int, stock: int) -> dict:
        """更新库存"""
        return self._request(
            "POST",
            "/v2/product/import",
            {"items": [{"product_id": product_id, "stock": stock}]},
        )


if __name__ == "__main__":
    # 测试连接（阶段 2 再运行）
    client = OzonClient()
    print("连接成功，商品数量：", len(client.get_products().get("items", [])))
