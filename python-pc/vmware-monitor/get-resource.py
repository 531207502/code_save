import time
from pyVmomi import vim,vmodl
from pyVim.connect import SmartConnectNoSSL
class VmManage(object):
    def __init__(self, host, user, password, port, ssl):
        self.host = host
        self.user = user
        self.pwd = password
        self.port = port
        self.sslContext = ssl
        try:
            self.client = SmartConnectNoSSL(host=host,
                                            user=user,
                                            pwd=password,
                                            port=443
                                            )
            self.content = self.client.RetrieveContent()
            self.result = True
        except Exception as e:
            self.result = False
            self.message = e
            print("登录参数存在问题")

    def _get_all_objs(self, obj_type, folder=None):
        """
        根据对象类型获取这一类型的所有对象
        """
        if folder is None:
            container = self.content.viewManager.CreateContainerView(self.content.rootFolder, obj_type, True)
        else:
            container = self.content.viewManager.CreateContainerView(folder, obj_type, True)
        return container.view

    def _get_obj(self, obj_type, name):
        """
        根据对象类型和名称来获取具体对象
        """
        obj = None
        content = self.client.RetrieveContent()
        container = content.viewManager.CreateContainerView(content.rootFolder, obj_type, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def get_datacenters(self):
        """
       返回所有的数据中心
        """
        return self._get_all_objs([vim.Datacenter])

    def get_datacenter_by_name(self, datacenter_name):
        """
       根据数据中心名称获取数据中心对象
        """
        return self._get_all_objs([vim.Datacenter], datacenter_name)
if __name__ == '__main__':
    ip = '10.10.1.2'
    user = 'administrator@vsphere.local'
    password = 'VMware1!'
    port = 443
    vm = VmManage(host=ip,
                  user=user,
                  password=password,
                  port=port, ssl=None)
    if vm.result:
        # 说明连接成功，可以使用vm.client等
        print("连接成功了")
        print(vm.result)
        pass
    else:
        print("请检查错误")
    cluster_objs_jiqun = vm._get_all_objs([vim.ClusterComputeResource])
    print(cluster_objs_jiqun)
    cluster_objs_hosts = vm._get_all_objs([vim.HostSystem])
    print(cluster_objs_hosts)
    cluster_objs_vms = vm._get_all_objs([vim.VirtualMachine])
    print(cluster_objs_vms)
    #print(dir(cluster_objs_jiqun[0]))
    #print(dir(cluster_objs_hosts[0]))
    #print(dir(cluster_objs_vms[0].summary.vm.guest))
    #print(cluster_objs_hosts[0].summary.quickStats.overallMemoryUsage)
    #print(cluster_objs_hosts[1].summary.quickStats.overallMemoryUsage)
    #print(cluster_objs_hosts[2].summary.quickStats.overallMemoryUsage)
    #print(dir(cluster_objs_hosts[0].datastore))
    #print(cluster_objs_jiqun[0])
    #print(cluster_objs_hosts[0].datastore.summary.capacity)
    print(dir(cluster_objs_vms[2].summary.storage))
    print(cluster_objs_vms[2].name)
    #print(cluster_objs_vms[2].summary.storage)
    print(cluster_objs_vms[2].summary.vm.guest.disk)
    #print(type(cluster_objs_vms[2].summary.vm.guest.disk))
    #print(cluster_objs_hosts[2].summary.host.summary)
    #print(cluster_objs_hosts[0].systemResources)