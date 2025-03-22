from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

"""
Prueba E2E
Ejercicio 2:

Realizar una prueba funcional automatizada (Prueba E2E) de un flujo de compra en la página https://www.saucedemo.com/ que incluya:

Autenticarse con el usuario: standard_user y password: secret_sauce
Agregar dos productos al carrito
Visualizar el carrito
Completar el formulario de compra
Finalizar la compra hasta la confirmación: "THANK YOU FOR YOUR ORDER"
"""

# Configuración del WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

test_results = []  # Lista para almacenar los resultados de las pruebas

try:
    # Login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    test_results.append(["Login", "Passed"])
    time.sleep(3)

    # Agregar productos al carrito
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    test_results.append(["Productos añadidos", "Passed"])
    time.sleep(3)

    # Ir al carrito
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    test_results.append(["Visualización del carrito", "Passed"])
    time.sleep(3)

    # Proceder al checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("QA")
    wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Tester")
    wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("12345")
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
    test_results.append(["Formulario de compra completado", "Passed"])
    time.sleep(3)

    # Finalizar compra
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert success_message == "THANK YOU FOR YOUR ORDER"
    test_results.append(["Finalización de compra", "Passed"])
    time.sleep(3)

except Exception as e:
    # Capturar excepciones y registrar el fallo
    test_results.append(["Error", str(e)])
    print(f"Error durante la ejecución: {e}")

finally:
    driver.quit()

# Generar el reporte CSV
with open("test_report.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Test Case", "Result"])  # Encabezados del CSV
    writer.writerows(test_results)

print("Reporte de pruebas generado: test_report.csv")