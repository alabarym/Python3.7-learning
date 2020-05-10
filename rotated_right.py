def rotated_right(data):
    data = data[-1::] + data[0:len(data)-1]
    return data

test1=[1,2,3]
test2="123"
test3=(1,2,3)
print (rotated_right(test3))
