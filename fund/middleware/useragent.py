# -*- coding: utf-8 -*-

from random import choice

from fund.useragents import USER_AGENT_LIST

def get_user_agent(spider):
    if hasattr(spider, 'user_agent'):
        return spider.user_agent
    return choice(USER_AGENT_LIST)

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = get_user_agent(spider)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
