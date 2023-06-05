LOG_LEVEL = 'WARNING'  # 日志的输出等级，不想看那么多日志信息就可以写成WARNING

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'  # 把自己伪装成浏览器

ROBOTSTXT_OBEY = False  # 不遵从机器人协议

# 把注释去掉就行
ITEM_PIPELINES = {
    'erShouFang.pipelines.ErshoufangPipeline': 300,
}
