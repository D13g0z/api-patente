from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def consultar_patente_chile(patente: str) -> str:
    options = Options()
    # options.add_argument("--headless")  # Activa para producción
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("C:/Users/dzuni/OneDrive/Documentos/Scraping/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.patentechile.com")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtTerm")))
        input_box = driver.find_element(By.ID, "txtTerm")
        input_box.send_keys(patente)

        buscar_btn = driver.find_element(By.ID, "btnConsultar")
        buscar_btn.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tbl-results")))
        tabla = driver.find_element(By.ID, "tbl-results")
        resultado = tabla.text.strip()

        if not resultado:
            resultado = "⚠️ No se encontró información para la patente ingresada."

    except Exception as e:
        resultado = f"❌ Error al consultar: {e}"

    finally:
        driver.quit()

    return resultado