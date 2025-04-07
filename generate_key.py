from uagents.identity import create_identity

# 自动生成并保存身份到 psych_agent.key 文件
create_identity("psych_agent.key")
print("✅ 成功生成身份文件：psych_agent.key")