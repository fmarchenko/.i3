# -*- coding: utf-8 -*-

from i3pystatus import Status

status = Status(standalone=True, logfile='/tmp/i3pystatus.log')

status.register('time_tracker')

#status.register('exmo', pair='WAVES_BTC', colorize=True)
# status.register('exmo', pair='ETH_BTC', colorize=True)
status.register('exmo', pair='ETH_USD', colorize=True)
status.register('exmo', pair='BTC_USD', colorize=True)
status.register('nicehash_speed', addr='1CZv4QT1ietU4bVXYxo1jE3cd8L9CE1JVF', format='{addr:.6}: {speed}', colorize=True,
                color_up='#DAF7A6', color_down='#C70039')
status.register('nicehash_speed', addr='1Bm2RmxXDrP6qy7RbFtDDU3e989wrNbp1z', format='{addr:.6}: {speed}', colorize=True,
                color_up='#DAF7A6', color_down='#C70039')

status.run()
