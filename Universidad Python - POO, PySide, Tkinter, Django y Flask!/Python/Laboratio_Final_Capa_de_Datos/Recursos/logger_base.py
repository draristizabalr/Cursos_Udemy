import logging as log

log.basicConfig(level=log.WARNING,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_de_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje DEBUG')
    log.info('Mensaje INFO')
    log.warning('Mensaje WARNING')
    log.error('Mensaje ERROR')
    log.critical('Mensaje CRITICAL')