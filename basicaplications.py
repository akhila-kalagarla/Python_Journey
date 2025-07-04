a = list(map(str, input().split(" ")))
stud = ["Akhila","Sivani","pushpa","Rupa","Sravani"]
for name in a:
    if name in stud:
        print(f"{name} is present")
    else:
        print(f"{name}is absent")