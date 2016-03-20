require 'httpclient'
require 'uri'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 1ce0fbaacb310b39ccf742a79fd0de2238a95b8a'
}

client=HTTPClient.new
uri=URI.parse('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
result= client.get(uri,nil,extheaders)
hashedresult= JSON.parse(result.content)

owners=Hash.new
ownerlocations=Hash.new
githublocations=Array.new(){Hash.new}

items=hashedresult['items']
items.map{|x|  owners[x['owner']['login']]=x['full_name']}.join('\n')

threads=[]
owners.each do |owner,fullname|
  threads << Thread.new do
  client2=HTTPClient.new
  uri2=URI.parse('https://api.github.com/users/'+owner)
  result2= client2.get(uri2,nil,extheaders)
  hashedresult2= JSON.parse(result2.content)
  ownerlocations[fullname]=hashedresult2['location']
  end
end
threads.each do |thread|
    thread.join
end

ownerlocations.each do |fullname,location|
  hash1={'full_name'=>fullname,'location'=> location}
  githublocations.push(hash1)
end
puts JSON.generate(githublocations)
