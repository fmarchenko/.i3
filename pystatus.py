# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}",)

status.register("xkblayout")

status.register("weather",
    location_code="RSXX1570:1:RS",
    colorize=True,
#    format="{current_temp} {current_wind}"
)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X KW%V",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eth3",
    format_up="{v4cidr}",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
# status.register("mpd",
#     format="{title}{status}{album}",
#     status={
#         "pause": "▷",
#         "play": "▶",
#         "stop": "◾",
#     },)

status.register("tcchk",
    host="mail1.100files.com", login="fmarchenko", password="KkQgH2Br"
)

status.run()
