screen -XS host_1_lookup quit
screen -XS host_1_d quit
screen -XS host_1_admin quit

screen -XS host_2_lookup quit
screen -XS host_3_lookup quit

screen -XS host_2_d quit
screen -XS host_3_d quit

killall nsqlookupd
killall nsqd
killall nsqadmin
killall nsq_to_file
