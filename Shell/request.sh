rm http.txt
if test -f "$1"; then
    cat oldhttp.txt $1 >> http.txt
else
    echo "HTTP/1.1 404 Not Found" > http.txt
fi
