# Mastodon name scan
Sometimes your friends put their mastodon handles in their twitter URL or description.

I wrote a script that looks for those. You could easily extend it to look in tweets and things.

You will need Python 3 to use it. You're also going to have to sign up for a twitter API key, but it doesn't cost anything but time.

## Usage:
First: [get a twitter API key and secret](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api). Put the secret info in the twitter.config file
```
[yourname.consumer]
key = ALGUHALGUHAGLUAHGLAUGHALU # "API Key" goes here
secret = blaghbalhgbalebgleauhglauhlahdlsuhfkalsabgaeibalif # this one is "API Secret"

[yourname.access]
key = HAUHGALUGHALUGHALGUAHLAGUHGLAUGHALUGHALUGHALGUAHLA # "User access token"
secret = kasjhflaxkwuefhxm6awilrhgm3xalsrihgTxa7lihgam # "User access token secret"
```

You need the click library installed, which makes it easy to expand command line tools.
You need the twitter python api installed. For dealing with twitter.

Probably just need to do:

`pip install click python-twitter`

Usage: exomus scan
andr00 (Andrew Denyes): mograph.social/@andr00
...

TODO:
* Check to make sure it actually works
* Make it scan the last tweet at least
* Make it scan your timeline until you run out of API calls
* Maybe save things to a file