class ParserClass():

    def __init__(self, data):
        self.data = data
        self.terms = ['C++', 'C#', 'Python', 'SQL', 'HTML', 'CSS', 'Perl', 'JavaScript', 'Mongo']

    def check(self):
        """check if term (languages) are in messages"""
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
