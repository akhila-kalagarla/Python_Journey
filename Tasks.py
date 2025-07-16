#Task 1 :- 16/07/2025
'''Convert to Uppercase'''
a = "Akhila"
print(a.upper()) # AKHILA
print(a.lower()) # akhila
a = "akhila"
print(a.capitalize()) # Akhila
a = " akhila kalagarla "
print(a.title()) # Akhila Kalagarla
print(a.count("a")) # 6
print(a.replace("kalagarla", "akki")) # akhila akki
print(a.startswith("akhi")) # True
print(a.endswith("garla")) # True
print(a.find("kalagarla")) # 8
print(a.strip()) # akhila kalagarla
a = "Akhila"
k = "-"
print(k.join(a)) # A-k-h-i-l-a
print(a.center(20,"*")) # *******Akhila*******
print(a.ljust(10,"-")) # Akhila----
print(a.rjust(30,"+")) # ++++++++++++++++++++++++Akhila
