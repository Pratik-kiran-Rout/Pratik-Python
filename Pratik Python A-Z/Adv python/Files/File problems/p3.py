def Table(x):
       table =""
       for i in range(1,11):
             table += f"{x}x{i}={x*i}\n" 

       with open(f"tables/table_{x}.txt","w") as i:
            i.write(table)
      
           
for i in range (2,20+1):
    Table(i)