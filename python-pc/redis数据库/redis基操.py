import redis
def main1():
    client=redis.Redis(host='wp35776584.qicp.vip',port='12346',password='890718feng')
    print(client.get('name').decode())
if __name__ == '__main__':
    main1()
