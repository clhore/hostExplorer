#!/usr/bin/python3

# library
import os
import sys
import platform
import threading
from datetime import datetime

# import personal module
from myModule import JSON, customCrono

# global variables
ping = 'ping -c 1'
redFile = 'red.json'
ttl_and_ip = list()

def importData():
    try:
        # import config red 
        conf = JSON.JSON(redFile).read() 

        #import necessary data
        ip = conf['ip'] # ip red
        start_N = int(conf['start']) # ip inicio
        finally_N = int(conf['finally']) # ip finally
        IPXHILOS = int(conf['threads'])

        # split ip
        ipSplit = ip.split('.')
        # create ip red
        red = '{0}.{1}.{2}.'.format(ipSplit[0], ipSplit[1], ipSplit[2])
        
        return IPXHILOS, ip, start_N, finally_N, red 
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
                    ttl_and_ip.append(direccion)
                    print(direccion, "está activo")
                    break


if __name__ == '__main__':

    IPXHILOS, ip, start_N, finally_N, red = importData()

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
    
    tmp_host = {
            "host_N": len(ttl_and_ip),
            "host": ttl_and_ip
            }
    JSON.JSON('tmp.json').write(tmp_host)
    print(ttl_and_ip)
