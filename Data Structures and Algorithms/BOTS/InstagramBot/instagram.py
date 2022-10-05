from instapy import InstaPy
from instapy import smart_run

username = '***************' #enter your username
password = '***************' #enter your password

profile = InstaPy(username= username,
                  password= password,
                  headless_browser= False,
                  browser_executable_path= r"C:\Program Files\Mozilla Firefox\firefox.exe")

with smart_run(profile):
    profile.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    min_followers=70,
                                    min_following=50)
    
    #select desired language
    profile.set_mandatory_language(enabled=True, character_set=['ENGLISH'])
    
    #allow the bot to follow other accounts
    profile.set_do_follow(True, percentage=10, times=2)
    
    #allow the bot to like posts with specific tags in them
    profile.set_do_like(enabled=True, percentage=70)
    profile.like_by_tags(['coding', 'programming', 'computerscience', 'webdevelopment'], media='Photo')
    
    #allow bot to comment on posts
    profile.set_do_comment(enabled=True, percentage=25)
    profile.set_delimit_commenting(enabled=True, max_comments=32, min_comments=10)
    profile.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])

    profile.set_comments(['Nice work!'], media='Photo')
    profile.set_comments(['Great work!'], media='Video')
    profile.set_comments(['Nice work! @{}'], media='Photo')

    profile.set_dont_like(['politics'])

