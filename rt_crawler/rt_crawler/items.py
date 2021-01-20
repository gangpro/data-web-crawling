# 내가 가져올 데이터 명시

import scrapy

# 영화 정보에 대한 class 정의
class RTItem(scrapy.Item):
    #rank = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    #opening = scrapy.Field()
    genres = scrapy.Field()
    year = scrapy.Field()
