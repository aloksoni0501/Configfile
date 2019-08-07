from configparser import ConfigParser


config = ConfigParser()

config['setting'] = {
    'debug': 'true',
    'Secret_Key': 'alok@123',
    'log_path': '/my_app/log'
}

config['db'] = {
    'db_app': 'myapp_dev',
    'db_post': 'localhost',
    'db_port': 8889
}
config['titles'] = {
    'use_con': 'false',
    'image_path': '/myapp/image'


}

with open('./Datafile.ini', 'w') as f:
    config.write(f)