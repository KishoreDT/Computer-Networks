s,n,size,x,y = 0,4,10,4,1
for i in range(0, n): # space left
	size_left = size - s
	if x <= size_left:
		s += x
		print(f"Buffer size= {s} out of bucket size = {size}")
	else:
		print("Packet loss = ", x)
	s -= y