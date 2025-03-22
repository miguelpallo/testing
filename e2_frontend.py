from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
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
print(driver.title)

# Login
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
print("Login - Test case: Passed")
time.sleep(3)

# Agregar productos al carrito
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
print("Productos añadidos - Test case: Passed")
time.sleep(3)

# Ir al carrito
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
print("Visualización del carrito - Test case: Passed")
time.sleep(3)

# Proceder al checkout
wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("QA")
wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Tester")
wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("12345")
wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
print("Formulario de compra completado - Test case: Passed")
time.sleep(3)

# Finalizar compra
wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
# print("Mensaje de éxito:", success_message)
assert success_message == "Thank you for your order!"
print("Finalización de compra - Test case: Passed")
time.sleep(3)

driver.quit()
