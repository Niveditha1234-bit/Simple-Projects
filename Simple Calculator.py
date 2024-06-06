print('-----Simple Calculator-----')
print('1-Add\n2-Sub\n3-Multiply\n4-Division')
ch=int(input('Enter your choice:'))
a=int(input('Enter a:'))
b=int(input('Enter b:'))
if(ch==1):
  print('Addition->',(a+b))
elif(ch==2):
  print('Subtraction->',(a-b))
elif(ch==3):
  print('Multiplication->',(a*b))
elif(ch==4):
  print('Division->',(a/b))
