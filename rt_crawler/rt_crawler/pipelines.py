# rt_spider 작업 이후 pipelines.py 작성하기.
import csv

class RTPipeline(object):

    def __init__(self):
        self.writecsv = csv.writer(open("rt_new.csv", "w"))
        # 파일 맨윗줄에 "title"과 "score"를 쓸 것이다.
        self.writecsv.writerow(["title","score","genres","year"])
        # self.writecsv.writerow(["rank","title","score","opening","genres","year"])
        # self.writecsv.writerow(["title"])


    def process_item(self, item, spider):
        row = list()
        #row.append(item["rank"])
        row.append(item["title"])
        row.append(item["score"])
        #row.append(item["opening"])
        row.append(item["genres"])
        row.append(item["year"])
        self.writecsv.writerow(row)   # 데이터가 csv 파일에 하나씩 삽입됨
        return item
