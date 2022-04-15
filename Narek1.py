def avg(marks):
    assert len(marks) != 0, "The marks length is 0"
    return sum(marks)/len(marks)
mark1 = []
print("Average of mark1:",avg(mark1))