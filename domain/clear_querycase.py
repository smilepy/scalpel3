# -*- coding:utf-8 -*-
import random


def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list

def clear_querycase():
        f = open("./file/musicquery.txt")
        f1 = open("./output/music_query_1207.0.txt", "a")
        q_set=set()
        for line in f:
            if len(line.strip('\n')) > 0:
                    query=line.strip('\n')
                    if '\t' in line:
                        splits=line.split('\t')
                        query=splits[0]
                    print(query)
                    q_set.add(query)

        f.close()
        query_list = list(q_set)
        # print(query_list)
        # index_list=random_int_list(0,9060,1100)
        # index_set=set(index_list)
        # index_list=list(index_set)
        # index_list.sort()
        # for i in index_list:
        #     f1.write('"'+query_list[i]+'"'+'\n')
        for line in query_list:
            f1.write(line+'\n')
        f1.close()



if __name__=="__main__":
    clear_querycase()