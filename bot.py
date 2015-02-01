import praw
import time


class Bot():
	
	# Cache storage
	cache = []
	
	# List of words the bot will reply to
	words_to_match = ['bison', 'spiderman']
					
	def __init__(self, cacheFile):
		self.cacheFile = cacheFile
		''' Logs the bot into Reddit'''
		
		self.r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

		# store user for later use, but not password
		# self.botName = input("Username: ")
		self.botName = 'progects_bot1'
		self.password = 'B0tP@ssword'
		print("Logging in...")
		self.r.login(self.botName, self.password)


		print("Successfull login...")
		
		
	def cacheCreate(self):
		''' Pulls information from file and creates cache'''
		with open(self.cacheFile, 'r') as f:
			self.cache = f.read().split('\n')
			self.cache = [x for x in self.cache if x != '']
					

	def runbot(self):
		''' Function to run bot'''
		
		
		# Creates temp cache storage
		self.cacheCreate()
		
			
		print("Grabbing subreddit...")
		subreddit = self.r.get_subreddit("test")
		comments = subreddit.get_comments(limit=25)

		# Search through comments, if a match is found reply
		# unless the user has already replied or if the comment
		# is by the user.
		
		print("Reading comments...")
		for comment in comments:
			comment_text = comment.body.lower().split(' ')
			comment_text = [x.strip('?!@#$%^&*"') for x in comment_text]
			for commentWord in comment_text:
				for word in self.words_to_match:
					author = str(comment.author).lower()
					self.botName =  self.botName.lower()
					if word == commentWord and comment.id not in self.cache\
					 and author != self.botName:
						print("Comment found, ID: " + comment.id)
						print ('Replying...')
						comment.reply("We are now in a spidey thread!")
						print ('Writing Comment ID to Cache')
						
						# add comment id to cache and cache file simultaneously
						self.cache.append(comment.id)
						
						# Updates cache file with new comment ID
						print ('Updating cache file...')				
						with open(self.cacheFile, 'w+') as f:
							for item in self.cache:
								f.write(item + '\n')
						
						print ('Cache Updated')
						
						# rate exception avoided here
						time.sleep(5)

				
		time.sleep(10)

def main():
	# Add in cache file upon creation of class object
	bot = Bot('commentIDcache.txt')
	i = 0
	while True:
		bot.runbot()
		i += 1
		print ('Iteration: {0}'.format(i))


if __name__ == '__main__':
    main()
