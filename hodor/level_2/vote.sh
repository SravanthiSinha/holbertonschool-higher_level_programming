for i in $(seq 1 1024):
do
curl 'http://173.246.108.142/level2.php' -H 'Cookie: HoldTheDoor=abdacb1456c5f669a7fda8f3a9f5493c773d3612' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent:Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MS-RTC LM 8; .NET CLR 2.0.50727; .NET CLR 1.1.4322)' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level2.php' -H 'Connection: keep-alive' --data 'id=37&holdthedoor=Submit&key=abdacb1456c5f669a7fda8f3a9f5493c773d3612' --compressed
done
