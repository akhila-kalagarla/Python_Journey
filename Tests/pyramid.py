v = int(input().strip())
w = int(input().strip())

if w % 2 != 0 or v < 2 or v > 500 or w < 2 or w > 1000 or v > w:
    print("INVALID INPUT")
else:
    fw = (w - 2 * v) // 2
    tw = v - fw
    if fw < 0 or tw < 0:
        print("INVALID INPUT")
    else:
        print(f"TW= {tw} FW= {fw}")

