from TwitterSearch import *
import json

def get_person_tweet(person):
    try:
        tuo = TwitterUserOrder(str(person)) 
        # tuo = TwitterUserOrder('ponny1') 
        # tuo = TwitterUserOrder('katasonovamaria')
    
        ts = TwitterSearch(
            consumer_key = "",
            consumer_secret = "",
            access_token="",
            access_token_secret=""
         )
    
        for tweet in ts.search_tweets_iterable(tuo):
            # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            file = open(str(person) + '.txt' , 'a')
            print(tweet['created_at'])
            json_str = json.dumps(tweet, indent = 4, sort_keys = True)
            file.write(u''.join(json_str))
        file.close()
    except TwitterSearchException as e: # catch all those ugly errors
        print(e)

def get_mentions_about(person_rus)
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords([str(person_rus)])
        tso.set_language('ru')
        tso.set_include_entities(False) 
        ts = TwitterSearch(
            consumer_key = "",
            consumer_secret = "",
            access_token="",
            access_token_secret=""
         )
        file = open(str(person_rus) + 'mention.json' , 'a')
        for tweet in ts.search_tweets_iterable(tso):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            json_str = json.dumps(tweet, indent = 4, sort_keys = True)
            file.write(u''.join(json_str))
        file.close()
    except TwitterSearchException as e:
        print(e)
