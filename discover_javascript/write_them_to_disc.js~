var https = require('https');
var fs=require('fs');

var options = {
    host: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
     headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token ' + process.env.TOKEN
  }
};

var req = https.request(options, function(res) {
   
 /*  res.on('data', function(d) {
      process.stdout.write(d);
      // console.log('hello');
      });*/
    var cb=function(jsonString){
/*	console.log(typeof jsonString);
	console.log(jsonString);	*/
	fs.writeFile('/tmp/37', jsonString);
	console.log("The file is saved");
    }
    streamToString(res,cb);
    
   
});
req.end();

req.on('error', function(e) {
    console.error(e);
});

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}
