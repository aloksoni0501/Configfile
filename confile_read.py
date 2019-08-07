from configparser import ConfigParser



parser = ConfigParser()
parser.read('Datafile.ini')
print(parser.sections())
print(parser.get('db'))

