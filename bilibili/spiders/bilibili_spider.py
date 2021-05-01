# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import logging
from scrapy.exceptions import CloseSpider
from bilibili.items import BiliBiliData
import json

logger = logging.getLogger(__name__)
class BilibiliSpiderSpider(RedisSpider):
    name = 'bilibili_spider'
    allowed_domains = ['bilibili.com']
    # 启动爬虫的命令
    redis_key = "bilibili_spider:start_urls"

    def parse(self, response):
        try:
            # 若settings中HTTPERROR_ALLOW_ALL = True，则需检测状态吗
            if response.status not in [200, 301, 302, 303, 307]:
                raise CloseSpider("网址:%s 状态码异常:%s" % (response.url, response.status))
        except CloseSpider as error:
            logger.error(error)
        else:
            try:
                # 解析json数据
                json_data = json.loads(response.text)
            except Exception as error:
                # 若解析错误，记录url
                json_data = {"code": 403}
                logger.error((response.url, error))
                with open("./error_json.txt", "a") as fb:
                    fb.write(response.url)
                    fb.write("\n")

            item = BiliBiliData()
            if json_data["code"] == 0:
                # 解析json数据，存入item对象
                data = json_data["data"]
                # print(data)调试查看json数据格式
                item['aid'] = data.get("aid")
                item['pubdate'] = data.get("pubdate")
                item['view'] = data.get("stat").get("view")
                item['like'] = data.get("stat").get("like")
                item['danmaku'] = data.get("stat").get("danmaku")
                item['reply'] = data.get("stat").get("reply")
                item['favorite'] = data.get("stat").get("favorite")
                item['coin'] = data.get("stat").get("coin")
                item['share'] = data.get("stat").get("share")
                yield item

        # 因logging等级设为了WARNING，则在log中增加一条完成记录
        logger.warning("完成:[%s]" % response.url)

