for i in $(seq 1 1024):
do
    curl 'http://173.246.108.142/level0.php' -H 'Accept: text/html,application/xhtml+xml,applxml;q=0.9,image/webp,*/*;q=0.8' -H 'Origin: null' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' --data 'id=37&holdthedoor=Submit' --compressed
done
