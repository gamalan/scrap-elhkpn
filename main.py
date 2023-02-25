from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd

def get_next(driver):
    get_next_page = driver.find_elements(by=By.XPATH,
                                         value='//*[@id="announ-page"]/div/div[2]/div[2]/div/div/div/div[2]/div/ul/li[*]/a')
    for el in get_next_page:
        if el.text == "Next ≫":
            el.click()
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=selenium")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    templist = []
    nama = []
    lembaga = []
    unit_kerja = []
    jabatan = []
    tanggal_lapor = []
    jenis_lapor = []
    kekayaan = []

    driver.get("https://elhkpn.kpk.go.id/portal/user/login#announ")
    driver.implicitly_wait(3)
    driver.find_element(by=By.XPATH, value='//*[@id="page-top"]/div[10]/div/button').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="notice"]/div/div[2]/a/img').click()
    time.sleep(4)
    ## TODO: Ganti pakai input, atau kode wilayah dari csv lalu diloop
    driver.find_element(by=By.XPATH, value='//*[@id="CARI_NAMA"]').send_keys("347109")
    time.sleep(5)
    elem = driver.find_element(by=By.XPATH, value='//*[@id="captcha-announ"]/div/div/iframe')
    driver.switch_to.frame(elem)
    ## TODO: Tambah bypass captcha
    driver.find_element(by=By.XPATH, value='//*[@id="recaptcha-anchor"]').click()
    time.sleep(3)
    driver.switch_to.parent_frame()
    driver.find_element(by=By.XPATH, value='//*[@id="ajaxFormCari"]/div/div[1]/div[5]/div/div[2]/div/button[1]').click()
    time.sleep(3)

    nama += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                        value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[7]')]
    lembaga += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                           value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[8]')]
    unit_kerja += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                              value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[9]')]
    jabatan += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                           value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[10]')]
    tanggal_lapor += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                                 value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[11]')]
    jenis_lapor += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                               value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[12]')]
    kekayaan += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                            value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[13]')]
    while get_next(driver):
        time.sleep(3)
        nama += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                            value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[7]')]
        lembaga += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                               value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[8]')]
        unit_kerja += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                                  value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[9]')]
        jabatan += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                               value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[10]')]
        tanggal_lapor += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                                     value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[11]')]
        jenis_lapor += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                                   value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[12]')]
        kekayaan += [elem.text for elem in driver.find_elements(by=By.XPATH,
                                                                value='//*[@id="announ-page"]/div/div[2]/div[1]/table/tbody/tr[*]/td[13]')]
    data_dict = {"Nama": nama, "Lembaga": lembaga, "Unit Kerja": unit_kerja, "Jabatan": jabatan,
                 "Tanggal Lapor": tanggal_lapor, "Jenis Lapor": jenis_lapor, "Kekayaan": kekayaan}
    data_frame = pd.DataFrame(data_dict)
    data_frame.to_csv("data/kekayaan347109.csv")
    time.sleep(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
