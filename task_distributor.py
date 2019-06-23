import time
import sys
import json
import random
import uuid

import nsq
import tornado.ioloop

i = 0


def pub_message():
    global i
    i += 1

    writer.pub(
        topic='test',
        msg=bytes(json.dumps(dict(
            type="add",
            uuid=str(uuid.uuid4()),
            num_a=random.choice(range(100)),
            num_b=random.choice(range(100)),
        )), encoding="utf-8"),
        callback=finish_pub,
    )
    if i == 10:
        sys.exit(0)


def finish_pub(conn, data):
    print(conn, data)


writer = nsq.Writer(nsqd_tcp_addresses=['127.0.0.1:4162'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
