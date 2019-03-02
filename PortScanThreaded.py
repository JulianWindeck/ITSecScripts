import socket
import optparse
from threading import Thread, Semaphore


lock = Semaphore(value=1)
def canConnect(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        s.send('test\r\n')
        reply = s.recv(100)

        lock.acquire()
        openPorts[port] = reply
        print '[+] Port %d is open: %s' % (port, reply)
    except:
        lock.acquire()
        print '[-] %d is closed' % port
    finally:
        lock.release()
        s.close()

def portScan(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except:
        print '[-] %s doesn\'t seem to exist.' % host
        exit(0)

    socket.setdefaulttimeout(1.5)
    for port in ports:
        t = Thread(target=canConnect, args=(host, int(port)))
        t.start()

def main():
    parser = optparse.OptionParser('%prog -H <host> -p <port>')
    parser.add_option('-H', dest='host', type='string', help='the host you want to target')
    parser.add_option('-p', dest='ports', type='string', help='a list of comma separated ports you want to scan')

    (options, args) = parser.parse_args()
    host = options.host
    ports = str(options.ports).split(', ')
    for i in range(40):
        ports.append(str(i))

    if host == None or ports[0] == None:
        print '[-] Please enter a host and ports (separated by comma)'
        exit(0)
    portScan(host, ports)

if __name__ == '__main__':
    main()