import time
import praw
r = praw.Reddit("Python:Gears 4 related post monitor:v1.0 (by /u/perry_the_blu_herron)")
r.login()
already_done = []

prawWords = ["gears 4", "beta", "multiplayer", "gears of war 4"]

while True:
    subreddit = r.get_subreddit("gearsofwar")
    for submission in subreddit.get_hot(limit=10):
        # Test if it contains a gears 4-related post
        op_text = submission.title.lower()
        has_praw = any(string in op_text for string in prawWords)
        if submission.id not in already_done and has_praw:
            print "Post found."
            msg = "[GEARS related thread](%s)" % submission.short_link
            r.send_message("perry_the_blu_herron", "Gears 4 Thread", msg)
            already_done.append(submission.id)
    time.sleep(600)# test again in 10 minutes
