# encoding: utf-8
import re
import time
import xlwt
from selenium import webdriver
from lxml import etree
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LagouSpider(object):
    driver_path = r"F:\sometools\chromdrive\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "http://localhost:9901/xindou9.html"
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('2021-10')
        ###找到上级元素
        alltr=self.driver.find_elements_by_xpath('/html/body/div/table/tbody/tr')
        i =1
        # xpath = '/html/body/div/table/tbody/tr[' + i +"]/td[1]/div/div[2]/div[1]/span"
        j=0
        # print(xpath)
        for tr in alltr:
            i=i+1
            j=j+1
            # print(i)
            #xpath= '/html/body/div/table/tbody/tr[%d]/td[1]/div/div[2]/div[1]/span'+i
            d=i.__str__()
            titlexpath = '/html/body/div/table/tbody/tr[' + d +"]/td[1]/div/div[2]/div[1]/span"
            timexpath='/html/body/div/table/tbody/tr[' + d + ']/td[1]/div/div[2]/div[2]/div/div[1]'
            sharexpath='/html/body/div/table/tbody/tr[' + d + ']/td[2]/span'
            talkxpath='/html/body/div/table/tbody/tr[' + d + ']/td[3]/span'
            topxpath='/html/body/div/table/tbody/tr[' + d + ']/td[4]/span'
            srcpath='/html/body/div/table/tbody/tr[' + d + ']/td[1]/div/div[1]/img'
            try:
             title=tr.find_element_by_xpath(titlexpath).text
             time3=tr.find_element_by_xpath(timexpath).text
             time2=time3.__str__()
             mytime=re.sub('[\u4e00-\u9fa5]', '', time2)
             sharenum=tr.find_element_by_xpath(sharexpath).text
             talknum= tr.find_element_by_xpath(talkxpath).text
             topnum= tr.find_element_by_xpath(topxpath).text
             images=tr.find_element_by_xpath(srcpath).get_attribute('src')
            except NoSuchElementException:
                print("没找到元素")
                worksheet.write(j, 0, label="null")
                worksheet.write(j, 1, label="null")
                worksheet.write(j, 2, label="null")
                worksheet.write(j, 3, label="null")
                worksheet.write(j, 4, label="null")
                worksheet.write(j, 5, label="null")
            # print(title,mytime,sharenum,talknum,topnum)
            # 参数对应 行, 列, 值
            else:
             worksheet.write(j, 0, label=title)
             worksheet.write(j, 1, label=images)
             worksheet.write(j, 2, label=mytime)
             worksheet.write(j, 3, label=sharenum)
             worksheet.write(j, 4, label=talknum)
             worksheet.write(j, 5, label=topnum)
             print("OK")
        workbook.save('data9.xls')



        # 写入excel
        # 参数对应 行, 列, 值
        # worksheet.write(1, 0, label='this is test')
        # workbook.save('data1.xls')

        # self.driver.find_element_by_xpath('//*[@id="_285c63f4da53bd5cedc023b4fdd71412-scss"]/button').click()
        # time.sleep(20)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/header/div[2]/div/div[1]/div/div[2]/div/form/input[1]').send_keys("四川观察")
        # time.sleep(10)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/header/div[2]/div/div[1]/div/div[2]/div/button/span').click()
        # time.sleep(30)
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[3]/div[2]/button').click()

        # for i in range(100):
        #     print(i)




        # while True:
        #     source = self.driver.page_source
            # WebDriverWait(driver=self.driver, timeout=10).until(
            #     EC.presence_of_element_located((By.XPATH, '//*[@id="s_position_list"]/div[2]/div/span[6]'))
            # )
            # # // *[ @ id = "s_position_list"] / div[2] / div / span[6]
            # self.parse_list_page(source)
            # try:
            #     next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            #     if "pager_next pager_next_disabled" in next_btn.get_attribute("class"):
            #         break
            #     else:
            #         next_btn.click()
            # except:
            #     print(source)


    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.get(url)
        source = self.driver.page_source
        self.parse_datail_page(source)
        # 关闭当前这个详情页
        self.driver.close()
        # 继续切换回职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_datail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")
        information = html.xpath("//div[@class='job-name']//text()")
        salary = html.xpath("//dd[@class='job_request']//text()")
        # job_request_spans = html.xpath("//dd[@class='job_request']//span")
        # salary = job_request_spans[0].xpath('.//text()')[0].strip()
        # city = job_request_spans[1].xpath(".//text()")[0].strip()
        # city = re.sub(r"[\s/]", "", city)
        # work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        # work_years = re.sub(r"[\s/]", "", work_years)
        # education = job_request_spans[3].xpath(".//text()")[0].strip()
        # education = re.sub(r"[\s/]", "", education)
        # desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        # company_name = html.xpath("//h2[@class='fl']/text()")[0].strip()
        position = {
            'name': position_name,
            'information': information,
            'salary': salary,
            # 'company_name': company_name,
            # 'salary': salary,
            # 'city': city,
            # 'work_years': work_years,
            # 'education': education,
            # 'desc': desc
        }
        self.positions.append(position)
        print(position)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
