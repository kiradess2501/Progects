import praw
import time


class Bot():
	
	# Cache storage
	cache = []
	
	# List of words the bot will reply to
	comment_words = []
	comment_reply = ''
	
	# Required for functions 
	subreddit =  None
	comments = None
	
	# Subreddits to search for
	subreddits = []
	subredditstring = ''
					
	def __init__(self, cache_file):
		self.cache_file = cache_file
		''' 
		Logs the bot into Reddit. Use append or extend to add keywords
		for the comment search function and add subreddits to search
		through
		
		Comments to search for are in self.comment_words
		Reply with is in self.comment_reply
		Subreddits is in self.subreddits
		'''
			
		print ("DON'T FORGET TO APPEND THE NECESSARY WORDS TO THE BOT"
				"SUCH AS COMMENTS, COMMENT REPLY, AND SUBREDDITS")
				
		self.r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

		# store user for later use, but not password
		self.bot_name = 'progects_bot1'
		self.password = 'B0tP@ssword'
		print("Logging in...")
		self.r.login(self.bot_name, self.password)


		print("Successfull login...")
		
		
	def cache_create(self):
		''' 
		Pulls information from file and creates cache
		'''
		with open(self.cache_file, 'r') as f:
			self.cache = f.read().split('\n')
			self.cache = [x for x in self.cache if x != '']

			
	def comment_search(self):
		'''
		Searches for comments in the comment_words list and replies
		to them
		'''
			
		self.comments = self.subreddit.get_comments(limit=25)

		# Search through comments, if a match is found reply
		# unless the user has already replied or if the comment
		# is by the user.
		
		print("Reading comments...")
		for comment in self.comments:
			
			# Removes any extraneous characters 
			comment_text = comment.body.lower().split(' ')
			comment_text = [x.strip('?!@#$%^&*"') for x in comment_text]
			
			for commentWord in comment_text:
				for word in self.comment_words:
					
					#
					author = str(comment.author).lower()
					self.bot_name =  self.bot_name.lower()
					if word == commentWord and comment.id not in self.cache\
					 and author != self.bot_name:
						print("Comment found, ID: " + comment.id)
						print ('Replying...')
						comment.reply("We are now in a spidey thread!")
						print ('Writing Comment ID to Cache')
						
						# add comment id to cache and cache file simultaneously
						self.cache.append(comment.id)
						
						# Updates cache file with new comment ID
						print ('Updating cache file...')				
						with open(self.cache_file, 'w+') as f:
							for item in self.cache:
								f.write(item + '\n')
						
						print ('Cache Updated')
					

	def runbot(self):
		''' 
		Function to run bot.
		'''
		
		
		# Creates temp cache storage
		self.cache_create()
		
		# Subreddits to be checked	
		print("Grabbing subreddits...")
		
		for subreddit in self.subreddits:
			self.subredditstring += subreddit + '+'
		
		self.subredditstring.rstrip('+')
		
		self.subreddit = self.r.get_subreddit(self.subredditstring)
		
		# Searches comments
		self.comment_search()

		# Used to stop bot for certain amount of time to not 
		# overload the server		
		time.sleep(30)

def main():
	
	bot = Bot('commentIDcache.txt')
	bot.comment_words.extend(['spidey', 'spiderman'])
	bot.comment_reply = 'Progects bot checking in on the real spidey'
	bot.subreddits.extend(['test'])
	
	i = 0
	while True:
		bot.runbot()
		i += 1
		print ('Iteration: {0}'.format(i))


if __name__ == '__main__':
    main()
