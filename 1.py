import yaml

with open('./conf.yaml', 'r') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)
    res1 = result['nao']
    for i in range(1, len(res1)+1):
        # print res1
        # print type(res1)
        res2 = res1[i]['ip']

#         print res2
# print result