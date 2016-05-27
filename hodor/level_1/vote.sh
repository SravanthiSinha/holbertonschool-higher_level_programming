for i in $(seq 1 10):
do
curl 'http://173.246.108.142/level1.php' -H 'Cookie: HoldTheDoor=abdacb1456c5f669a7fda8f3a9f5493c773d3612' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.87 Chrome/49.0.2623.87 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level1.php' -H 'Connection: keep-alive' --data 'id=37&holdthedoor=Submit&key=abdacb1456c5f669a7fda8f3a9f5493c773d3612' --compressed
done
