# -*- coding:utf-8 -*-
import requests
import json


def get_dst_resp():
        url = 'http://192.168.1.41:8081/v3/query?traceId=pypyppypypypypypy12070956'
        params = {
            "agentId": "1ZmI5ZmQ2MTkzZmE",
            "token": "dee81a6d2edb2593cf344208532424d96647",
            "sessionId": "10110000002018A4",
            "query": "",
            "verbose": True
        }
        f = open("./file/music_1206_76.txt")
        # f1 = open("./file/music_1206_76_result.txt", "a")
        # f1.write('query'+'\t'+'service'+'\t'+'action'+'\t'+'params'+'\n')
        # print('query'+'\t'+'service'+'\t'+'action'+'\t'+'params')
        i=0
        for line in f:
            if len(line.strip('\n')) > 0:
                    params['query']=line.strip('\n')
                    if '\t' in line:
                        splits=line.split('\t')
                        print(splits[0])
                        params['query']=splits[0]
                    res = requests.post(url=url, data=json.dumps(params))
                    i += 1
                    print(i)
                    print(res)

        # f1.close()
        f.close()


if __name__=="__main__":
    get_dst_resp()