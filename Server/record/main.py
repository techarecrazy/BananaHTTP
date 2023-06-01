from pyshort import tcp
tcp(8080).accept()[0].send(b"HTTP/1.1 200 OK\n\n"+open("index.html",'rb').read())
