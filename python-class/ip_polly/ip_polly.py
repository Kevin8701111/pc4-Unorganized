import os
import re

first = ''
second = ''
ip_polly_add = 0
while True:
    try:
        ip_start = input("請輸入開始IP ")

        ip_start_checkS = ip_start.split('.')
        ip_polly_S0 = int(ip_start_checkS[0])
        ip_polly_S1 = int(ip_start_checkS[1])
        ip_polly_S2 = int(ip_start_checkS[2])
        ip_polly_S3 = int(ip_start_checkS[3])
        print("start :" + ip_start)

        ip_end = input("請輸入結束IP ")

        ip_end_checkE = ip_end.split('.')
        ip_polly_E0 = int(ip_end_checkE[0])
        ip_polly_E1 = int(ip_end_checkE[1])
        ip_polly_E2 = int(ip_end_checkE[2])
        ip_polly_E3 = int(ip_end_checkE[3])
        print("end :" + ip_end)

    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

if ip_polly_S0 > ip_polly_E0 :
    first = ip_end
    second = ip_start
    ip_SE0_sub = (ip_polly_S0 - ip_polly_E0)
    ip_SE1_sub = (ip_polly_S1 - ip_polly_E1)
    ip_SE2_sub = (ip_polly_S2 - ip_polly_E2)
    ip_SE3_sub = (ip_polly_S3 - ip_polly_E3)

elif ip_polly_E0 > ip_polly_S0:
    first = ip_start
    second = ip_end
    ip_SE0_sub = (ip_polly_E0 - ip_polly_S0)
    ip_SE1_sub = (ip_polly_E1 - ip_polly_S1)
    ip_SE2_sub = (ip_polly_E2 - ip_polly_S2)
    ip_SE3_sub = (ip_polly_E3 - ip_polly_S3)

else:
    if ip_polly_S1 > ip_polly_E1:
        first = ip_end
        second = ip_start
        ip_SE0_sub = (ip_polly_S0 - ip_polly_E0)
        ip_SE1_sub = (ip_polly_S1 - ip_polly_E1)
        ip_SE2_sub = (ip_polly_S2 - ip_polly_E2)
        ip_SE3_sub = (ip_polly_S3 - ip_polly_E3)

    elif ip_polly_E1 > ip_polly_S1:
        first = ip_start
        second = ip_end
        ip_SE0_sub = (ip_polly_E0 - ip_polly_S0)
        ip_SE1_sub = (ip_polly_E1 - ip_polly_S1)
        ip_SE2_sub = (ip_polly_E2 - ip_polly_S2)
        ip_SE3_sub = (ip_polly_E3 - ip_polly_S3)

    else:
        if ip_polly_S2 > ip_polly_E2:
            first = ip_end
            second = ip_start
            ip_SE0_sub = (ip_polly_S0 - ip_polly_E0)
            ip_SE1_sub = (ip_polly_S1 - ip_polly_E1)
            ip_SE2_sub = (ip_polly_S2 - ip_polly_E2)
            ip_SE3_sub = (ip_polly_S3 - ip_polly_E3)

        elif ip_polly_E2 > ip_polly_S2:
            first = ip_start
            second = ip_end
            ip_SE0_sub = (ip_polly_E0 - ip_polly_S0)
            ip_SE1_sub = (ip_polly_E1 - ip_polly_S1)
            ip_SE2_sub = (ip_polly_E2 - ip_polly_S2)
            ip_SE3_sub = (ip_polly_E3 - ip_polly_S3)

        else:
            if ip_polly_S3 > ip_polly_E3:
                first = ip_end
                second = ip_start
                ip_SE0_sub = (ip_polly_S0 - ip_polly_E0)
                ip_SE1_sub = (ip_polly_S1 - ip_polly_E1)
                ip_SE2_sub = (ip_polly_S2 - ip_polly_E2)
                ip_SE3_sub = (ip_polly_S3 - ip_polly_E3)

            elif ip_polly_E3 > ip_polly_S3:
                first = ip_start
                second = ip_end
                ip_SE0_sub = (ip_polly_E0 - ip_polly_S0)
                ip_SE1_sub = (ip_polly_E1 - ip_polly_S1)
                ip_SE2_sub = (ip_polly_E2 - ip_polly_S2)
                ip_SE3_sub = (ip_polly_E3 - ip_polly_S3)

            else:
                first = ip_end
                second = ip_start
                ip_SE0_sub = (ip_polly_S0 - ip_polly_E0)
                ip_SE1_sub = (ip_polly_S1 - ip_polly_E1)
                ip_SE2_sub = (ip_polly_S2 - ip_polly_E2)
                ip_SE3_sub = (ip_polly_S3 - ip_polly_E3)

ip_SE_add = (ip_SE0_sub)*256**3 + (ip_SE1_sub)*256**2 + (ip_SE2_sub)*256 + ip_SE3_sub

if first == ip_start:
    if ip_polly_S3 == 0 or ip_polly_S3 == 255 :
        print('broadcast : ' + first)
    else:
        os.system('ping -c 1 ' + str(first))
    for first in range(0,ip_SE_add):
        ip_polly_S3 = ip_polly_S3 + 1
        if ip_polly_S3 == 256:
            ip_polly_S3 = ip_polly_S3 - 256
            ip_polly_S2 = ip_polly_S2 + 1
            if ip_polly_S2 == 256:
                ip_polly_S2 = ip_polly_S2 -256
                ip_polly_S1 = ip_polly_S1 + 1
                if ip_polly_S1 == 256:
                    ip_polly_S1 = ip_polly_S1 -256
                    ip_polly_S0 = ip_polly_S0 + 1
                    if ip_polly_S0 == 256:
                        print('error')

        ip_polly = (str(ip_polly_S0) + '.' + str(ip_polly_S1) + '.' + str(ip_polly_S2) + '.' + str(ip_polly_S3))
        if ip_polly_S3 == 0 or ip_polly_S3 == 255 :
            print('broadcast : ' + ip_polly)
        else:
            os.system('ping -c 1 ' + str(ip_polly))
        
else:
    if ip_polly_E3 == 0 or ip_polly_E3 == 255 :
        print('broadcast : ' + first)
    else:
        os.system('ping -c 1 ' + str(first))

    for first in range(0,ip_SE_add):
        ip_polly_E3 = ip_polly_E3 + 1
        if ip_polly_E3 == 256:
            ip_polly_E3 = 0
            ip_polly_E2 = ip_polly_E2 + 1
            if ip_polly_E2 == 256: 
                ip_polly_E2 = 0
                ip_polly_E3 = 0
                ip_polly_E1 = ip_polly_E1 + 1
                if ip_polly_E1 == 256:
                    ip_polly_E1 = 0
                    ip_polly_E0 = ip_polly_E0 + 1
                    if ip_polly_E0 == 256:
                        print('error')
                        
        ip_polly = (str(ip_polly_E0) + '.' + str(ip_polly_E1) + '.' + str(ip_polly_E2) + '.' + str(ip_polly_E3))
        if ip_polly_E3 == 0 or ip_polly_E3 == 255 :
            print('broadcast : ' + ip_polly)
        else:
            os.system('ping -c 1 ' + str(ip_polly))