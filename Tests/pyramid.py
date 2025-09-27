# To find the width of the two sections of a pyramid given the total width and the width of the vertical section
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


# To find the difference between the count of '*' and '#' in the given string
s = input().strip()
count_star = s.count('*')
count_hash = s.count('#')
print(count_star - count_hash)


# To find the number of Sundays in the given number of days starting from a specific day
start_day = input().strip().lower()
n = int(input().strip())
days_map = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6
}
start_index = days_map[start_day]
sundays = n // 7
if (start_index + (n % 7) - 1) >= 6:  
    sundays += 1
print(sundays)