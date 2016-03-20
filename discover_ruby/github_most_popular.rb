require 'httpclient'
require 'uri'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 1ce0fbaacb310b39ccf742a79fd0de2238a95b8a'
}

client=HTTPClient.new
uri=URI.parse('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
result= client.get(uri,nil,extheaders)
puts result.content

