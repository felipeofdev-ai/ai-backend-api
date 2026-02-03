import logging
import sys

# Logger configurado de forma profissional
logger = logging.getLogger("ai-backend-api")
logger.setLevel(logging.INFO)

# Formato de log padrão
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)

# Handler para console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.propagate = False
