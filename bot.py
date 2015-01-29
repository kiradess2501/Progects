import praw
import time

r = praw.Reddit(user_agent = '''
The purpose of this bot is to help organize the subreddit
/r/progects with tasks such as:
Registering redditers for events
Organizing teams
and anything else that may be required

by /u/NEET_Here
''')

r.login()

# List of words the bot will reply to
words_to_match = ['hey', 'hello', 'hi', 'sup', 'greetings',
				'howdy', 'bonjour','good day', 'good morning', 
				'hiya', 'how goes it', 'whats up',
				'how are you']

cache = []

# Function to run the bot
def run_bot():
	subreddit = r.get_subreddit('test')
	comments = subreddit.get_comments(limit=25)
	
	for comment in comments:
		comment_text = comment.body.lower()
		
		# Bot was replying to any words that contained the string
		# regardless of whether it was singular
		# So I'm trying to split them
		comment_text = comment_text.split(' ')
		
		for word in words_to_match:
			if comment.id not in cache and word in comment_text:
				print ('Replying...')
				comment.reply('This is a test bot. Just sayin\' {0}'.format(word))
				cache.append(comment.id)
				time.sleep(2)

def main():		
	while True:
		run_bot()
		time.sleep(10)

if __name__ = '__main__':
	main()
