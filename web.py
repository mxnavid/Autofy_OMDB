from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(executable_path="/Users/mxnavid/Documents/random/AutoFy/webfy/bin/geckodriver")


def initiateWebPage():
    driver.get("WEBSITE ADDRESS")
    time.sleep(15)
    # el = driver.find_element_by_class_name("form-control placeholder-no-fix")
    # el.send_keys("navid")
    driver.get("WEBSITE ADDRESS")

def startFillingInfo(driver):
    name = driver.find_element_by_id("name")
    name.send_keys("I Am a TEST")

    orignal_title = driver.find_element_by_id("o_name")
    orignal_title.send_keys("I am the original test")

    http = Select(driver.find_element_by_name("protocol"))
    http.select_by_index(1)
    time.sleep(1)

    linkHTTP = driver.find_element_by_id("rtsp_url")
    linkHTTP.send_keys("###/playlist.m3u8")
    


    #TODO FOR HD

    category = Select(driver.find_element_by_name("category_id"))
    category.select_by_index(3) # Selects the English Category
    
    year = driver.find_element_by_name("year")
    year.send_keys("2018")
    
    country = driver.find_element_by_name("country")
    country.send_keys("United States")

    duration = driver.find_element_by_name("time")
    duration.send_keys("100")
    
    director = driver.find_element_by_name("director")
    director.send_keys("Nolan")
    
    actors = driver.find_element_by_name("actors")
    actors.send_keys("Actors, Nectors, Lactose, Factose")


    description = driver.find_element_by_class_name("form-control description")
    description.send_keys("Trynna be a good person")

    



def main():
    initiateWebPage()
    startFillingInfo(driver)


if __name__ == "__main__":
    main()
    