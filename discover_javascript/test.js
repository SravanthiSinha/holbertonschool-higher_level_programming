var https = require('https');
var fs=require('fs');

var options = {
    host: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
     headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token b65bc47da5b1dc6aea9835a3897ea55cad8fef48'
  }
};

var options2 = {
    host: 'api.github.com',
//    path: '/users/',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token b65bc47da5b1dc6aea9835a3897ea55cad8fef48'
    }
};

var owners={};
var lobj={};

var req = https.request(options, function(res) {
    streamToString(res,cb);
});
			
req.end();

req.on('error', function(e) {
    console.error(e);
});

var cb=function(jsonString){
	
    var parsedData= JSON.parse(jsonString);
    
    owners=parsedData['items'].map(function(obj){
	    var robj={};	    
	    robj[obj.owner['login']]=obj.full_name;	    
  	    return(robj);		 
    });
    
    getlocations();
}
function getlocations()
{
    for( repo in owners)
	{
	    for(x in owners[repo])
	    {
		options2.path='/users/'+x;
		var req2=https.request(options2,function(res2){		    
		   streamToString(res2,cb2);
		});
		req2.end();
		req2.on('error',function(e){
	            console.error(e);
		});
		//console.log(lobj);
	    }
	    
	}
    console.log(lobj);
}

var cb2= function(jsString){
    var lo=JSON.parse(jsString);
    lobj[lo.login]=lo.location;
}



function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}
