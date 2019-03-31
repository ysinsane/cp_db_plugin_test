This proj is used to test cherrpy plugin over multipe requests.


conclusion: can not store some client's db_engine in plugin class, the data in certain 
plugin class is application level.

solution: we can store a list or dict of engines, providing 'engine_set','engine_del',
'engine_get' channels for certain request from customer. Even more, I can encapsulate a class to
provide CRUD funtion instead of engine.