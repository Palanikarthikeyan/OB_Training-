import logging

#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(filename="app.log",filemode="a",level=logging.INFO)
logging.basicConfig(filename="app.log",filemode="a",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("App info")
logging.error("DB failed")
