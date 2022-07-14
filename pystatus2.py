# -*- coding: utf-8 -*-

import os

# os.environ['HTTPS_PROXY'] = 'socks5://localhost:9050'

from i3pystatus import Status

status = Status(standalone=True, logfile='/tmp/i3pystatus.log')

status.register("clock", format=('London: %a %-d %b %X', 'Europe/London'))

# status.register('time_tracker')

status.register(
    'apploye',
    format='{current_day:.2f}|{current_week:.2f}|{previous_week:.2f}|{current_month:.2f}|{current_month_payment:.2f}',
    dashboard_id='b2483fb2-af1e-48d7-b728-0653772f4bc8',
    jwt_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOGI4MTMwZDYtOTc5ZC00YWVkLWEyNjAtNzRiYjA3YjQyYTYzIiwidXNlcm5hbWUiOiJtZnM5MEBtYWlsLnJ1IiwiZXhwIjoxNjUwOTU3NDE4LCJlbWFpbCI6Im1mczkwQG1haWwucnUifQ.nFVM144ooUof79nTOLpJ_H-nvJ7IRdbhlMW71xuZ258',
    pay_rate=25,
)

#status.register('exmo', pair='WAVES_BTC', colorize=True)
# status.register('exmo', pair='ETH_BTC', colorize=True)
status.register('exmo', pair='ETH_BTC', colorize=True)
status.register('exmo', pair='ETH_USDT', colorize=True)
status.register('exmo', pair='BTC_USDT', colorize=True)
#status.register('nicehash_speed', addr='1CZv4QT1ietU4bVXYxo1jE3cd8L9CE1JVF', format='{addr:.6}: {speed}', colorize=True,
#                color_up='#DAF7A6', color_down='#F1948A', interval=60*5, algo=22)
#status.register('nicehash_speed', addr='1Bm2RmxXDrP6qy7RbFtDDU3e989wrNbp1z', format='{addr:.6}: {speed}', colorize=True,
#                color_up='#DAF7A6', color_down='#F1948A', interval=60*10, algo=8)
# status.register('advela',
#                 api_url='http://gates.advela.ru:8080/v1/stats/?speed_interval_minutes=5',
#                 api_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImkzcHlzdGF0dXMifQ.VoRngSQOQauyW04hMHiMyL1Nuh8SaXSMxZy2kVR0BBo')
#status.register('mining', currency='ETH')
#status.register('mining', currency='ETC', wallet='0xe9429Ee564265B90e977AE4C6a000dF9eE65cEcA', balance_notyfi=0.095)

status.run()
