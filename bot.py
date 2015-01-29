import praw
import time

r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

print("Logging in...")
r.login()

# List of words the bot will reply to
words_to_match = ['hey', 'hello', 'hi', 'sup', 'greetings',
				'howdy', 'bonjour','good day', 'good morning', 
				'hiya', 'how goes it', 'whats up',
				'how are you']
				
print("Successfull")
cache = []

# Function to run the bot
def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=25)

	for comment in comments:
		print("Reading comment...")
		comment_text = comment.body.lower().split(' ')
		
		for commentWord in comment_text:
				for word in words_to_match:
					if word == commentWord and comment.id not in cache:
						print("Comment found, ID: " + comment.id)
						print ('Replying...')
						comment.reply("This is a test bot. Just sayin' hey")
						cache.append(comment.id)
	time.sleep(10)


def main():		
	while True:
		run_bot()
main()
