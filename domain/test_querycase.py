# -*- coding:utf-8 -*-
import requests
import json


def test_rosai_regression():
        url = 'http://192.168.1.29:8080/v3/query'
        params = {
            "query": "",
            "sessionId": "1481509978",
            "token": "d0bb7439644c1b0dbf6d21c34d06b2b39425",
            "apiKey":"jk4NzBhM2UwYWU5Z",
            "agentId": "222",
            "location": {
                "address": {
                    "country": "中国",
                    "province": "北京",
                    "city": "北京"
                }
            }
        }
        f = open("./file/music_1206_76.txt")
        f1 = open("./file/music_1206_76_result.txt", "a")
        f1.write('query'+'\t'+'service'+'\t'+'action'+'\t'+'params'+'\n')
        print('query'+'\t'+'service'+'\t'+'action'+'\t'+'params')
        i=0
        for line in f:
            if len(line.strip('\n')) > 0:
                    params['query']=line.strip('\n')
                    if '\t' in line:
                        splits=line.split('\t')
                        print(splits[0])
                        params['query']=splits[0]
                    res = requests.post(url=url, data=json.dumps(params))
                    print(res)
                    i+=1
                    if res.json()["status"]["code"]==0:
                        if str(res.json()["semantic"]["service"])=='Translator':
                            f1.write(params['query'] +'\t'+str(res.json()["semantic"]["service"])+'\t'+str(res.json()["semantic"]["action"])+'\t' + str(res.json()["result"]["hint"])+'\t'+str(res.json())+'\n')
                            print(params['query'] + '\t'+str(res.json()["semantic"]["service"])+'\t'+str(res.json()["semantic"]["action"])+'\t' + str(res.json()["result"]["hint"])+'\t'+str(res.json()))
                        else:

                            try:
                                f1.write(params['query'] + '\t' + str(res.json()["semantic"]["service"]) + '\t' + str(
                                    res.json()["semantic"]["action"]) + '\t' + str(
                                    res.json()["semantic"]["params"]) + '\n')
                                print(str(i)+'\t'+params['query'] + '\t' + str(res.json()["semantic"]["service"]) + '\t' + str(
                                    res.json()["semantic"]["action"]) + '\t' + str(res.json()["semantic"]["params"]))
                            except KeyError:
                                f1.write(params['query'] + '\t' + str(res.json()["semantic"]["service"]) + '\t' + str(
                                    res.json()["semantic"]["action"])  +'\t'+ " has not params "+ '\n')
                                print(str(i)+'\t'+params['query'] + '\t' + str(res.json()["semantic"]["service"]) + '\t' + str(
                                    res.json()["semantic"]["action"]) + '\t' + " has not params ")


                    else:
                        f1.write(params['query'] + '\t' + str(res.json())+'\n')
                        print(str(i)+'\t'+params['query'] + '\t' + str(res.json()))

        f1.close()
        f.close()


if __name__=="__main__":
    test_rosai_regression()