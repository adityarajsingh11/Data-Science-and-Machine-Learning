
## configuring logging
import logging

logging.basicConfig(
    filename='app.log',  ## create a app.log file
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )