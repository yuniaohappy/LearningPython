import configparser
config = configparser.ConfigParser()
# config["DEFAULT"] = {"ServerAliveInterval":"45",
#                      "Compression":"yes",
#                      "CompressionLevel":"9"}
# config["bitbucket.org"] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecreter = config['topsecret.server.com']
# topsecreter['Host Port'] = '50022'
# topsecreter['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open("config.ini","w") as conf:
#     config.write(conf)

config.read("config.ini")
# config.sections()
# print(config["DEFAULT"]["serveraliveinterval"])
# for key in config["DEFAULT"]:
#     print(key,"\t",config["DEFAULT"][key])
config.set("DEFAULT","compression",'no')
config.write(open("config.ini","w"))

# config.remove_section("topsecret.server.com")
# config.write(open("config_remove.ini","w"))




