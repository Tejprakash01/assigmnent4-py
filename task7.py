try:
    print('Reading file content:')
    file0='sample.txt'
    file=open('sample.txt','r')
    file1=file.readlines(1)
    file2=file.readlines(2)
    print('line1:',file1,'\nline2:',file2)
    file.close()
except FileExistsError:
    print('The file ',file0,'was not found.')



