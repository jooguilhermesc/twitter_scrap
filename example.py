import twint

client = twint.Config()
client.Username = 'CHOOSE_THE_USERNAME_THAT_YOU_WANTS_TO_SCRAP'
client.Search = 'CHOOSE_THE_TERM_THAT_YOU_WANTS_LOOK_FOR'
client.Format = "Twitter Id: {id} | Tweet: {tweet}"

twint.run.Search(client)

'''
twint.run.Followers(client) # THIS LINE RETURNS FOLLOWERS LIST FOR CHOOSED USER
twint.run.Profile(client) # THIS LINE RETURNS ALL TWITTER FOR THE CHOOSED USER
'''
