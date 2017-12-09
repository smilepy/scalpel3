# -*- coding:utf-8 -*-


def get_querycase():
        line_list=[]


        file_path_list=['./file/author_name_albumname_slice.txt','./file/music.txt',
                        './file/music_notpassed.txt','./file/RMusic.1.1_12072138notpassed.txt']
        for f_path in file_path_list:
            f=open(f_path)
            for line in f:
                if len(line.strip('\n')) > 0:
                    query = line.strip('\n')
                    if '\t' in line:
                        splits = line.split('\t')
                        query = splits[0]
                    if query not in line_list:
                        line_list.append(query)
                    print(query)

            f.close()

        f1 = open("./output/music_query_12081348.txt", "a")
        print("line_list's length:"+str(line_list.__len__()))
        for line in line_list:
            f1.write(line+'\n')
        f1.close()


if __name__=="__main__":
    get_querycase()