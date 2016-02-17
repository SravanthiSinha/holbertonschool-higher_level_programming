var https = require('https');
var fs=require('fs');

var options = {
    host: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
     headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token bd59c3c9a475b797ea855b3e1e1542828afc96aa'
  }
};

var owners=[];
var lobj=[];;

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
	robj[1]=obj.full_name;	
	robj[0]=obj.owner['login'];
  	    return(robj);		 
    });
//    console.log(owners);
    getlocations();
}

function getlocations()
{
    for( x in owners)
    {
	options.path='/users/'+owners[x][0];
//	console.log(options.path);
	var req2=https.request(options,function(res2){
	    streamToString(res2,cb2);
	  if(Object.keys(lobj).length==29)
	    {	
		writeF(owners,lobj);
	    }
		});
		req2.end();
		req2.on('error',function(e){
	            console.error(e);
		});	
	    }  	
}

var cb2= function(jsString){
    var lo=JSON.parse(jsString);
    var robj={};
    
    robj[0]=lo.login;
    robj[1]=lo.location;
    
    lobj.push(robj);
}


function writeF(owners,locations){
    fs.writeFile('/tmp/37','[');
    for( var a in owners )
    {
	for(b in locations)
	{  if(owners[a][0]==locations[b][0])
	   {;
	       var owner= new Object();
	       owner.fullname=owners[a][1];
	    owner.location=locations[b][1];
	    
	    fs.appendFile('/tmp/37',JSON.stringify(owner));
	       break;
	   }
	}
	}
    fs.appendFile('/tmp/37',']');
    console.log('The file was saved!');
}

function Owner(fullname,location){this.fullname=fullname;this.location=location;}


function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
}
