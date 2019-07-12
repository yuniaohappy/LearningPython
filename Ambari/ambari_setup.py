import json
import argparse
import requests


class AmbariSetup(object):
    def __init__(self, host, port, username, password, clustername, blueprintname):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.clustername = clustername
        self.blueprintname = blueprintname
        self.headers = {"X-Requested-By": "ambari"}

    def blue_print(self):
        with open('./json/blueprint.json', 'r') as blue_file:
            blue_print_json = json.loads(blue_file.read(), encoding='utf-8')
            blue_print_json['Blueprints']['blueprint_name'] = self.blueprintname
            return json.dumps(blue_print_json)

    def hdp(self):
        with open('./json/hdp.json', 'r') as hdp_file:
            hdp = json.loads(hdp_file.read(), encoding='utf-8')
            return json.dumps(hdp)

    def hdputils(self):
        with open('./json/hdputils.json', 'r') as hdputiles_file:
            hdputiles = json.loads(hdputiles_file.read(), encoding='utf-8')
            return json.dumps(hdputiles)

    def hostmapping(self):
        with open('./json/hosts.json', 'r') as hostmapping_file:
            hostmap = json.loads(hostmapping_file.read(), encoding='utf-8')
            hostmap['blueprint'] = self.blueprintname
            hostmap['default_password'] = 'lp'
            return json.dumps(hostmap)

    def get_url(self, name):
        if name == 'blueprint':
            bule_print_url = 'http://{host}:{port}/api/v1/blueprints/{blueprintname}?validate_topology=false' \
                .format(host=self.host, port=self.port, blueprintname=self.blueprintname)
            return bule_print_url
        elif name == 'cluster':
            cluster_url = 'http://{host}:{port}/api/v1/clusters/{clustername}' \
                .format(host=self.host, port=self.port, clustername=self.clustername)
            return cluster_url
        elif name == 'hdp':
            hdp_url = 'http://{host}:{port}/api/v1/stacks/HDP/versions/2.5/operating_systems/redhat7/repositories/HDP-2.5' \
                .format(host=self.host, port=self.port)
            return hdp_url
        elif name == 'hdputils':
            hdputils_url = 'http://{host}:{port}/api/v1/stacks/HDP/versions/2.5/operating_systems/redhat7/repositories/HDP-UTILS-1.1.0.21' \
                .format(host=self.host, port=self.port)
            return hdputils_url
        else:
            print(name, 'URL错误！！！')
            return None


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Ambari 配置参数')
    ap.add_argument('--host', help='Ambari IP 地址', default='20.5.194.62')
    ap.add_argument('--port', help='Ambari 端口号', default='8080')
    ap.add_argument('--username', help='Ambari 用户名', default='admin')
    ap.add_argument('--password', help='Ambari 密码', default='admin')
    ap.add_argument('--clustername', help='Ambari 名称', default='ambari_lp')
    ap.add_argument('--blueprintname', help='bluprint 名称', default='ambari_lp')
    args = ap.parse_args()

    ambari = AmbariSetup(args.host, args.port, args.username, args.password, args.clustername, args.blueprintname)

    # 获取已经创建好的集群blueprint
    # url = 'http://{host}:{port}/api/v1/clusters/{clusterName}?format=blueprint'\
    #     .format(host=ambari.host,port=ambari.port,clusterName=ambari.clustername)
    # blueprint3node = requests.get(url,headers = ambari.headers,auth=(ambari.username, ambari.password))
    # data = json.loads(blueprint3node.text,encoding='utf-8')
    # with open('./json/blueprint3node.json','w') as f:
    #     f.write(json.dumps(data,indent=True))

    # print('第一步：创建和配置集群蓝图请求，开始。。。。')
    print(ambari.get_url('blueprint'))
    # blueprint = requests.post(ambari.get_url('blueprint'),json=ambari.blue_print(),headers = ambari.headers,auth=(ambari.username, ambari.password))
    # print(blueprint.text)

    # print('第二步：创建本地HDP存储库请求（可以执行多次创建不同操作系统类型的本地库），开始。。。。')
    print(ambari.get_url('hdp'))
    print('http://20.5.194.63:8080/api/v1/stacks/HDP/versions/2.5/operating_systems/redhat7/repositories/HDP-2.5')

    # hdp = requests.post(ambari.get_url('hdp'), json=ambari.hdp(), headers=ambari.headers,
    #                     auth=(ambari.username, ambari.password))
    # print(hdp.text)
    # print('第三步：创建本地HDP-UTILS存储库请求（可以执行多次创建不同操作系统类型的本地库）')
    print(ambari.get_url('hdputils'))

    # hdp_utils_url = requests.post(ambari.get_url('hdputils'), json=ambari.hdputils(), headers=ambari.headers,
    #                               auth=(ambari.username, ambari.password))
    # print(hdp_utils_url.text)

    # print('第四步：使用创建好的蓝图安装部署集群')
    print(ambari.get_url('cluster'))
    # host_mapping_url = requests.post(ambari.get_url('cluster'),json=ambari.hostmapping(),headers = ambari.headers,auth=(ambari.username, ambari.password))
    # print(host_mapping_url.text)
