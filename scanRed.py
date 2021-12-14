#!/usr/bin/python3

# library
import os
import re
import sys
import threading

# import personal module
from myModule import JSON, customCrono

# global variables
ping = 'ping -c 1'
IPXHILOS = 1
tmpFile = 'tmp.json'
waktmpFile = 'tmps.txt'
numeroIPs = list()
ttl_and_ip = list()
priority_ports = [22, 80]

def importData():
    try:
        # import config red
        tmp = JSON.JSON(tmpFile).read() 
        
        #import necessary data
        ip = tmp['ip'] # ip red
        start_N = int(tmp['start']) # ip inicio
        finally_N = int(tmp['finally']) # ip finally

        # split ip
        ipSplit = ip.split('.')
        # create ip red
        red = '{0}.{1}.{2}.'.format(ipSplit[0], ipSplit[1], ipSplit[2])
        
        return ip, start_N, finally_N, red 
    except:
        print("[!] Error")
        sys.exit(1)

class Hilo(threading.Thread):
    def __init__(self, start, end):
        threading.Thread.__init__(self)
        self.inicio = start
        self.fin = end

    def run(self):
        count = 0
        for subred in range(self.inicio, self.fin):
            direccion = red + str(subred)
            response = os.popen(ping + " " + direccion)
            for line in response.readlines():
                if "ttl" in line.lower():
                    numeroIPs.append(direccion)
                    print(direccion, "está activo")
                    out = line.split()
                    ttl = out[5].split('=')[1]
                    ttl = int(ttl)
                    system = "ttl={}".format(ttl)
                    if ttl >= 0 and ttl <= 64:
                         system = "linux"
                         sp = True
                    elif ttl >= 65 and ttl <= 128:
                        system = "windows"
                        sp = True
                    elif ttl >= 129 and ttl <= 254:
                        system = "Solaris/AIX"
                        sp = True
                    else:
                        sp = False
                    com_file = "{};{}".format(direccion, system)
                    com_file = 'echo "\n{}" >> {}'.format(com_file, waktmpFile)
                    os.system(com_file)

                        
if __name__ == '__main__':

    ip, start_N, finally_N, red = importData()

    # control time
    TMP = customCrono.CronoTime() # create object TMP
    TMP.start() # save time now

    print("[*] El escaneo se está realizando desde", red + str(start_N), "hasta", red + str(finally_N))

    try:
        NumeroIPs = finally_N - start_N
        numeroHilos = int((NumeroIPs / IPXHILOS))
        hilos = list()
        
        for i in range(numeroHilos):
            finAux = start_N + IPXHILOS
            if finAux > finally_N:
                finAux = finally_N
            hilo = Hilo(start_N, finAux)
            hilo.start()
            hilos.append(hilo)
            start_N = finAux
    except Exception as e:
        print("[!] Error creando hilos:", e)
        sys.exit(2)

    for hilo in hilos:
        hilo.join()

    # control time
    t = TMP.stop() 
    
    print("[*] El escaneo ha durado %s" % t)

    jsonFile = {
            "host_N": len(numeroIPs)
            }
    tmp = JSON.JSON(tmpFile).write(ctx=jsonFile)
    with open(waktmpFile, 'r', encoding = 'utf-8') as fr,open('tmp.txt', 'w', encoding = 'utf-8') as fd:
        for text in fr.readlines():
                if text.split():
                        fd.write(text)
