Quine - is  a self-replicating program that produces its complete source code as its output, basically, a quine is a program that prints or displays its own source code when it is executed.
Writing a quine usually requires using some form of self-reference or reflection mechanisms available in the programming language

* All quines: https://rosettacode.org/wiki/Quine#Go

### Oneliners:

```bash

## Start a simple webserver running in the background on port 8000 with the current directory as the doc root
## sending stdout and stderr to /dev/null. Also making sure it continues running when the shell is closed.
nohup python3 -m http.server 80 > /dev/null 2>&1 & 
# ptyhon 2
python -m SimpleHTTPServer 80

```

```bash
# gotcha get ip
import socket
socket.gethostbyname(socket.gethostname())
```

```bash
#fibonacci
fib = lambda n: n if n < 2 else (fib(n - 1) + fib(n - 2))
```