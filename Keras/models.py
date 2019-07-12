import json
import pprint
class Hosts(object):
    def __init__(self):
        self.hosts = {'20.5.194.63':'vm-5.novalocal','20.5.194.55':'vm-6.novalocal','20.5.194.58':'vm-7.novalocal'}
    def add_hosts(self):
        return dict(self.hosts)

# 配置blueprint的json数据
class BluePrint(object):
    BLUEPRINT_DATA = ''
    def __init__(self,buleprint_name,stack_name='HDP',stack_version='2.5'):
        with open('./blueprint.json','r') as f:
            self.BLUEPRINT_DATA = json.loads(f.read(),encoding='utf-8')
        self.buleprint_name = buleprint_name
        self.stack_name = stack_name
        self.stack_version = stack_version


    # 配置Blueprints数据
    def blueprints(self):
        self.BLUEPRINT_DATA['Blueprints']['blueprint_name'] = self.buleprint_name
        self.BLUEPRINT_DATA['Blueprints']['stack_name'] = self.stack_name
        self.BLUEPRINT_DATA['Blueprints']['stack_version'] = self.stack_version
        return self.BLUEPRINT_DATA

    # 配置host_groups
    def host_groups(self):
        # {
        #     "name": "master_1",
        #     "cardinality": "1",
        #     "components": [
        #         {"name": "HISTORYSERVER"},
        #         {"name": "JOURNALNODE"},
        #         {"name": "METRICS_MONITOR"},
        #         {"name": "NAMENODE"},
        #         {"name": "ZKFC"},
        #         {"name": "ZOOKEEPER_SERVER"}
        #     ]
        # },
        pass
    # 配置hosts_groups中的group
    def _group(self):
        group = {
            "name": "master_1",
            "cardinality": "1",
            "components": []
        }
        for i in range(3):
            group['components'].append(i)
        return group
    def configurations(self):
        pass



class Cluster(object):
    def __init__(self,blueprint,hosts,default_password='admin'):
        self.blueprint = blueprint
        self.hosts = Hosts()
        self.default_password = default_password
        pass
    def host_groups(self):
        host_groups = []
        for k,v in self.hosts.add_hosts().items():
            host_groups.append({"name": "master_1", "hosts": [{"fqdn": v}]})
        return host_groups

    def to_json(self):
        json_data = json.dumps({
                      "blueprint": self.blueprint,
                      "default_password": self.default_password,
                      "host_groups": self.host_groups()
                    })
        return json_data


# 返回HDP 和 HDPUTILS 的json数据
class HDP(object):
    def __init__(self,base_url,verify_base_url=True):
        self.base_url = base_url
        self.verify_base_url = verify_base_url

    def to_json(self):
        hdp_data = json.dumps({
            "Repositories": {
                "base_url": self.base_url,
                "verify_base_url": self.verify_base_url
            }
        })
        return hdp_data
if __name__ == '__main__':
    blueprint = BluePrint('ambari_lPPP',stack_name='CDK',stack_version='2.3.4')
    print(blueprint.blueprints())
    # hosts = Hosts()
    # cluster = Cluster('ambari_lp',hosts)
    #
    # print(cluster.host_groups())
    # pprint.pprint(cluster.to_json())