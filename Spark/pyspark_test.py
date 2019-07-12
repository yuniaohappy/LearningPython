# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName('spark_test').getOrCreate()
# people = spark.read.json('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\people.json')\
#     .createOrReplaceGlobalTempView('people')
# print(type(people))
# user = spark.read.parquet('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\users.parquet').show()
# user.select('user').show()
# people.select().show()
# spark.sql('select * from people').show()
# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("First_App")
# sc = SparkContext(conf=conf)
#
# data = sc.parallelize(range(10))
# ans = data.reduce(lambda x, y: x + y)
# print (ans)
#
# lines = sc.textFile("D:\spark-2.3.3-bin-hadoop2.7\README.md")
# print (lines.count())
# print (lines.first())


py = """
absl-py                     0.2.0                  
alembic                     1.0.0                  
amqp                        2.3.2                  
apispec                     1.2.0                  
appdirs                     1.4.3                  
asn1crypto                  0.24.0                 
astor                       0.6.2                  
async-generator             1.10                   
attrs                       17.4.0                 
Automat                     0.7.0                  
Babel                       2.6.0                  
bcrypt                      3.1.5                  
beautifulsoup4              4.6.0                  
billiard                    3.5.0.4                
bitarray                    0.8.3                  
bleach                      1.5.0                  
botocore                    1.12.71                
cachetools                  3.0.0                  
captcha                     0.3                    
castellan                   1.0.0                  
celery                      4.2.0                  
certifi                     2018.8.24              
certipy                     0.1.3                  
cffi                        1.11.5                 
chardet                     3.0.4                  
click                       6.7                    
cliff                       2.14.0                 
cmd2                        0.9.6                  
cntk                        2.7                    
colorama                    0.3.9                  
comtypes                    1.1.4                  
constantly                  15.1.0                 
contextlib2                 0.5.5                  
croniter                    0.3.26                 
cryptography                2.4.2                  
cssselect                   1.0.3                  
cx-Oracle                   7.1.2                  
cycler                      0.10.0                 
DateTime                    4.3                    
debtcollector               1.20.0                 
decorator                   4.3.0                  
defusedxml                  0.5.0                  
Django                      2.0.7                  
dnspython                   1.16.0                 
docopt                      0.6.2                  
docutils                    0.14                   
dogpile.cache               0.6.8                  
dominate                    2.3.5                  
dukpy                       0.2.0                  
editdistance                0.5.3                  
entrypoints                 0.2.3                  
enum34                      1.1.6                  
et-xmlfile                  1.0.1                  
eventlet                    0.24.1                 
extras                      1.0.0                  
facets                      1.1.0                  
fasteners                   0.14.1                 
fix-yahoo-finance           0.0.21                 
fixtures                    3.0.0                  
Flask                       1.0.2                  
Flask-AppBuilder            1.12.3                 
Flask-Babel                 0.11.1                 
Flask-Bootstrap             3.3.7.1                
Flask-Caching               1.4.0                  
Flask-Compress              1.4.0                  
Flask-Login                 0.4.1                  
Flask-Migrate               2.1.1                  
Flask-Moment                0.7.0                  
Flask-OpenID                1.2.5                  
Flask-SQLAlchemy            2.3.2                  
flask-talisman              0.7.0                  
Flask-WTF                   0.14.2                 
funcsigs                    1.0.2                  
future                      0.16.0                 
futurist                    1.8.0                  
gast                        0.2.0                  
geopy                       1.11.0                 
graphviz                    0.8.4                  
greenlet                    0.4.15                 
grpcio                      1.11.0                 
gunicorn                    19.8.0                 
h5py                        2.9.0                  
hdfs                        2.2.2                  
html5lib                    0.9999999              
http-client                 0.1.22                 
humanize                    0.5.1                  
hyperlink                   19.0.0                 
idna                        2.6                    
igraph                      0.1.11                 
impyla                      0.15.0                 
incremental                 17.5.0                 
interface-meta              1.1.0                  
ipykernel                   4.8.2                  
ipython                     6.2.1                  
ipython-genutils            0.2.0                  
ipywidgets                  7.1.2                  
iso8601                     0.1.12                 
isodate                     0.6.0                  
itsdangerous                0.24                   
javascripthon               0.10                   
jdcal                       1.3                    
jedi                        0.11.0                 
jieba                       0.39                   
Jinja2                      2.10                   
jmespath                    0.9.3                  
json5                       0.8.5                  
jsonpatch                   1.23                   
jsonpointer                 2.0                    
jsonschema                  3.0.1                  
jupyter                     1.0.0                  
jupyter-client              5.2.2                  
jupyter-console             5.2.0                  
jupyter-core                4.4.0                  
jupyter-echarts-pypkg       0.1.1                  
jupyter-tensorboard         0.1.8                  
jupyterhub                  1.0.0                  
jupyterlab                  1.0.1                  
jupyterlab-server           1.0.0                  
Keras                       2.2.4                  
Keras-Applications          1.0.7                  
Keras-Preprocessing         1.0.9                  
keystoneauth1               3.11.2                 
keystonemiddleware          5.3.0                  
kombu                       4.2.1                  
lightgbm                    2.2.2                  
linecache2                  1.0.0                  
lml                         0.0.2                  
lxml                        4.1.1                  
macropy3                    1.1.0b2                
Mako                        1.0.7                  
Markdown                    3.0                    
MarkupSafe                  1.0                    
matplotlib                  2.1.2                  
memory-profiler             0.55.0                 
microversion-parse          0.2.1                  
mistune                     0.8.3                  
mock                        2.0.0                  
monotonic                   1.5                    
mox3                        0.26.0                 
msgpack                     0.6.0                  
multitasking                0.0.5                  
munch                       2.3.2                  
mxnet                       1.3.0                  
mysql-connector             2.2.9                  
mysql-connector-python      8.0.15                 
mysqlclient                 1.3.12                 
nbconvert                   5.3.1                  
nbformat                    4.4.0                  
nester                      1.1.0                  
netaddr                     0.7.19                 
netifaces                   0.10.7                 
nltk                        3.4                    
nodejs                      0.1.1                  
notebook                    5.4.0                  
npm                         0.1.1                  
numexpr                     2.6.4                  
numpy                       1.16.2                 
oauthlib                    3.0.1                  
omniduct                    1.1.2                  
openpyxl                    2.5.1                  
openstacksdk                0.22.0                 
optional-django             0.1.0                  
oracle2postgres             0.1.6                  
os-client-config            1.31.2                 
os-service-types            1.4.0                  
osc-lib                     1.11.1                 
oslo.cache                  1.31.2                 
oslo.concurrency            3.29.0                 
oslo.config                 6.7.0                  
oslo.context                2.22.0                 
oslo.db                     4.42.0                 
oslo.i18n                   3.23.0                 
oslo.log                    3.42.1                 
oslo.messaging              9.3.0                  
oslo.middleware             3.37.0                 
oslo.policy                 1.43.1                 
oslo.rootwrap               5.15.1                 
oslo.serialization          2.28.1                 
oslo.service                1.33.0                 
oslo.upgradecheck           0.1.1                  
oslo.utils                  3.39.0                 
oslotest                    3.7.0                  
pamela                      1.0.0                  
pandas                      0.24.2                 
pandocfilters               1.4.2                  
paramiko                    2.4.2                  
parsedatetime               2.0                    
parsel                      1.5.1                  
parso                       0.1.0                  
Paste                       3.0.5                  
PasteDeploy                 2.0.1                  
pathlib2                    2.3.0                  
pbr                         5.1.1                  
pdfminer3k                  1.3.1                  
pickleshare                 0.7.4                  
Pillow                      5.2.0                  
pip                         19.1.1                 
pluggy                      0.6.0                  
ply                         3.11                   
polyline                    1.3.2                  
prettytable                 0.7.2                  
progressbar2                3.39.3                 
prometheus-client           0.7.1                  
prompt-toolkit              1.0.15                 
protobuf                    3.5.2.post1            
psutil                      5.6.3                  
psycopg2                    2.8.1                  
pure-sasl                   0.4.0                  
py                          1.7.0                  
py4j                        0.10.7                 
pyasn1                      0.4.4                  
pyasn1-modules              0.2.5                  
pycadf                      2.8.0                  
pycparser                   2.19                   
pycurl                      7.43.0.2               
PyDispatcher                2.0.5                  
pydot                       1.4.1                  
pydruid                     0.5.0                  
pyecharts                   0.5.5                  
pyecharts-javascripthon     0.0.6                  
pyecharts-jupyter-installer 0.0.3                  
Pygments                    2.2.0                  
PyGreSQL                    5.0.6                  
PyHamcrest                  1.9.0                  
PyHDFS                      0.2.1                  
PyHive                      0.5.0                  
PyMySQL                     0.8.0                  
PyNaCl                      1.3.0                  
pyOpenSSL                   18.0.0                 
pyparsing                   2.2.0                  
pyperclip                   1.7.0                  
PyQt5                       5.10.1                 
pyreadline                  2.1                    
pyrsistent                  0.15.2                 
pyspark                     2.4.0                  
pytest                      3.4.1                  
python-ambariclient         0.6.0                  
python-barbicanclient       4.8.0                  
python-cinderclient         4.1.0                  
python-dateutil             2.8.0                  
python-editor               1.0.3                  
python-glanceclient         2.15.0                 
python-heatclient           1.16.1                 
python-keystoneclient       3.18.0                 
python-manilaclient         1.25.0                 
python-mimeparse            1.6.0                  
python-neutronclient        6.11.0                 
python-novaclient           11.1.0                 
python-subunit              1.3.0                  
python-swiftclient          3.6.0                  
python-utils                2.3.0                  
python3-openid              3.1.0                  
pytz                        2018.9                 
pywifi                      1.1.10                 
pywinpty                    0.5.1                  
PyYAML                      3.13                   
pyzmq                       18.0.2                 
qtconsole                   4.3.1                  
queuelib                    1.5.0                  
repoze.lru                  0.7                    
requests                    2.20.0                 
requestsexceptions          1.4.0                  
retry                       0.9.2                  
rfc3986                     1.2.0                  
Routes                      2.4.1                  
sahara                      10.0.0                 
sahara-plugin-ambari        1.0.0                  
sasl                        0.2.1                  
scikit-learn                0.19.1                 
scipy                       1.0.0                  
Scrapy                      1.6.0                  
seaborn                     0.8.1                  
selenium                    3.141.0                
Send2Trash                  1.5.0                  
service-identity            18.1.0                 
setuptools                  41.0.1                 
simplegeneric               0.8.1                  
simplejson                  3.15.0                 
singledispatch              3.4.0.3                
sip                         4.19.8                 
six                         1.12.0                 
SQLAlchemy                  1.3.2                  
sqlalchemy-migrate          0.11.0                 
SQLAlchemy-Utils            0.32.21                
sqlparse                    0.2.4                  
statsd                      3.3.0                  
statsmodels                 0.9.0                  
stestr                      2.2.0                  
stevedore                   1.30.0                 
tables                      3.4.2                  
Tempita                     0.5.2                  
tenacity                    5.0.2                  
tensorboard                 1.7.0                  
tensorflow                  1.7.0                  
tensorflow-tensorboard      1.5.1                  
termcolor                   1.1.0                  
terminado                   0.8.1                  
testpath                    0.3.1                  
testresources               2.0.1                  
testscenarios               0.5.0                  
testtools                   2.3.0                  
thrift                      0.11.0                 
thrift-sasl                 0.3.0                  
thriftpy2                   0.4.0                  
tooz                        1.63.1                 
torch                       1.0.1                  
torchvision                 0.2.2.post3            
tornado                     6.0.3                  
traceback2                  1.4.0                  
traitlets                   4.3.2                  
Twisted                     19.2.1                 
unicodecsv                  0.14.1                 
unittest2                   1.1.0                  
urllib3                     1.22                   
vine                        1.1.4                  
visitor                     0.1.3                  
voluptuous                  0.11.5                 
w3lib                       1.20.0                 
warlock                     1.3.0                  
wcwidth                     0.1.7                  
webencodings                0.5.1                  
WebOb                       1.8.4                  
Werkzeug                    0.14.1                 
wheel                       0.31.0                 
widgetsnbextension          3.1.4                  
wordcloud                   1.5.0                  
wrapt                       1.10.11                
WTForms                     2.2.1                  
WTForms-JSON                0.3.3                  
xgboost                     0.81                   
xlrd                        1.1.0                  
zmq                         0.0.0                  
zope.interface              4.6.0                  
"""

lit = py.replace('\n','').split(' ')
lit1 = []
for i in lit:
    if i == '':
        pass
    else:
        lit1.append(i)
res = []
for i in range(len(lit1)-1):
    if i % 2 == 0:
        res.append(str(lit1[i ] + '==' + lit1[i+1]))
with open('C:\\Users\\Li Peng\\res.txt','w') as f :
    for i in res:
        f.write(i + '\n')
print(res)









