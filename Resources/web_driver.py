from selenium import webdriver

#from webdriver_manager.chrome import ChromeDriverManager

def web_driver():
    try:
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Firefox()
        return driver
    except Exception as e:
        return{
            'status': 'ERROR',
            'error': str(e)
        },500