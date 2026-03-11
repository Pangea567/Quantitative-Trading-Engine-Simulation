
input_file = "input.txt"
output_file = "output.txt"



folderopened = open(input_file,"r",encoding="utf-8")
information = folderopened.read()
folderopened.close()


lines = information.split("\n")

mywordlist = []
for line in lines:
    words = line.split()
    mywordlist.append(words)

print("started")

# creating my own list with while loop according to priorities
# it compares two lines and changes places of them if needed
def mylisting(fwordlist):
    lineindex = 0
    while lineindex<(len(fwordlist)-1):
        if fwordlist[lineindex][0] < fwordlist[lineindex+1][0]:                # if timestamps are increasing in time it passes those lines directly
            lineindex += 1
        
        elif fwordlist[lineindex][0] == fwordlist[lineindex+1][0]:   # if timestamps are same 
            if lineindex != 0:
                if fwordlist[lineindex-1][0] != fwordlist[lineindex][0]:
                    counter = lineindex                                    # instead of making lineindex = 0 it assings lineindex to prvious line which has a smaller timestamp
                else:
                    counter = 0           
            elif lineindex == 0:
                counter = 0

            if fwordlist[lineindex][3] != fwordlist[lineindex+1][3]:            # if it is different stock
                if fwordlist[lineindex][3]>fwordlist[lineindex+1][3]:            # it checks alfabetic order
                    fwordlist[lineindex],fwordlist[lineindex+1] = fwordlist[lineindex+1],fwordlist[lineindex]      # swaps the lines
                    lineindex = counter   
                else:
                    lineindex += 1          # if line priority is true

            elif fwordlist[lineindex][3] == fwordlist[lineindex+1][3]:            # if it is same stock and it compares sell orders , buy orders among thierselves
               
                if fwordlist[lineindex][4] == "Sell" and fwordlist[lineindex+1][4] == "Sell":            # if both are sell orders it checks which one is cheaper , cheaper one is prioritized
                    if float(fwordlist[lineindex][6]) > float(fwordlist[lineindex+1][6]):
                        fwordlist[lineindex],fwordlist[lineindex+1] = fwordlist[lineindex+1],fwordlist[lineindex]
                        lineindex = counter
                    elif fwordlist[lineindex][6] == fwordlist[lineindex+1][6]:                        # if both are sell orders and same price, smaller id is prioritized
                        if int(fwordlist[lineindex][1]) > int(fwordlist[lineindex+1][1]):
                            fwordlist[lineindex],fwordlist[lineindex+1] = fwordlist[lineindex+1],fwordlist[lineindex]
                            lineindex = counter                          
                        else:
                            lineindex+=1 
                    else:
                        lineindex+=1


                elif fwordlist[lineindex][4] == "Buy" and fwordlist[lineindex+1][4] == "Buy":            # if both are buy orders it checks which one is more expensive , more expensive one is prioritized
                    if float(fwordlist[lineindex][6]) < float(fwordlist[lineindex+1][6]):
                        fwordlist[lineindex],fwordlist[lineindex+1] = fwordlist[lineindex+1],fwordlist[lineindex]
                        lineindex = counter
                    elif fwordlist[lineindex][6] == fwordlist[lineindex+1][6]:                        # if both are buy orders and same price, smaller id is prioritized
                        if int(fwordlist[lineindex][1]) > int(fwordlist[lineindex+1][1]):
                            fwordlist[lineindex],fwordlist[lineindex+1] = fwordlist[lineindex+1],fwordlist[lineindex]
                            lineindex = counter                            
                        else:
                            lineindex += 1         # if line priority is true
                    else:
                        lineindex +=1
                
                else:
                    lineindex += 1          # if timestamp and share are the same and one of the lines is buy and the other one is sell orders it continues to next line

            else:
                break

    return fwordlist


newlist = mylisting(mywordlist)
import copy
orderlist = copy.deepcopy(newlist)

print("mylist is ready")
# İKİLİ FOR DÖNGÜSÜ YAZIP HER BUY TEKER TEKER SELL İLE EŞLEŞTİRİP STOK MİKTARLARINI DEĞİŞTİRİCEZ
# SATMA İŞİNİ YAPABİLİYOR
outputlist = []
for a in range(len(newlist)):             # one line will be buy and other one will be sell order 
    
    if "Sell" in newlist[a]:
        continue
    
    elif "Buy" in newlist[a]:
        if newlist[a][5] == 0:          # if demand becomes zero it continues to next line
            continue
        for b in range(len(newlist)):                                     # it checks if there is sell in a line 
            if newlist[a][5] == 0:          # if demand becomes zero it continues to next line
                break
            if "Sell" in newlist[b]:          # if someone sell
                if newlist[a][3] == newlist[b][3]:       # controls if it is same share     
                    if newlist[b][5] == 0:   # if no stock it continues to next line
                        continue                
                    if newlist[a][1] == newlist[b][1]:       # we need different persons   
                        continue    
                    if float(newlist[a][6]) >= float(newlist[b][6]):       # buy price need to be higher than sell price or at least same      
                        pass
                    else:
                        continue
        
                    if int(newlist[a][5]) < int(newlist[b][5]):       # if stock is higher than demand
                        
                        quantity = int(newlist[a][5])
                        productprice = float(newlist[b][6])
                        offeredprice = float(newlist[a][6])                        
                        personsellid = int(newlist[b][1])
                        personbuyid = int(newlist[a][1])

                        if newlist[a][0] > newlist[b][0]:       
                            info = newlist[a][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            pinfo = newlist[b][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                            
                            outputlist.append([f"{newlist[a][2]} bought {newlist[a][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])


                        elif newlist[a][0] < newlist[b][0]:                                 
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            pinfo = newlist[a][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                             
                            outputlist.append([f"{newlist[a][2]} bought {newlist[a][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])                    
                        
                        elif newlist[a][0] == newlist[b][0]:    
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            
                            outputlist.append([f"{newlist[a][2]} bought {newlist[a][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,year,time,info,quantity,productprice,offeredprice,personsellid,personbuyid])                             
                        
                        newlist[b][5] = int(newlist[b][5]) - int(newlist[a][5])    #  stock will decrease and demand will be zero
                        newlist[a][5] = 0 

                    elif int(newlist[a][5]) > int(newlist[b][5]):       # if demand is higher
                        
                        quantity = int(newlist[b][5])
                        productprice = float(newlist[b][6])
                        offeredprice = float(newlist[a][6])
                        personsellid = int(newlist[b][1])
                        personbuyid = int(newlist[a][1])

                        if newlist[a][0] > newlist[b][0]:       
                            info = newlist[a][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")                    
                            pinfo = newlist[b][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                             
                            outputlist.append([f"{newlist[a][2]} bought {newlist[b][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])
                        
                        elif newlist[a][0] < newlist[b][0]:      
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            pinfo = newlist[a][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                             
                            outputlist.append([f"{newlist[a][2]} bought {newlist[b][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])                    
                        
                        elif newlist[a][0] == newlist[b][0]:        
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            outputlist.append([f"{newlist[a][2]} bought {newlist[b][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,year,time,info,quantity,productprice,offeredprice,personsellid,personbuyid])                         
                        
                        newlist[a][5] = int(newlist[a][5]) - int(newlist[b][5])    # demand will be drop and stock will be decreased
                        newlist[b][5] = 0

                    elif int(newlist[a][5]) == int(newlist[b][5]):       # if stock and demand quantity are same    
                        
                        quantity = int(newlist[a][5])
                        productprice = float(newlist[b][6])
                        offeredprice = float(newlist[a][6])                        
                        personsellid = int(newlist[b][1])
                        personbuyid = int(newlist[a][1])

                        if newlist[a][0] > newlist[b][0]:        # from matching time the later time will be process time or we can say bought time 
                            info = newlist[a][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")                      
                            pinfo = newlist[b][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                             
                            outputlist.append([f"{newlist[a][2]} bought {newlist[a][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])
                        
                        elif newlist[a][0] < newlist[b][0]:        # from matching time the later time will be process time or we can say bought time 
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            pinfo = newlist[a][0]
                            pyear = pinfo[0:10]
                            ptime = pinfo[11:].replace("-",":")                             
                            outputlist.append([f"{newlist[a][2]} bought {newlist[b][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,pyear,ptime,info,quantity,productprice,offeredprice,personsellid,personbuyid])                    
                        
                        elif newlist[a][0] == newlist[b][0]:        # if match timestamp is same , timestamp date is known already
                            info = newlist[b][0]
                            year = info[0:10]
                            time = info[11:].replace("-",":")
                            outputlist.append([f"{newlist[a][2]} bought {newlist[b][5]} {newlist[a][3]} for {newlist[b][6]} USD from {newlist[b][2]} on {year} at {time}",year,time,year,time,info,quantity,productprice,offeredprice,personsellid,personbuyid])
                       
                        newlist[b][5] = 0 
                        newlist[a][5] = 0
print(outputlist)


# (sentence,year1,time1,year2,time2,totalinfo,quantity,productprice,offeredprice,personsellid,personbuyid)


#A GOOD WAY FOR LİSTİNG OUTPUT

def sort_key(line):
    return (line[1], line[2], line[3], line[4])

outputlist.sort(key=sort_key)


def total_executed_volume(time):     # YYYY-MM-DD-hh-mm-ss sum of the procceses up to that time
    totalvolume = 0
    for row in range(len(outputlist)):
        if outputlist[row][5] <= time:
            totalvolume += outputlist[row][6] * float(outputlist[row][7])         # quantity times price
    
    return round(totalvolume)    


def executed_user_volume(user_id,time):
    totalforone = 0
    for row in range(len(outputlist)):
        if outputlist[row][5] <= time:        # earlier time than given time or sam
            if int(outputlist[row][10]) == user_id:      # if user bought it 
                totalforone += outputlist[row][6] * float(outputlist[row][7])
            elif int(outputlist[row][9]) == user_id:      # if user sold it
                totalforone += outputlist[row][6] * float(outputlist[row][7])
            else:
                continue
    return round(totalforone)            


# orderlist a deepcopy of ordered list according to priorities

def total_remaining_volume(time):
    total = 0 
    soldvolume = 0 
    boughtvolume = 0
    totalremaining = 0
    for row1 in range(len(orderlist)):
        if orderlist[row1][0] <= time:
            total += int(orderlist[row1][5]) * float(orderlist[row1][6])       # quantity times price
   
    for row2 in range(len(outputlist)):
        if outputlist[row2][5] <= time:
            boughtvolume += int(outputlist[row2][6]) * float(outputlist[row2][8])    # to subtract it from total execution by all 
            soldvolume += int(outputlist[row2][6]) * float(outputlist[row2][7])
    totalremaining = total - soldvolume - boughtvolume
    return round(totalremaining)
    


def remainig_user_volume(user_id,time):
    total = 0 
    soldvolume = 0 
    boughtvolume = 0
    totalremaining = 0
    for row1 in range(len(orderlist)):
        if orderlist[row1][0] <= time:     
            if int(orderlist[row1][1]) == user_id:    
                total += int(orderlist[row1][5]) * float(orderlist[row1][6])       # quantity times price
    
    for row2 in range(len(outputlist)):
        if outputlist[row2][5] <= time:    
            if int(outputlist[row2][10]) == user_id:       # if user bought
                boughtvolume += int(outputlist[row2][6]) * float(outputlist[row2][8])    # to subtract it from total execution by one 
            
            elif int(outputlist[row2][9]) == user_id:      # if user sold
                soldvolume += int(outputlist[row2][6]) * float(outputlist[row2][7])

    
    totalremaining = total - soldvolume - boughtvolume
    
    return round(totalremaining)



answer = open(output_file,"w", encoding="utf-8")
for line in range(len(outputlist)):
    result = outputlist[line][0]
    answer.write(f"{result}\n")
answer.close()
