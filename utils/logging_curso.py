import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/curso_python.log'),
                    log.StreamHandler()
                ])

log.debug("Esto es un log de debug",12,"",34)
log.info("Esto es un log de prueba de error")
log.warning("Esto es un log de prueba de error")
log.error("Esto es un log de prueba de error")
log.critical("Esto es un log de prueba de error")