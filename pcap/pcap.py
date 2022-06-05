# convert base64 to pcap

import base64, struct, sys

base64_str = 'ABDzlg8ZomR3AABEgQAAUQgARQAAQJj6QAA2BusgW1yFIawUNAuINgBQllBGbW9o2QawEAH2yloAAAEBCAqXjD1ra4QuYwEBBQpvaNwpb2jcKg==';


payload = 'F4EuBNCpXkZcfnkbvn46uXqRQh1KiS0a16NSYW6dB7dOk/xgFYDufdaB4var8Xr/7aG2lfEDJLrMjmf5XNO31Tr3V29gVLHxmc4M0ApSmaTwJ4K/UaamIkhQpCljC5vHvpztVPdyHq7T/WDeLdA88106Is0VUYmP3MvukrF4IAHV3Kz/sr9xxzmXFp4yC9FHkcqk6fhNm1gtjn0VQag4BVqkn3FS7h0tbZiJN9xw7Bk1dihUOray1TMTY4n3rkZmEDKXZJM8Xyua+yeKN+uG6KKyGyC7iE06cP0Daunl7kmf+HdJsN7fALjW9hozEUpozLPb5+sNJEL1jz8fIzQ+1Cl3g9cgOSnj6esBuHrfMHjNjKHu7SLijtibsyM79mx5UANhG/ro/lOV0Kk4Rzb8l9CS75nqjuL8f27hZYd+rHQTKKWJOuYJbqbo+cuUI3G+/K8jJp1ZMlnpnVDobBDR5HvcTNMIXW3L2cxOcc4H5j8mw1kvxf0aBecP88WFBuz+QED1/ut+ai6LMenKqscE23bEmZmN3UY7okEs2iasTIT7Ox+VmMz9xSbgYvHrP2somr0ZMXchtkslpQzNODEFe6YLeHDTU7hEx/iAEYRW7R01jeQa4fBx0jJrTOLpVV0pItbEK0vMaEpmUT5vpG/FCBsgvxUdSnhHu9J5mfLpEO2xA7tfezgT878Z6YiiMgAozMsVfAom4oJsChhY2eFfgZjEVxgjHod/idVsI3HM2jZPi3pgOH5q9C5w0ycJ4B7/cp6y5Yte1ypdEVLH45zO2UYSPPhpC/2y0N6qD4ecleJ1nAr7svPWAanntNF0Npr5ZdbCDycb317J9TOB4kqDs2Z2ex63OORyrTFFj0BkHS9NxHZms06Z7i1oz4oBt6xA448oQF644C5opQ8QfPL9MXaSdnb84eFOdbd/stcLt2gNnoqVO/hbeJ7bBWHVTv5cGpoPTqpUe7MXB7WfVa4YgK+ntkzUv9+54iXqx8+NBoedvyHi03mKuHeXSBQ1SHNzUl0C5kGutvHvdpn5jNVSkmlXMlgF75M/YEWU03VqIRUKZU95KIOnborXU6S63V72m68Y6Mfdopp1/BctshT95z403LN/evswQF6sf48Ri5c+2C1mfrQ8baTyuwBN2280iic72zQP6FRJ0Dyg8YeFaO4WbtU1i0xNnQxaG9MHYprxgI2+YHkBeJ+RPxsnrzxHX+pNJdXWA/8mtWvd9pxCqxZgy0yY8yCFyGlEFwMDBZAAAAAAAAApne+6yUiyNDKktHL6tI9EQeRy/pcumS+A/9S03zCVJBHx7SnGDHue5xP8GNutKSeFvwN2HrPca80weHToawkAW6MR33jVnSGgzPoY0TRFhU96bKGFzZng1A0NRoBvYRTNTC/RY3aty9nB9KX+5w1iyjTquP8Vl0yZHpl0mQG5yfQu9wYP8qMeb5jqi/WRN2Ruk3oywt9Nd7m67kS6kBI06hN6f469d8LUCK7ZOt1UR7GtKmYDcq59twNIZcOxyir0YTgoTKPWlB8eLMs66Rf5eD3o/lwpgHSRG7FqLzZw5+X1Z1gdHMuUgDBjW9peW58vFGjCRgNgV3UVoPBM1mldmMdYFAP40FFt3hUBtmwOwV9KaZ6o91NaJeFzAMgtKC9ya9452I/Tg7QQy7hE8FIKAflB+aJW3iXWuHuRDBEsIIFwYhgZmG4bbfi7XL/uA+ftqrhIAvciXEkt/P/uM7NgijyzDWkb/ck/wtIWEOZvlahEKHO0tDfBJ7YchTxkdp/ERGGC5VNRZ4llAMlQG+cls7TVliM/4o8vmD0Qxr/FidG8';

binary = base64.standard_b64decode(base64_str);

listbyte = list(binary);


#encoding = 'utf-8';
#str = binary.decode(encoding);

#print(str);

hexval = binary.hex('-');
#print(type(hexval))
print('\n');
#print((hexval))
#print('\n');
#print(listbyte)
#print('\n');
#print(hex(listbyte[0]))
print('\n');
values = hexval.split('-');

#print((values))
#print( '{:08x}'.format(2003) )

line = 0;

bytes_val = line.to_bytes(2, 'big')
hexval_line = bytes_val.hex();

f = open("text-decod.txt", "a")
f.write(hexval_line);
f.write('   ');
i = 0;
for k in range(len(values)):
    if i <= 16 :
        f.write(values[k] + ' ');
        #print(values[k] + ' ');
        i = i + 1;
    if i == 16 :
        i = 0;
        line = line + 16
        f.write('\n')
        bytes_val = line.to_bytes(2, 'big')
        hexval_line = bytes_val.hex();
        f.write(hexval_line);
        f.write('   ');
        #print('\n');
    
f.close()    
     
        

'''

pack1 = struct.pack("IHHIIII", 
                            0xa1b2c3d4,  # Magic
                            2,           # Major
                            4,           # Minor
                            0,           # This zone
                            0,           # Sigfigs
                            0xffffffff,  # Snaplen
                            1            # DataLink type (Ethernet)
);

pack2 =  struct.pack("IIII",
                            0,           # Timestamp seconds
                            0,           # Timestamp microseconds
                            len(binary), # Length of packet in file
                            len(binary)  # Original length of packet
)
        
        
#print(pack2);


#File header
sys.stdout.write(struct.pack("IHHIIII", 
                    0xa1b2c3d4,  # Magic
                    2,           # Major
                    4,           # Minor
                    0,           # This zone
                    0,           # Sigfigs
                    0xffffffff,  # Snaplen
                    1            # DataLink type (Ethernet)
))

#Record header
sys.stdout.write(struct.pack("IIII",
                    0,           # Timestamp seconds
                    0,           # Timestamp microseconds
                    len(binary), # Length of packet in file
                    len(binary)  # Original length of packet
))

#Record data
sys.stdout.write(binary)

#f = open("text-decod.txt", "a")
#f.write(binary)
#f.close()

#print(binary);

'''
