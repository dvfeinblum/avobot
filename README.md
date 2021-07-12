# avobot
This here is a twitter bot I wrote!

## Things it Does
1. you can manually post a tweet using `update_status`
but this isn't gonna stay a CLI forever. Mostly just testing. For now,
the way you do this is:
```
python utils/update_status.py --secrets ~/path/to/secrets/file.yml --text "here is a tweet"
```

2. we can check to see if we created a new blogpost and then
let people know about it!
```
python utils/blogpost_checker.py --secrets ~/path/to/secrets/file.yml
```

## Things it Will Do
1. Post a tweet when I go live on twitch
1. Post a tweet when I write a blog post
