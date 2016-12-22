#coding=utf-8

class LoginData:
    __id = None
    __name = None
    __type = None
    
    def __init__(self, uid, login_name, name):
        self.__id = uid
        self.__login_name = login_name
        self.__name = name

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.__id)
    
    def get_login_name(self):
        return self.__login_name
    
    def get_name(self):
        return self.__name
    
