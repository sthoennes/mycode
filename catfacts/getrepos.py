#!/usr/bin/env python3
import requests

def show_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    r = requests.get(url)
    #print(r.json())
    #print(r.text)
# use of headers
    #print(r.headers)
# rate limits for hitting an api site, the more you do, the more you pay 
# X-ratelimit-limit=60 how many github requests we can make in an hour
# X-rateLimit-Remaining tells us how many requests we have 
    print(f"Limit:       {r.headers['X-RateLimit-Limit']}")
    print(f"Remaining:   {r.headers['X-RateLimit-Remaining']}")
    print(f"Used:        {r.headers['X-RateLimit-Used']}")


if __name__ =="__main__":
    show_repos('sthoennes')
