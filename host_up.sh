screen -dmS host_1_lookup bash -c 'nsqlookupd -http-address=0.0.0.0:4161 -tcp-address=0.0.0.0:4160'
screen -dmS host_1_d bash -c 'nsqd --lookupd-tcp-address=127.0.0.1:4160 --lookupd-tcp-address=127.0.0.1:4170 --lookupd-tcp-address=127.0.0.1:4180 -tcp-address=0.0.0.0:4162 -http-address=0.0.0.0:4163 -data-path=host_1'
screen -dmS host_1_admin bash -c 'nsqadmin --lookupd-http-address=127.0.0.1:4161 -http-address=0.0.0.0:4164'

screen -dmS host_2_lookup bash -c 'nsqlookupd -http-address "0.0.0.0:4171" -tcp-address "0.0.0.0:4170"'
screen -dmS host_2_d bash -c 'nsqd --lookupd-tcp-address=127.0.0.1:4170 -tcp-address=0.0.0.0:4172 -http-address=0.0.0.0:4173 -data-path=host_2'
screen -dmS host_2_to_file bash -c 'nsq_to_file --topic=test --output-dir=host_2 --lookupd-http-address=127.0.0.1:4171'


screen -dmS host_3_lookup bash -c 'nsqlookupd -http-address "0.0.0.0:4181" -tcp-address "0.0.0.0:4180"'
screen -dmS host_3_d bash -c 'nsqd --lookupd-tcp-address=127.0.0.1:4180 -tcp-address=0.0.0.0:4182 -http-address=0.0.0.0:4183 -data-path=host_3'
screen -dmS host_3_to_file bash -c 'nsq_to_file --topic=test --output-dir=host_3 --lookupd-http-address=127.0.0.1:4181'


