from services import CoronaService, TweetService
from utils import create_corona_message
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(seconds=5))
def corona_task():
    """
    Task which will get corona infos from website and post it on the
    twitter profile
    """
    # create corona service instance and get info from data website
    corona_service = CoronaService()
    corona_brazil_info = corona_service.get_info('brazil')
    corona_world_info = corona_service.get_info()

    # format messages for tweet service message
    corona_brazil_message = create_corona_message(corona_brazil_info)
    corona_world_message = create_corona_message(corona_world_info)

    # create tweet service instance and tweet messages
    tweet_service = TweetService()
    tweet_service.tweet(corona_brazil_message)
    tweet_service.tweet(corona_world_message)
