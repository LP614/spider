from db import RedisClient
from crawler import Crawler

Pool_UPPER_THRESHOLD = 10000


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_thresshould(self):
        """
        判断是否达到了代理池限制
        :return:
        """
        if self.redis.count() >= Pool_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_thresshould():
            for callback_lable in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_lable]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)