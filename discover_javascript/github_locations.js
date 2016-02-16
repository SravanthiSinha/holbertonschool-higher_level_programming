
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

var options2 = {
    host: 'api.github.com',
    path: '/users/',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token '+ process.env.TOKEN
    }
};

var req = https.request(options, function(res) {
    var cb=function(jsonString){
//	fs.writeFile('/tmp/37', jsonString);
	var parsedData= JSON.parse(jsonString);
	var loc={};
	var repos=parsedData['items'];
	    /*.map(function(obj){
	    var robj={};  
	    robj[obj.full_name]=obj['owner'];	    
  	    return(robj);		 
	})

	console.log(repos);*/

	for(var obj in repos){
//	    console.log(repos[obj].owner['url']);
	   options2.path=repos[obj].owner['url'];
	    var req2=https.request(options2,function( res2) {
		var cb2=function(jstring)
		{
		    var lobj={};
		    lobj[repos[obj]['full_name']]= JSON.parse(jstring)['location'];
		    console.log(lobj);
		    return (lobj);
		}
		loc2=	streamToString(res2,cb2);
	    });
	    
	    req2.end();	
	}

	for(mykey in loc)
	console.log(mykey+ " "+repos[mykey]);
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
