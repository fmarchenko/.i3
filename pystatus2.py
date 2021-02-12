# -*- coding: utf-8 -*-

import os

os.environ['HTTPS_PROXY'] = 'socks5://localhost:9050'

from i3pystatus import Status

status = Status(standalone=True, logfile='/tmp/i3pystatus.log')

status.register('time_tracker')

status.register("clock", format=('London: %a %-d %b %X', 'Europe/London'))

#status.register('exmo', pair='WAVES_BTC', colorize=True)
# status.register('exmo', pair='ETH_BTC', colorize=True)
status.register('exmo', pair='ETH_USD', colorize=True)
status.register('exmo', pair='BTC_USD', colorize=True)
#status.register('nicehash_speed', addr='1CZv4QT1ietU4bVXYxo1jE3cd8L9CE1JVF', format='{addr:.6}: {speed}', colorize=True,
#                color_up='#DAF7A6', color_down='#F1948A', interval=60*5, algo=22)
#status.register('nicehash_speed', addr='1Bm2RmxXDrP6qy7RbFtDDU3e989wrNbp1z', format='{addr:.6}: {speed}', colorize=True,
#                color_up='#DAF7A6', color_down='#F1948A', interval=60*10, algo=8)
status.register('advela',
                api_url='http://gates.advela.ru:8080/v1/stats/?speed_interval_minutes=5',
                api_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImkzcHlzdGF0dXMifQ.VoRngSQOQauyW04hMHiMyL1Nuh8SaXSMxZy2kVR0BBo')

status.run()
