import random
import json

import nsq.message
from pprint import pprint

lookupd_http_addresses = ['http://127.0.0.1:4171']
nsqd_tcp_addresses = ['127.0.0.1:4172']


class Pull(object):
    def __init__(self):
        self.r_1 = nsq.Reader(
            message_handler=self.r1_handler,
            lookupd_http_addresses=lookupd_http_addresses,
            topic='test', channel="a", lookupd_poll_interval=15,
        )
        self.r_2 = nsq.Reader(
            message_handler=self.r2_handler,
            lookupd_http_addresses=lookupd_http_addresses,
            topic='test', channel="b", lookupd_poll_interval=15,
        )
        # self.r_3 = nsq.Reader(
        #     message_handler=self.r3_handler,
        #     lookupd_http_addresses=lookupd_http_addresses,
        #     topic='test', channel="c", lookupd_poll_interval=15,
        # )

    def r1_handler(self, message: nsq.message.Message):
        message.body: bytes

        j = json.loads(message.body.decode("utf-8"))
        if j["type"] == "add":
            pprint((self.r_1.channel, j))
        return True

    def r2_handler(self, message: nsq.message.Message):
        message.body: bytes

        j = json.loads(message.body.decode("utf-8"))
        if j["type"] == "add":
            pprint((self.r_2.channel, j))
            return True

    def r3_handler(self, message: nsq.message.Message):
        message.body: bytes

        j = json.loads(message.body.decode("utf-8"))
        if j["type"] == "add":
            pprint((self.r_3.channel, j))
        return True


Pull = Pull()


class Push(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    nsq.run()
