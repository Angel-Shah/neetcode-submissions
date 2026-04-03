# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # result = []
        visited = set()
        queue = deque()
        hostname = startUrl.split('/')[2]
        queue.append(startUrl)
        # result.append(startUrl)
        visited.add(startUrl)
        while queue:
            toParse = queue.popleft()
            newLinks = htmlParser.getUrls(toParse)
            for link in newLinks:
                if link not in visited:
                    currHostName = link.split('/')[2]
                    if currHostName == hostname:
                        queue.append(link)
                        visited.add(link)
        return list(visited)