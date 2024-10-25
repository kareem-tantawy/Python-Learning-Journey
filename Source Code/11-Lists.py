# -----------
# -- Lists --
# -----------

# --------------------------------------------------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# --------------------------------------------------


MyList = ["Zero", "One", "Two", 3, 4.0, False, "One"]
print(MyList[1])
print(MyList[-2])
print(MyList[1:])
print(MyList[:5:2])
print(", ".join(MyList[0:3]))

MyList[1] = 1
print(MyList)

MyList[2:5] = ['A', 3.5, 4]
print(MyList)

MyList[0:3] = ["Kareem"]
print(MyList)
