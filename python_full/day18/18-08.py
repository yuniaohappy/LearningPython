import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {"ServerAliveInterval":"45",
                     "Compression":"yes",
                     "CompressionLevel":"9"}
config["bitbucket.org"] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecreter = config['topsecret.server.com']
topsecreter['Host Port'] = '50022'
topsecreter['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'

with open("config.ini","w") as conf:
    config.write(conf)