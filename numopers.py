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

def wrap(v, minv, maxv):
    if minv > maxv: minv,maxv = maxv,minv
    dist = abs(minv - maxv)
    while v > maxv: v -= dist
    while v < minv: v += dist
    return v
