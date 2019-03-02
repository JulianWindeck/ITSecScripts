import socket


def printLine():
    print 40*'-'

default_ports = {
    20: 'FTP',
    21: 'FTP',
    22: 'SSH',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'SSL',
    3306: 'MySQL',
    8080: 'HTTP_ALT'
}
def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        return True
    return False


def scan(ip):
    socket.setdefaulttimeout(0.8)
    openPorts = []
    for port in default_ports.keys():
        print '[*] Scanning port: ' + str(port)
        if isOpen(ip, port):
            openPorts.append(port)
            print '[+] ' + ip + ' open at port ' + str(port)
    return openPorts


def main():
    printLine()
    print 'WELCOME TO JSCAN'
    printLine()
    site = raw_input('Enter the url you want to scan:')

    ip = ''
    try:
        ip =  socket.gethostbyname(site)
    except:
        print '[-] URL seems to be wrong!'
        print '[*] Exit'
        exit(0)
    print '[*] Starting to scan ' + ip

    openPorts = scan(ip)
    printLine()
    print '[+] Finished! Results for ' + site + ' (' + ip + '):'
    for openPort in openPorts:
        print '[+] Open at port: ' + str(openPort) + ' (' + default_ports.get(openPort) + ')'

if __name__ == '__main__':
    main()