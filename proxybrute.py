from proxylist import ProxyList
import requests
import sys
import _thread

p1 = ProxyList()
p1.load_file('big')
print("Starting 15 threads each with 5000 tries")

def get_site(threadName, none):
    count = 5000
    while count > 1:
        proxies = { 'http': 'http://'+p1.random().address() }
        count = count-1
        try:
            out = requests.get('http://google.com', proxies=proxies, timeout=5)
            print('Thread: '+threadName+'\t Proxy: '+str(proxies)+'\t URL: '+out.url)
        except requests.exceptions.ConnectTimeout:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue
        except KeyboardInterrupt:
            print('Exiting')
            sys.exit(0)

try:
    _thread.start_new_thread(get_site, ("Thread-1", 1))
    _thread.start_new_thread(get_site, ("Thread-2", 2))
    _thread.start_new_thread(get_site, ("Thread-3", 3))
    _thread.start_new_thread(get_site, ("Thread-4", 4))
    _thread.start_new_thread(get_site, ("Thread-5", 5))
    _thread.start_new_thread(get_site, ("Thread-6", 6))
    _thread.start_new_thread(get_site, ("Thread-7", 7))
    _thread.start_new_thread(get_site, ("Thread-8", 8))
    _thread.start_new_thread(get_site, ("Thread-9", 9))
    _thread.start_new_thread(get_site, ("Thread-10", 10))
    _thread.start_new_thread(get_site, ("Thread-11", 11))
    _thread.start_new_thread(get_site, ("Thread-12", 12))
    _thread.start_new_thread(get_site, ("Thread-13", 13))
    _thread.start_new_thread(get_site, ("Thread-14", 14))
    _thread.start_new_thread(get_site, ("Thread-15", 15))
except:
    print("Error: unable to start thread")

while 1:
    pass
