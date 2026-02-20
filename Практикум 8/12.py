name = input()

if name and (name[0].isalpha() or name[0] == "_") \
   and name.replace("_","").isalnum():
    print("Является")
else:
    print("Не является")
