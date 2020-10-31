print('Enter the number of employee')
m=(input())
m=int(m)
file=open("filesample.txt",'r')
fout=open("output.txt","a")
line=[]
da=[]
lit=[]
str1=dict()
for data in file:
    data=data.replace('\n','')
    line.append(data)
    da=data.split(':')
    if da[1] !='':
        lit.append(int(da[1]))
        str1[lit[-1]]=da[0]
lit.sort()
temp=[]
diff=111111111
sum=0
for i in range(0,len(lit)-(m-1)):
    sum=lit[i+m-1]-lit[i]
    if diff > sum:
       diff=sum
       temp=[]
       for k in range(i,i+m):
           temp.append(lit[k])
print('Number of employees: '+ str(m))
print('\n')
fout.write('Number of employees: '+ str(m))
fout.write('\n')
print('Here the goodies that are selected for distribution are:')
for i in range(len(temp)):
    for k,v in str1.items():
        if temp[i]==k:
            print(v+": "+str(temp[i]))
            fout.write(v+": "+str(temp[i]))
            fout.write('\n')
val=temp[-1]-temp[0]

print('\n')
fout.write('\n')
print('And the difference between the chosen goodie with highest price and the lowest price is '+str(val))
fout.write('And the difference between the chosen goodie with highest price and the lowest price is '+str(val))  

fout.write
fout.close()

