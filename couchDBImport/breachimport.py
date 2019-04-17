# fancy import breach compilation into couchDb
# by freakyclown - fc@redactedfirm.com

# note: you might need to rm .DS_Store from the data directory to avoid fud in your db
# note: you will need to go into data/symbols and delete the line with crap in, its about 30 lines down
# note: this data was not cleaned well before being compiled.


# import the regular expression stuff for splitting lines and
# the os stuff for walking the directory, oh and couchdb
# requirements - pip install couchdb

import re
import os
import couchdb

#put in your server details and user/password combo
user = 'username'
password = 'password'
couchserver = couchdb.Server("http://%s:%s@127.0.0.1:5984" % (user, password))

#give your database a name
dbname = "namehere"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)


#open the file and process it a line at a time
def processor(filepath):
    with open(filepath) as f:
        for line in f:
            #yay another hack, lets split on ; and : because people cant sanitise data, also lets decode it sensibly because of symbols
            cleaved = re.split('[:;]',line.rstrip().decode('latin-1'))
            try:
                email = cleaved[0]
            except IndexError:
                # just incase it goes wrong put something in at least
                email = "empty_here"
            try:
                password = cleaved[1]
            except IndexError:
                password = "empty_here"


            #process the line
            #couch will auto make the docid and revision so we just save what we have
            db.save({"email":email, "password":password})

def dothething():
    for subdir, dirs, files in os.walk("data/"):
        for file in files:
            filepath = subdir + os.sep + file
            processor(filepath)

dothething()
