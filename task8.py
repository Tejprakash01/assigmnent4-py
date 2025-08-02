x='output.txt'
a=input('Enter text to write:')
file=open('output.txt','w')
file.write(a)
print('Data entered successfully.')
file.close()

print('\n')

b=input('Enter additional text to append:')
file=open('output.txt','a')
file.write(b)
file.close()

print('\n')

print('Final content of',x)
file=open('output.txt','r')
print(file.readlines())
file.close()


