## https://www.acmicpc.net/source/23215304

r, c, t = map(int, input().split())

room_given=[]
g=[]
for i in range(r):
    arr = list(map(int, input().split()))
    if arr[0]==-1:
       g.append(i) 
    room_given.append(arr)
    
def diff_center(pos_x, pos_y,room):
    return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*4

def diff_x1(pos_x,pos_y,room):
    return room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3    
    
def diff_xr(pos_x,pos_y,room):    
    return room[pos_x-1][pos_y]//5+room[pos_x][pos_y-1]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3

def diff_y1(pos_x,pos_y,room):
    return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*3

def diff_yc(pos_x,pos_y,room):
    return room[pos_x-1][pos_y]//5+room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*3

def diff_x1y1(pos_x,pos_y,room):
    return room[pos_x+1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*2

def diff_x1yc(pos_x,pos_y,room):
    return room[pos_x+1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*2

def diff_xry1(pos_x,pos_y,room):
    return room[pos_x-1][pos_y]//5+room[pos_x][pos_y+1]//5-(room[pos_x][pos_y]//5)*2

def diff_xryc(pos_x,pos_y,room):
    return room[pos_x-1][pos_y]//5+room[pos_x][pos_y-1]//5-(room[pos_x][pos_y]//5)*2


def diff(room,r,c):
    room_ins=[[0]*c for _ in range(r)]
    for ix in range(1,r-1):
        for iy in range(1,c-1):
            room_ins[ix][iy]=diff_center(ix,iy,room)
    for ix in range(1,r-1):
        room_ins[ix][0]=diff_y1(ix,0,room)
        room_ins[ix][c-1]=diff_yc(ix,c-1,room)
    for iy in range(1,c-1):
        room_ins[0][iy]=diff_x1(0,iy,room)
        room_ins[r-1][iy]=diff_xr(r-1,iy,room)
    room_ins[0][0]=diff_x1y1(0,0,room)
    room_ins[0][c-1]=diff_x1yc(0,c-1,room)
    room_ins[r-1][0]=diff_xry1(r-1,0,room)
    room_ins[r-1][c-1]=diff_xryc(r-1,c-1,room)
    
    room_ins[g[0]][0]=0
    room_ins[g[1]][0]=0
    
    room_ins[g[0]-1][0]=room[g[0]-2][0]//5+room[g[0]-1][1]//5-(room[g[0]-1][0]//5)*2
    room_ins[g[1]+1][0]=room[g[1]+2][0]//5+room[g[1]+1][1]//5-(room[g[1]+1][0]//5)*2
    room_ins[g[0]][1]=room[g[0]+1][1]//5+room[g[0]-1][1]//5+room[g[0]][2]//5-(room[g[0]][1]//5)*3
    room_ins[g[1]][1]=room[g[1]+1][1]//5+room[g[1]-1][1]//5+room[g[1]][2]//5-(room[g[1]][1]//5)*3
    
    for ix in range(r):
        for iy in range(c):
            room[ix][iy]+=room_ins[ix][iy]
    
    
    return room

def cir(room,r,c):
    for ix in range(g[0]-1,0,-1):
        room[ix][0]=room[ix-1][0]
    for iy in range(c-1):
        room[0][iy]=room[0][iy+1]
    for ix in range(g[0]):
        room[ix][c-1]=room[ix+1][c-1]
    for iy in range(c-1,1,-1):
        room[g[0]][iy]=room[g[0]][iy-1]
    room[g[0]][1]=0
    
    for ix in range(g[1]+1,r-1):
        room[ix][0]=room[ix+1][0]
    for iy in range(c-1):
        room[r-1][iy]=room[r-1][iy+1]
    for ix in range(r-1,g[1],-1):
        room[ix][c-1]=room[ix-1][c-1]
    for iy in range(c-1,1,-1):
        room[g[1]][iy]=room[g[1]][iy-1]
    room[g[1]][1]=0
    return room    
    

for _  in range(t):
    room_given=diff(room_given,r,c)
    room_given=cir(room_given,r,c)

summ=2
for ix in range(r):
    for iy in range(c):
        summ=summ+room_given[ix][iy]
    
print(summ)