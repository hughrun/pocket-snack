pocket_consumer_key = ''
pocket_redirect_uri = 'https://hugh.li/success'
items_per_cycle = 10
archive_tag = 'TBR' # apply this tag before archiving items
ignore_faves = True # don't archive items that are favorited
replace_all_tags = False # if set to True this will replace ALL tags on an item in the user's List with the archive_tag and anything in exclude_tags. If set to False, the archive tag is still added but any existing tags are retained.
exclude_tags = ['GLAM Blog Club', 'aus glam blogs', 'empocketer'] # if replace_all_tags is set to True, you can still retain particular tags by adding them to the exclude_tags list
longreads_wordcount = 3000 # if there are more than this many words, the article will be classified as a 'long read'
num_videos = None # if you change this to an integer this many items_per_cycle will be videos (if there are any videos in your list)
num_images = None # if you change this to an integer this many items_per_cycle will be images (if there are any images in your list)
num_longreads = 2 # if this is an integer this many items_per_cycle will be longreads (if there are any longreads in your list). If all your items are longreads you will still get the total items_per_cycle. Change to False if you don't want to filter longreads
# ensure the last line is blank so that authorisation token is stored correctly