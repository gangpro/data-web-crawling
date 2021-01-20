# 실제로 크롤링하는 파일
import scrapy
from rt_crawler.items import RTItem


class RTSpider(scrapy.Spider):
    # 3개의 정해진 변수를 설정해야 한다.
    name = "My_First_Crawler"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/top/bestofrt/?year=2018"]     # 1~100등 영화제목나온 페이지

    def parse(self, response):
        tr_list = response.xpath('//*[@id="top_movies_main"]/div/table/tr')

        for tr in tr_list:
            href = tr.xpath('./td[3]/a/@href').extract()[0]
            url = response.urljoin(href)
            # print(url) 화면에 출력 대신에 Request를 보내야 한다.
            # 해당 page로 이동하겠다는 의미

            # 현재 페이지에서 xpath를 이용해서 year와 rank를 구해보자.
            year = "2018"
            yield scrapy.Request(url, callback=self.parse_detail_page,meta={"year" : year})     #yield는 잠시대기라는 의미
            # request를 보내고 해당 결과를 받아 와서 아래와 같이 reponse 객체가 우리 함수에 전달 된다.

    def parse_detail_page(self, response):
        item = RTItem()
        #item["rank"] = response.meta["rank"]
        item["title"] = response.xpath('//*[@id="topSection"]/div[2]/div[1]/h1/text()').extract()[0]
        item["score"] = response.xpath('//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/div/small/text()').extract()[0].strip()
        #item["opening"] = response.xpath('//*[@id="top_movies_main"]/div/div[2]/button/text()').extract()[1].strip()
        item["genres"] = ", ".join(response.xpath('//*[@id="mainColumn"]/section[3]/div/div/ul/li[2]/div[2]/a/text()').getall())
        item["year"] = response.meta["year"]

#        genres = response.xpath('//*[@id="mainColumn"]/section[3]/div/div/ul/li[2]/div[2]/a/text()').extract(
#        temp_str = ""
#        for i in genres:
#            print(i.strip())
#            temp_str += i.strip()
#            if i == genres[-1]:
#                break
#            temp_str += ", "
#        item["genres"] = temp_str

        yield item   # 데이터가 pipeline으로 넘어감






