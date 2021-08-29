class employeea:
    nof=8
    pass
harry=employeea()
rohan=employeea()
harry.name="harry"
harry.height=150
harry.weight=66
rohan.nof=12
print(harry.__dict__)
print(rohan.__dict__ )
print(employeea.nof)
employeea.nof=14

