"""
Parser Class
"""

from terms import terms

class Parser():

    def __init__(self, data):
        """
        Constructor method

        Parameters
        ---------------
        Data - {message : user}

        Returns
        -------------
        Nothing
        """
        self.data = data
        self.terms = terms

    def check(self):
        """
        check if term (languages) in messages and return
        a list of users

        Parameters
        ----------------
        Takes nothing

        Returns
        -----------------
        Nothing
        """
        users = []

        for data in self.data:
            result = { 'membership': []}
            user = data["user"]
            message = data["message"]

            for term in self.terms:
                if term in message:
                    result["user"] = user
                    result["membership"].append(term)
            users.append(result)
        return users
