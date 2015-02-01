import praw
import time


class Bot():
	
	# List of words the bot will reply to
	words_to_match = ['bison']
					
	def __init__(self, cacheFile):
		self.cacheFile = cacheFile
		''' Logs the bot into Reddit'''
		
		self.r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

		# store user for later use, but not password
		self.botName = input("Username: ")
		print("Logging in...")
		self.r.login(username=self.botName)


		print("Successfull login...")
		

	def cacheCreate(self, cacheFile):
		""" Imports stored Comment ID's into temporary cache"""
		self.cache = []
		with open(self.cacheFile, 'r') as f:
			for line in f.read():
				line = line.rstrip('\n')
				self.cache.append(line)
				

	def runbot(self):
		''' Function to run bot'''
		
		# Create cache of comment ID's
		self.cacheCreate(self.cacheFile)
		
			
		print("Grabbing subreddit...")
		subreddit = self.r.get_subreddit("test")
		comments = subreddit.get_comments(limit=25)

		# Search through comments, if a match is found reply
		# unless the user has already replied or if the comment
		# is by the user.
		for comment in comments:
			print("Reading comment...")
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
						comment.reply("You are the last airbender.")
						print ('Writing Comment ID to Cache')
						
						# add comment id to cache and cache file simultaneously
						self.cache.append(comment.id)
						
						print ('Cache Updated')
						
						# rate exception avoided here
						time.sleep(5)
						
		# Updates cache file with new items				
		with open(self.cacheFile, 'w+') as f:
			for item in self.cache:
				f.write(item + '\n')
				
		time.sleep(10)

def main():
	# Add in cache file upon creation of class object
	bot = Bot('commentIDcache.txt')
	
	while True:
		bot.runbot()

if __name__ == '__main__':
	main()
