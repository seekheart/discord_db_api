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
          self.collection = 'pros'
          self.client = pymongo.MongoClient(self.host, self.port)

          try:
               self.db_cursor = self.client[self.db_name].create_collection(self.collection)
          except:
               pass
          finally:
               self.db_cursor = self.client[self.db_name].get_collection(self.collection)

     def get_users(self, lang):
          """
          Queries list of pros for a given language.

          Parameters
          --------------
          lang : string
              the language to query

          Returns
          ----------
          result : list
              list of pros
          """

          users_li = self.db_cursor.find_one({},{lang: True})
          result = users_li[lang]
          return result

     def add_user(self, username, skills):
          """ Remember to implement Check"""
          for lang in skills:
               self.db_cursor.update({}, {'$push' :{lang : username}})

     def _del_user(self, username, skills):
          """ Remember to implement Check"""
          for lang in skills:
               self.db_cursor.update({}, {'$pull' :{lang : username}})



#Test out class
# my_db = db('localhost', 27017, 'helpTest')
# my_db.get_users('python')
# my_db.add_user('seekheart', ['abc', 'git'])
# my_db._del_user('seekheart', ['abc', 'git'])
