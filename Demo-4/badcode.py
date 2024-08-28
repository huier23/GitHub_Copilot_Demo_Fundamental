import time

def target():
    a = 2024
    b = 12
    c = 31
    d = 23
    e = 59
    f = 59
    return time.mktime((a, b, c, d, e, f, 0, 0, 0))

def rem(tt):
    ct = time.time()
    rt = int(tt - ct)
    if rt <= 0:
        return 0
    else:
        return rt

def ft(rt):
    d, rm = divmod(rt, 86400)
    aa, rm = divmod(rm, 3600)
    cc, ddd = divmod(rm, 60)
    return f"{d}  {aa}  {cc}  {ddd} "

def cd():
    tt = target()
    while True:
        rt = rem(tt)
        if rt == 0:
            print("End")
            break
        res = ft(rt)
        print(res)
        time.sleep(1)

cd()