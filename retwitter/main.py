from twython import Twython
import csv
import sys
import traceback

twitter_accounts = {}

def initialize():
    with open('accounts.csv') as account_file:
        rows = csv.reader(account_file, delimiter=',', quotechar='|')
        first_row = True
        for row in rows:
            if first_row:
                first_row = False
                continue
            APP_KEY = row[0]  # API Key
            APP_SECRET = row[1]  # API Secret
            OAUTH_TOKEN = row[2]  # Access Token
            OAUTH_TOKEN_SECRET = row[3]  # Access Token Secret
            twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            try:
                account_settings = twitter.get_account_settings()
                twitter_accounts[account_settings['screen_name']] = twitter
            except:
                pass  # Create only those, which are possible


def add_account():
    with open('accounts.csv', 'a+') as account_file:
        account_file = csv.writer(account_file, delimiter=',', quotechar='|')
        print('Input app key')
        app_key = input()
        print('Input app secret')
        app_secret = input()
        print('Input oauth token')
        oauth_token = input()
        print('Input token secret')
        token_secret = input()
        account_file.writerow([app_key, app_secret, oauth_token, token_secret])


def show_accounts():
    account_number = [user for user in twitter_accounts.keys()]
    print('')
    for i, account in enumerate(account_number):
        print(i + 1, account)
    print('')
    return account_number


def see_tweets(twitter):
    print('Choose the tweet you want to retweet')
    tweets = twitter.get_user_timeline(trim_user=True, include_entities=False, include_rts=1, exclude_replies=True)
    i = 1
    tweet_dict = {}
    for tweet in tweets:
        print(i,  "".join(tweet['text'].splitlines()))  #, end=''
        tweet_dict[i] = tweet['id']
        i += 1
    print('')
    return tweet_dict


def retweet():
    print('Which user tweet to retweet? Choose one number.')
    print('')
    accounts = show_accounts()
    # user = input()
    account_no = int(input())
    user = accounts[account_no - 1]
    if user in twitter_accounts:
        tweet_dict = see_tweets(twitter_accounts[user])
    else:
        print('Please type correct name.')
    rt_tweet = int(input())
    for name, account in twitter_accounts.items():
        if name != user:
            try:
                resp = account.retweet(id=tweet_dict[rt_tweet])
                print('Retweeted for ' + name)
            except Exception as e:
                print('Failed to retweet for ' + name + ' because ' + str(e))


if __name__ == '__main__':
    initialize()
    while True:
        print('')
        print('===================================')
        print('What do you want to do? Choose one number:')
        print('1. Add new account')
        print('2. See all accounts')
        # print('3. See tweets')
        print('3. Retweet')
        print('0. Exit')
        print('===================================')
        print('')
        option = input()
        if option == '1':
            add_account()
            initialize()  # Regenerate account links
        elif option == '2':
            show_accounts()
        # elif option == '3':
        #     get_tweets()
        elif option == '3':
            retweet()
        elif option == '0':
            exit(0)
        else:
            print('Not a valid option. Retry.')