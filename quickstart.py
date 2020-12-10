from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='', password='', headless_browser=True)

# let's go! :>
with smart_run(session):
    session.like_by_feed(amount=50, randomize=False, unfollow=False, interact=False)
    following_list = session.grab_following(username="", amount="full", live_match=True, store_locally=True)
    session.set_do_story(percentage=70, enabled=True, simulate=True)
    session.story_by_users(following_list)
    session.set_delimit_liking(enabled=True, max_likes=150, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=4, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-0.50,
                                    delimit_by_numbers=True,
                                    max_followers=2000,
                                    max_following=3500,
                                    min_followers=25,
                                    min_following=25)
    session.set_do_comment(False, percentage=80)
    session.set_do_follow(enabled=True, percentage=50, times=1)
    session.set_comments(['Amazing!', 'Awesome!!', 'Cool!', 'Good one!',
                          'Really good one', 'Love this!', 'Like it!',
                          'Beautiful!', 'Great!', 'Nice one'], media='Photo')
    session.set_sleep_reduce(200)
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=700,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=180,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=400,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)
    session.unfollow_users(amount=50, instapy_followed_enabled=True,
                          instapy_followed_param='nonfollowers',
                           style="FIFO",
                           unfollow_after=24 * 60 * 60,
                           sleep_delay=503)
    session.unfollow_users(amount=50, instapy_followed_enabled=True,
                          instapy_followed_param='all',
                           style="FIFO",
                           unfollow_after=48 * 60 * 60,
                           sleep_delay=503)
    session.like_by_tags(['forex','forexsignals','forexsignal','heavypips'], amount=50)
    session.join_pods(topic='sports', engagement_mode='no_comments')


