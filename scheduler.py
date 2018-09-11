import random
def schedule():
    
    seen={}
    counts={'a':[0,0],'b':[0,0],'c':[0,0],'d':[0,0],'e':[0,0],'f':[0,0],'g':[0,0],'h':[0,0],'i':[0,0],'j':[0,0]}
    ##schedule
    week_dict={}
    check=2
    ##rivals
    riv=[['a','b'],['c','d'],['e','f'],['g','h'],['i','j']]
    for week in range(1,13):
        print(week)
        teams=['a','b','c','d','e','f','g','h','i','j']
        matchups=[]
        if week==12:
            seen_here=[]
            for team1 in teams:
                for team2 in teams:
                    if team1==team2:
                        continue
                    else:
                        game=sorted([team1,team2])
                        
                        if str(game[0])+str(game[1]) not in seen:
                            if game not in riv:
                                if game not in seen_here:
                                    print('match')
                                    print(game)
                                    matchups.append(team1)
                                    matchups.append(team2)
                                    seen_here.append(game)               
        else:
            proceed=False
            c=0
            while proceed is False:
                c+=1
                if c>10000:
                    print('broke')
                    return
                matchups=[]
                tseen=[]
                for t in range(0,10):
                    r=random.randint(0, len(teams)-1)
                    while r in tseen:
                        r=random.randint(0, len(teams)-1)
                    matchups.append(teams[r])
                    tseen.append(r)
                nogo=False
                tc=0
                for m in range(0,5):
                    game=sorted([matchups[2*m],matchups[(2*m)+1]])
                    if str(game[0])+str(game[1]) in seen:
                        if seen[str(game[0])+str(game[1])]==1:
                            if counts[str(game[0])][0]==4:
                                nogo=True
                            elif counts[str(game[1])][0]==4:
                                nogo=True
                    else:
                        if counts[str(game[0])][1]==4:
                            nogo=True
                        elif counts[str(game[1])][1]==4:
                            nogo=True
                            
                    if game in riv:
                        nogo=True
                    if str(game[0])+str(game[1]) in seen:
                        if seen[str(game[0])+str(game[1])]==2:
                            nogo=True
                    if week>1:
                        if game in week_dict[week-1]:
                            nogo=True
                    
                if nogo==False:
                    proceed=True
                            
                    
        
        for m in range(0,5):
            game=sorted([matchups[2*m],matchups[(2*m)+1]])
            if str(game[0])+str(game[1]) in seen:
                seen[str(game[0])+str(game[1])]+=1
                counts[str(game[0])][0]+=1
                counts[str(game[1])][0]+=1
                counts[str(game[0])][1]-=1
                counts[str(game[1])][1]-=1
                
            else:
                seen[str(game[0])+str(game[1])]=1
                counts[str(game[0])][1]+=1
                counts[str(game[1])][1]+=1
            if week not in week_dict:
                week_dict[week]=[game]
            else:
                week_dict[week].append(game)
    return([week_dict,seen,counts])
        

def var_to_name():
    d={1: [['c', 'h'], ['g', 'i'], ['e', 'j'], ['b', 'f'], ['a', 'd']], 2: [['a', 'g'], ['h', 'i'], ['d', 'f'], ['b', 'j'], ['c', 'e']], 3: [['b', 'f'], ['a', 'c'], ['h', 'j'], ['e', 'i'], ['d', 'g']], 4: [['d', 'h'], ['b', 'c'], ['f', 'j'], ['a', 'i'], ['e', 'g']], 5: [['c', 'h'], ['b', 'j'], ['a', 'g'], ['d', 'f'], ['e', 'i']], 6: [['a', 'f'], ['d', 'h'], ['c', 'j'], ['b', 'i'], ['e', 'g']], 7: [['f', 'j'], ['h', 'i'], ['c', 'e'], ['a', 'd'], ['b', 'g']], 8: [['b', 'i'], ['a', 'c'], ['f', 'h'], ['d', 'e'], ['g', 'j']], 9: [['h', 'j'], ['b', 'e'], ['d', 'g'], ['a', 'f'], ['c', 'i']], 10: [['a', 'j'], ['b', 'd'], ['c', 'f'], ['e', 'h'], ['g', 'i']], 11: [['a', 'h'], ['e', 'j'], ['f', 'g'], ['d', 'i'], ['b', 'c']], 12: [['a', 'e'], ['b', 'h'], ['c', 'g'], ['d', 'j'], ['f', 'i']]}
    name_dict={'a':'Bensky','b':'Pink','c':'Tenner','d':'Theo','e':'Minster','f':'Shanus','g':'Sam','h':'LangWin','i':'Fish','j':'Eli'}
    home_d={'a':[0,0],'b':[0,0],'c':[0,0],'d':[0,0],'e':[0,0],'f':[0,0],'g':[0,0],'h':[0,0],'i':[0,0],'j':[0,0]}
    for week in d.keys():
        print('Week '+str(week))
        g=0
        for game in range(len(d[week])):
            g+=1
            team1=list(d[week][game])[0]
            team2=list(d[week][game])[1]
            r=random.randint(0, 1)
            if home_d[team1][0]<home_d[team2][0]:
                print('Game '+str(g) +': '+str(name_dict[team2])+' at '+str(name_dict[team1]))
                home_d[team1][0]+=1
            elif home_d[team2][0]<home_d[team1][0]:
                print('Game '+str(g) +': '+str(name_dict[team1])+' at '+str(name_dict[team2]))
                home_d[team2][0]+=1
            else:
                if r==0:
                    print('Game '+str(g) +': '+str(name_dict[team2])+' at '+str(name_dict[team1]))
                    home_d[team1][0]+=1
                else:
                    print('Game '+str(g) +': '+str(name_dict[team1])+' at '+str(name_dict[team2]))
                    home_d[team2][0]+=1
    return(home_d)
            
            
