import RPi.GPIO as sa
sa.setmode(sa.BOARD)
sa.setwarnings(False)
sa.setup(3,sa.IN)
sa.setup(5,sa.IN)
sa.setup(11,sa.OUT)
ir1=3
ir2=5
lights=11
count=0


while 1:
    while(sa.input(ir1)==1):
        while((sa.input(ir1)==1) & (sa.input(ir2)==0)):
            while((sa.input(ir1)==1) & (sa.input(ir2)==1)):
                while((sa.input(ir1)==0) & (sa.input(ir2)==1)):
                    while((sa.input(ir1)==0) & (sa.input(ir2)==0)):
                        count=count+1
                        break
           
    while(sa.input(ir2)==1):
        while((sa.input(ir2)==1) & (sa.input(ir1)==0)):
            while((sa.input(ir2)==1) & (sa.input(ir1)==1)):
                while((sa.input(ir2)==0) & (sa.input(ir1)==1)):
                    while((sa.input(ir2)==0) & (sa.input(ir1)==0)):
                        count=count-1
                        break
    print ("count= ",count)
    if(count>0):
        sa.output(11,1)
    else:
        sa.output(11,0)


'''
rs=3
rw=5
en=7

d1=11
d2=12
d3=13
d4=15
d5=18
d6=19
d7=21
d8=22

pin=[rs,rw,en,d1,d2,d3,d4,d5,d6,d7,d8]

for i in string(0,len(pin)):
        xyz.setup(pin[i],xyz.OUT)

def lcd_pinData(data):          #To get ASCII values
        j=1
        for a in range(0,7):
                print ("k=",k)
                if(x & a == a):         # Anding operation to do masking
                        xyz.output(pin[a],1)
                else:
                        xyz.output(pin[a],0)
                k=k*2
                print ("a=",a)
def lcd_data(value):
        xyz.output(rs,1)
        xyz.output(rw,0)
        xyz.output(en,1)
        print ("value=", value)
        print (type(value))
        if(type(value)==str):
                print("ValueStr=",value)
                lcd_pinData(ord(value))
        else:
                print("else")
                lcd_pinData(value)
        time.sleep(0.001)
        xyz.output(en,0)

def lcd_cmd(com):
        lcd_pinData(com)
        xyz.output(rs,0)
        xyz.output(rw,0)
        xyz.output(en,1)
        time.sleep(0.001)
        xyz.output(en,0)

def lcd_init():
        lcd_cmd(0x02)
        lcd_cmd(0x38)
        lcd_cmd(0x0C)
        lcd_cmd(0x06)

def lcd_stmt(disp):
        for i in disp:
                print("i=",i)
                lcd_data(i)

def lcd_num(num):
        lcd_cmd(0x04)
        if(num==0):
                lcd_data(num)
        while(num>0):
                d=num%10
                num=num/10
                lcd_data(d+48)
        lcd_cmd(0x06)

lcd_init()
lcd_cmd(0x80)
lcd_stmt("Count= ",count)
'''
