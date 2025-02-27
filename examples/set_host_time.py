#!/usr/bin/env python3
# .+
# .context    : Pyhackrf2_HTime
# .title      : Set Host Time
# .kind       : python script
# .author     : Fabrizio Pollastri <mxgbot@gmail.com>
# .site       : Revello - Italy
# .creation   : 27-Feb-2025
# .copyright  : (c) 2025 Fabrizio Pollastri
# .license    : GNU GPL v2 or higher
# .description
# Set the host time into the HackRF SDR. The host unix time
# in seconds is set into the second counter of the SDR.
# The host unix time fractional part is set into the tick
# counter of the SDR.
# .-


import pyhackrf2_htime as ph

import math as mt
import time as tm

hackrf = ph.HackRF()

# set PPS timer divisor for 10 MHz main clock
hackrf.divisor = 200000000-1

# set SDR main clock to 10 MHz
hackrf.clk_freq = 10000000

# avoid working near second transition: set a 0.15s guard around transition.
host_seconds_dec,host_seconds_int = mt.modf(tm.time())
adjust = 0.15
if host_seconds_dec > 0.14:
    adjust += 1.0
tm.sleep(adjust - host_seconds_dec)

# set host time into SDR
host_seconds_dec,host_seconds_int = mt.modf(tm.time())
hackrf.ticks = int((host_seconds_dec) * hackrf.divisor)
hackrf.seconds = int(host_seconds_int)

# check host time vs SDR time: int part of seconds must be equal,
# decimal part difference must not exceed +-0.001 s
host_seconds_dec,host_seconds_int = mt.modf(tm.time())
sdr_seconds_dec = hackrf.ticks / hackrf.divisor
sdr_seconds_int = hackrf.seconds
if host_seconds_int != sdr_seconds_int:
    print("ERROR: host(%ld) and sdr(%ld) seconds int part differ" %
        (host_seconds_int, sdr_seconds_int))
else:
    print("host and SDR seconds int part: %ld" % (host_seconds_int,))
seconds_dec_diff = host_seconds_dec - sdr_seconds_dec
if mt.fabs(seconds_dec_diff) > 0.001:
    print("ERROR: host(%lf) and sdr(%lf) secs dec part differ too much" %
        (host_seconds_dec, sdr_seconds_dec))
else:
    print("host(%lf) and sdr(%lf) secs dec part" %
        (host_seconds_dec, sdr_seconds_dec))
    print("host - SDR secs dec part: %lf" % (seconds_dec_diff,))

#### END
