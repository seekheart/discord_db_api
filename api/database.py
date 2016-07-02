#!/usr/bin/env python
"""
Discord Database Class
"""

import pymongo

class db():
     """Our database class will be constructed"""
     def __init__(self, host, port, name):
          self.host = host
          self.port = port
          self.db_name = name
          self.collection = 'help_directory'
          self.client = pymongo.MongoClient(self.host, self.port)

          try:
               self.db_cursor = self.client[self.db_name].create_collection(self.collection)
          except:
               pass
          finally:
               self.db_cursor = self.client[self.db_name].get_collection(self.collection)

     def get_users(self, lang):
          users_li = self.db_cursor.find_one({'language' : lang})['users']
          return '\n'.join([user['username'] for user in users_li])

     def _add_user(self, username, skills):
          record = {username: skills}
          self.db_cursor.insert_one(record)





my_db = db('localhost', 27017, 'helpTest')

print(my_db.get_users('German'))
my_db._add_user('Exodus111', ['python'])