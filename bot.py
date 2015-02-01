import praw
import time


class Bot():
	
	# List of words the bot will reply to
	words_to_match = ['bison']
					
	def __init__(self):
		''' Logs the bot into Reddit'''
		
		self.r = praw.Reddit(user_agent = "Test bot for /r/progects by /u/NEET_Here and /u/triple-take")

		# store user for later use, but not password
		self.botName = input("Username: ")
		print("Logging in...")
		self.r.login(username=self.botName)


		print("Successfull login...")
		



	def runbot(self, botName):
		''' Function to run bot. The argument botName is the Reddit
		username of the bot'''
		
		# Temporary cache storage
		cache = []
		
		# Cache file where comment Id's are stored
		f = open("commentIDcache.txt", "+r")
		print ("Opening file for already replied comments...")
		
		# Updates cache list
		for line in f:
			cache.append(line)
		
			
		print("Grabbing subreddit...")
		subreddit = self.r.get_subreddit("test")
		comments = subreddit.get_comments(limit=25)

		# Search through comments, if a match is found reply
		# unless the user has already replied or if the comment
		# is by the user.
		for comment in comments:
			print("Reading comment...")
			comment_text = comment.body.lower().split(' ')
			for commentWord in comment_text:
				for word in self.words_to_match:
					author = str(comment.author).lower()
					botName =  botName.lower()
					if word == commentWord and comment.id not in f.read().replace('\n', '')\
					 and author != botName:
						print("Comment found, ID: " + comment.id)
						print ('Replying...')
						comment.reply("You are the last airbender.")
						print ('Writing Comment ID to Cache')
						
						# add comment id to cache and cache file simultaneously
						cache.append(comment.id)
						f.write(comment.id + "\n")
						
						# Reset the read function.
						# f.read() reads till the end of the text file
						# and stops there.
						f.seek(0)
						print ('Cache Updated')
						
						# rate exception avoided here
						time.sleep(5)
		f.close()
		time.sleep(10)

def main():
	bot = Bot()
	while True:
		# Argument for bot.runbot is username
		bot.runbot('progects_bot1')

if __name__ == '__main__':
	main()
