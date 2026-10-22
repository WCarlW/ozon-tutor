"""
ROI 计算器（阶段 2 启用）

自动计算 Ozon 商品的 ROI 和利润率。
利润 = 售价 - 采购成本 - 物流成本 - 佣金 - 广告费 - 其他费用
"""

from dataclasses import dataclass


@dataclass
class ProductCost:
    sale_price: float        # 售价（卢布）
    purchase_cost: float     # 采购成本（人民币）
    logistics_cost: float    # 物流成本（人民币）
    commission_rate: float   # 佣金率（如 0.15 表示 15%）
    ad_cost: float = 0.0     # 广告费（卢布）
    other_cost: float = 0.0  # 其他费用（人民币）
    exchange_rate: float = 13.0  # 卢布兑人民币汇率


def calculate_profit(cost: ProductCost) -> dict:
    """计算单品利润"""
    revenue_rub = cost.sale_price
    commission = revenue_rub * cost.commission_rate
    net_revenue_rub = revenue_rub - commission - cost.ad_cost
    net_revenue_cny = net_revenue_rub / cost.exchange_rate
    total_cost_cny = cost.purchase_cost + cost.logistics_cost + cost.other_cost
    profit_cny = net_revenue_cny - total_cost_cny
    profit_margin = profit_cny / (revenue_rub / cost.exchange_rate) if revenue_rub else 0

    return {
        "net_revenue_cny": round(net_revenue_cny, 2),
        "total_cost_cny": round(total_cost_cny, 2),
        "profit_cny": round(profit_cny, 2),
        "profit_margin": round(profit_margin, 4),
    }


if __name__ == "__main__":
    # 示例：售价 1000 卢布，采购 20 元，物流 15 元，佣金 15%
    cost = ProductCost(
        sale_price=1000,
        purchase_cost=20,
        logistics_cost=15,
        commission_rate=0.15,
    )
    result = calculate_profit(cost)
    print("单品利润分析：")
    for k, v in result.items():
        print(f"  {k}: {v}")
