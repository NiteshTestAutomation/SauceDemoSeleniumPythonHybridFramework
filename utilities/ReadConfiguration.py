from configparser import ConfigParser

def read_Configuaration(category,key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    #return category
    return config.get(category,key)
