import logging

import inventory

logger = logging.getLogger("inventory")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("application.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logger.info("Inventory management started")
logger.debug("Checking product inventory operations")

# Product stock checks
try:
    result = inventory.check_stock(10, 5)
    logger.info("Product check: %s", result)

    result = inventory.check_stock(5, 10)
    logger.warning("Product check: %s", result)

except ValueError as error:
    logger.error("Product check error: %s", error)

# Successful operations
try:
    total = inventory.calculate_total_price(100, 2)
    logger.info("Total price: %s", total)

    discounted_price = inventory.apply_discount(total, 10)
    logger.info("Discounted price: %s", discounted_price)

except ValueError as error:
    logger.error("Operation error: %s", error)

# Invalid calculation
try:
    inventory.calculate_total_price(-50, 2)

except ValueError as error:
    logger.error("Calculation error: %s", error)

logger.info("Inventory management completed")

file_handler.close()
