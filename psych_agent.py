from uagents import Agent, Context
from uagents.identity import restore_identity

# 加载身份
identity = restore_identity("psych_agent.key")

# 创建心理 Agent
psych_agent = Agent(
    name="PsychAgent",
    identity=identity,
    port=8001
)

# 启动事件
@psych_agent.on_event("startup")
async def start(ctx: Context):
    ctx.logger.info("✅ 心理 Agent 启动成功")

# 接收消息
@psych_agent.on_message()
async def handle_message(ctx: Context, sender: str, msg: str):
    ctx.send(sender, f"🧠 心理建议：你提到“{msg}”，建议多倾诉、深呼吸、适度运动。")

if __name__ == "__main__":
    psych_agent.run()