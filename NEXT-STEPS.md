# 下一步行动清单

> 本文件交给 Ozon 导师 Agent，作为接下来工作的执行指引。

## 已完成

- [x] GitHub 仓库创建并推送所有文件：https://github.com/WCarlW/ozon-tutor
- [x] 飞书知识库结构搭建（8 个分类）：https://my.feishu.cn/wiki/Rm8fwD9n9iftgikqVEScpgcRnQd
- [x] 飞书 Base 5 张表创建完成：https://my.feishu.cn/base/JMFHbBsOlaJS4tsTomPcBp6ZnGc

## 待办（按优先级）

### P0：验证 Agent 能正常工作

1. **在 TRAE 中从 GitHub 拉取云端项目**
   - 操作：TRAE → 打开项目 → 从 GitHub 导入 `WCarlW/ozon-tutor`
   - 验证：打开项目后，确认 `.trae/rules/ozon-tutor.md` 规则已加载
   - 验证方式：问一个 Ozon 问题，看回答是否符合导师身份和第一性原则

2. **测试飞书读写能力**
   - 操作：让 Agent 读取飞书 Base「状态快照表」
   - 验证：Agent 能成功读到表内容
   - 操作：让 Agent 在「商品表」里添加你已上架的 2 款商品
   - 验证：Base 里出现 2 条商品记录

3. **初始化状态快照**
   - 操作：让 Agent 在「状态快照表」创建第一条记录
   - 内容：当前级别 = Level 1，当前阶段 = 上架，在售商品数 = 2，累计出单 = 0，当前重点任务 = "让 2 款商品出第一单"

### P1：填充知识库内容

4. **灌入 Ozon 官方文档到飞书 Wiki**
   - 来源：Ozon 官方中文文档 https://docs.ozon.ru/global/zh-hans/
   - 操作：按 Wiki 分类（01-平台规则、02-选品方法论...）把官方文档内容整理进去
   - 优先灌入：佣金与费用、物流模式(FBO/FBS/rFBS)、收款结算、违禁品
   - 要求：每篇文档标注来源链接和日期

5. **整理选品方法论**
   - 操作：在「02-选品方法论」节点写入选品基本流程和利润计算公式
   - 利润公式：到手利润 = 售价 - 佣金 - 广告费 - 物流成本(头程+尾程) - 采购成本 - 其他
   - 要求：用人民币和卢布分别标注

### P2：开始实操

6. **分析现有 2 款商品**
   - 操作：让 product-scorer 子智能体对你的 2 款商品做评估
   - 输入：品类、采购价、售价、物流成本、竞品情况
   - 输出：每款商品的判断（能做/谨慎做/别碰）+ 理由

7. **竞品拆解**
   - 操作：你在 Ozon 前台找 3 个竞品，把信息给 Agent
   - Agent 帮你拆解竞品的标题、主图、价格、评价数量
   - 输出：你的商品和竞品的差距 + 优化建议

8. **Listing 优化**
   - 操作：让 listing-optimizer 子智能体优化你的 2 款商品标题和描述
   - 输出：俄语标题 + 五点描述 + 关键词列表

### P3：出单后（达到第一单后启动）

9. **接入 Ozon API**（阶段 2）
   - 在 Ozon 后台申请 API Key
   - 配置环境变量 OZON_CLIENT_ID 和 OZON_API_KEY
   - 用 scripts/ozon_api_client.py 测试连接
   - 把订单/库存/广告数据同步到飞书 Base

## 验证标准

- P0 全部完成 = Agent 可以开始教你了
- P1 完成 = Agent 回答政策问题有据可查
- P2 完成 = 2 款商品优化到位，等待出单
- P3 完成 = 数据自动化，进入稳定运营阶段

## 重要资源链接

- GitHub 仓库：https://github.com/WCarlW/ozon-tutor
- 飞书知识库：https://my.feishu.cn/wiki/Rm8fwD9n9iftgikqVEScpgcRnQd
- 飞书 Base：https://my.feishu.cn/base/JMFHbBsOlaJS4tsTomPcBp6ZnGc
- Ozon 官方文档：https://docs.ozon.ru/global/zh-hans/
- Ozon 卖家后台：https://seller.ozon.ru/
