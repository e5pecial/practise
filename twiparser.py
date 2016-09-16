# from TwitterSearch import *
import json
# try:
#     tso = TwitterSearchOrder()
#     tso.set_keywords(['Баронова'])
#     tso.set_language('ru')
#     tso.set_include_entities(False)

#     ts = TwitterSearch(
#         consumer_key = "",
#         consumer_secret = "",
#         access_token="",
#         access_token_secret=""
#      )
#      # this is where the fun actually starts :)
#     for tweet in ts.search_tweets_iterable(tso):

#         # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
#         print(tweet['created_at'])
#         # file = open('bar_22_data.json' , 'a')

#         json_str = json.dumps(tweet, indent = 4, sort_keys = True)
#     # print(json_str)
#         file.write(u''.join(json_str))
#     file.close()
# except TwitterSearchException as e:
#     print(e)

# #######################################


# from TwitterSearch import *

# try:
#     tuo = TwitterUserOrder('gudkovd') # create a TwitterUserOrder
#     # tuo = TwitterUserOrder('ponny1') # create a TwitterUserOrder
#     # tuo = TwitterUserOrder('katasonovamaria') # create a TwitterUserOrder

#     # it's about time to create TwitterSearch object again
#     ts = TwitterSearch(
#         consumer_key = "vAFqO3jFbVUXkSVKSitaUiU4Q",
#         consumer_secret = "4aG1sNq2pwDjEvpvG7FbR63GMCrQQfbTkP8Z0kdrLvkE8MCv8A",
#         access_token="711632049711554560-Co5AtwXqrg5Qf3m2TwAzHnw6C5rWfxS",
#         access_token_secret="VXMe4nJKHX1mb8QNh5LW3TMAdZSQ0L9FuwZADlG6GxHFB"
#      )

#     # start asking Twitter about the timeline
#     for tweet in ts.search_tweets_iterable(tuo):
#         # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
#         file = open('20160907gudkov_twitter.txt' , 'a')
#         print(tweet['created_at'])
#         json_str = json.dumps(tweet, indent = 4, sort_keys = True)
#         file.write(u''.join(json_str))
#     file.close()
# except TwitterSearchException as e: # catch all those ugly errors
#     print(e)


#  22 08 2016 ################################

from TwitterSearch import *
try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['Баронова'])
    tso.set_language('ru')
    tso.set_include_entities(False) 
    ts = TwitterSearch(
        consumer_key = "vAFqO3jFbVUXkSVKSitaUiU4Q",
        consumer_secret = "4aG1sNq2pwDjEvpvG7FbR63GMCrQQfbTkP8Z0kdrLvkE8MCv8A",
        access_token="711632049711554560-Co5AtwXqrg5Qf3m2TwAzHnw6C5rWfxS",
        access_token_secret="VXMe4nJKHX1mb8QNh5LW3TMAdZSQ0L9FuwZADlG6GxHFB"
     )
    file = open('bar_0709_data.json' , 'a')
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        json_str = json.dumps(tweet, indent = 4, sort_keys = True)
        file.write(u''.join(json_str))
    file.close()
except TwitterSearchException as e:
    print(e)
