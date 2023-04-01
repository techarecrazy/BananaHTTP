del http.txt

if exist %1 (
  echo HTTP/1.1 200 OK  &1 > http.txt
) 
ELSE (
  echo HTTP/1.1 404 Not Found
) 
