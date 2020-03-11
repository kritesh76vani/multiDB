class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes','CustomUsers'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to default.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to default.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        db_list = ('default', 'database1', 'database2','database3','database4','database5')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'default' database.
        """

        if db == 'default':
            # Migrate Django core app models if current database is default
            if app_label in ['auth','admin','sessions','contenttypes','CustomUsers']:
                return True            
            else:
                # Non Django core app models should not be migrated if database is default
                return False
        # Other database should not migrate Django core app models            
        elif app_label in ['auth','admin','sessions','contenttypes','CustomUsers']:
            return False
        # Otherwise no opinion, defer to other routers or default database
        

        else:
            return True

        if app_label in self.route_app_labels:
            return db == 'default'

        return None


#########################################################################################

class RouterDB1(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'database1'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Products':
            return 'database1'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database1':
            return model._meta.app_label == 'Products'
        elif model._meta.app_label == 'database1':
            return False
        return None

class RouterDB2(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'database2'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Products':
            return 'database2'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database2':
            return model._meta.app_label == 'database2'
        elif model._meta.app_label == 'database2':
            return False
        return None


class RouterDB3(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'database3'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Products':
            return 'database3'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database3':
            return model._meta.app_label == 'database3'
        elif model._meta.app_label == 'database3':
            return False
        return None

class RouterDB4(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'database4'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Products':
            return 'database4'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database4':
            return model._meta.app_label == 'database4'
        elif model._meta.app_label == 'database4':
            return False
        return None

class RouterDB5(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Products':
            return 'database5'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'Products':
            return 'database5'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database5':
            return model._meta.app_label == 'database5'
        elif model._meta.app_label == 'database5':
            return False
        return None