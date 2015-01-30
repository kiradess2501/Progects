import praw
import time

r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

# store user for later use, but not password
userN = input("Username: ")
print("Logging in...")
r.login(username=userN)

# List of words the bot will reply to
words_to_match = ['hey', 'hello', 'hi', 'sup', 'greetings',
                'howdy', 'bonjour','good day', 'good morning',
                'hiya', 'how goes it', 'whats up',
                'how are you']
cache = []

print("Successfull login...")

# Function to run the bot
def run_bot():
    # Cache file where comment Id's are stored
    f = open("commentIDcache.txt", "+r")
    print("Opening file for already replied comments...")
    for line in f:
        cache.append(line)
        
    print("Grabbing subreddit...")
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit=25)

    # search through comments, if a match is found reply
    # unless the user has already replied or if the comment
    # is by the user
    for comment in comments:
        print("Reading comment...")
        comment_text = comment.body.lower().split(' ')
        for commentWord in comment_text:
            for word in words_to_match:
                if word == commentWord and comment.id not in f.read() and comment.author is not r.get_redditor(user_name=userN):
                    print("Comment found, ID: " + comment.id)
                    print ('Replying...')
                    comment.reply("This is a test bot. Just sayin' hey")
                    print ('Writing Comment ID to Cache')
                    # add comment id to cache and cache file simultaneously
                    cache.append(comment.id)
                    f.write(comment.id + "\n")
                    print ('Cache Updated')
                    # rate exception avoided here
                    time.sleep(10)
    f.close()

def main():
    while True:
        run_bot()
        time.sleep(100)

main()
