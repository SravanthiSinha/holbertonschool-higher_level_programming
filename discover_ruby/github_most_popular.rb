require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 42ee520bd99c8951da18894d2e0cd0c06d957089'
}

client=HTTPClient.new
domain='https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'
print client.get_Cpontent(domain,extheaders)