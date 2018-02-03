
# -*- coding: utf-8 -*-
import urllib2


class HTMLDownloader(object):

    def download(self, url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
