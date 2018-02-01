import getpass

from deregnet_rest.resources.redis import RedisServer
from deregnet_rest.resources.mongodb import MongoD
from deregnet_rest.resources.mongodb import Database
from deregnet_rest.controllers.runners import Runner


class Server:
    def __init__(self, database, redis_server):
        self._db = database
        self._redis = redis_server
        # TODO: factor into method
        NUM_RUNNERS = 2
        self._runners = []
        for runner_id in range(NUM_RUNNERS):
            log_file = 'data/runners/runner'+str(runner_id)+'.log'
            self._runners.append(
                                  Runner(database.config,
                                         database.mongod,
                                         self.redis,
                                         runner_id,
                                         20,
                                         log_file)
                                 )

        # TODO: implement run dependency graph
        self._run_deps = None

    @property
    def db(self):
        return self._db

    @property
    def mongod(self):
        return self._db.mongod

    @property
    def redis(self):
        return self._redis

    @property
    def graphs(self):
        return self._db._graphs

    @property
    def scores(self):
        return self._db._scores

    @property
    def nodesets(self):
        return self._db._nodesets

    @property
    def parameter_sets(self):
        return self._db._parameter_sets

    @property
    def runs(self):
        return self._db._runs

    @property
    def subgraphs(self):
        return self._db._subgraphs

    @property
    def run_dependency(self):
        return self._run_deps


def init_server(path2conf):
    path2redis_conf = 'server/config/redis.conf'
    redis_bindir = '/opt/redis/4.0.2/bin'
    redis_server = RedisServer(path2redis_conf, redis_bindir)
    return Server(get_database({}, redis_server),
                  redis_server)

def get_database(conf, redis_server):
    #user = getpass.getpass(prompt='User: ')
    user = 'deregnet_rest_server'
    #passwd = getpass.getpass(prompt='Password: ')
    passwd = 'deregnet'
    path2conf = 'server/config/mongod.conf'
    mongod_bindir = '/usr/bin'
    return Database(user,
                    passwd,
                    MongoD(path2conf, mongod_bindir),
                    redis_server)
