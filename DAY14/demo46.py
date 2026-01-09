import logging

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="app.log",filemode="a",level=logging.INFO)

logging.debug("This is Debug message")
logging.info("App info")
logging.warning("Low disk space")
logging.error("DB failed")
logging.critical("App Crash")