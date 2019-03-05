#!/usr/bin/python
import os
import sys
import time


class IPerf:

    def __init__(self, local, remote, tcp_p, udp_p, metric_name, time, bandwidth):
        self.local = local
        self.remote = remote
        self.tcp_p = tcp_p
        self.udp_p = udp_p
        self.metric_name = metric_name
        self.time = time
        self.bandwidth = bandwidth

    def command_tcp(self, time, remote):
        self = 'iperf -x CMSV -t ' + self.time + ' -y C -c ' + self.remote

    def command_udp(self, time, remote, bandwidth):
        self = 'iperf -u -x CDMS -y C -c ' + self.remote + ' -b ' + self.bandwidth