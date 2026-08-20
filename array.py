import array

a=array.array('i',[10,20,30])
print(a)

print(a.buffer_info())

a.insert(2,4)
print(a)

b=array.array('f',[10.2,20.3,30])
print(b)

c = array.array('h', [10, 20, 30])
c.byteswap()
print(c)

a =array.array('d', [10.5, 20.5])
b = array.array('d', [30.5, 40.5])
a.extend(b)
print(a)




a = array.array('f', [10.5, 20.5, 30.5])

a.insert(1, 15.5)
a.reverse()


print(a)

a = array.array('q', [100000, 200000, 300000])

x = a.pop()

print("Removed:", x)
print(a)

a = array.array('H')

a.fromlist([10, 20, 30, 40])

print(a)
