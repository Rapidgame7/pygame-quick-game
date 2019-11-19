#import math
# rawset(_G, "vWrapSuper", function(n, min, max) // Wraps around even better (?)
# 	if min > max then
# 		min,max = max,min
# 	end
# 	local dist = abs(min - max)+1
# 	while n > max do n = n - dist end
# 	while n < min do n = n + dist end
# 	return n
# end)

def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def wrap(v, minv, maxv):
    if minv > maxv: minv,maxv = maxv,minv
    dist = abs(minv - maxv)
    while v > maxv: v -= dist
    while v < minv: v += dist
    return v

def clamp(v, minv, maxv):
    if minv > maxv: minv,maxv = maxv,minv
    if v > maxv: v = maxv
    if v < minv: v = minv
    return v

def slideToZero(v, step):
    if abs(v) < step: return 0
    if v > 0:
        return v - step
    else: return v + step
