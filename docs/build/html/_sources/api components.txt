Api Components
=====

The following section contains description of all the components involved in the Discord Bot Api.

Discord Bot
-----
The bot class uses the discord api provided by `Rapptz <https://github.com/Rapptz/discord.py>`_ to do the actual chat room service. For the backend the bot invokes the database class (more info in database class description) to quickly query and return a message of all users with expertise in a language requested by user.

.. automodule:: bot
    :members:

Database
-------------
The database class uses a MongoDB backend that is handled by the PyMongo library. In the bot class the database object is instantiated globally and the connection to the database is opened until termination or logout of the bot.

.. automodule:: database
    :members:

Parser
------------
The parser class is used to parse user massages and extract out languages to associate with username. Typically it is used to populate the database.

.. automodule:: user_parser
.. autoclass:: Parser
    :members: