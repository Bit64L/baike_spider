# -*- coding: utf-8 -*-
from baike_spider import url_manager, HTML_downloader, HTML_parser, HTML_outputer


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = HTML_downloader.HTMLDownloader()
        self.parser = HTML_parser.HTMLParser()
        self.outputer = HTML_outputer.HTMLOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                html_count = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count > 50:
                    break
                count = count + 1
            except Exception as e:
                print(str(e))
                # 根据报错信息提示错误

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
