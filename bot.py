import praw
import pdb
import re
import os

reddit=praw.Reddit('Bot1')
# subreddit=reddit.subreddit("globaloffensive")
# for submission in subreddit.hot(limit=5):
# 	print("Title: ", submission.title)
	
# 	print("Score: ", submission.score)
# 	print("---------------------------------\n")

# reddit.login("Bot_county", "redditgod")

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('globaloffensive')
for submission in subreddit.hot(limit=20):
    print(submission.title)
   
    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:
        print("ff")
        # Do a case insensitive search
        if re.search("bots", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("WE bots are gonna rule you all")
            print("Bot replying to : ", submission.title)
            # Store the current id into our list
            posts_replied_to.append(submission.id)
            break

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
