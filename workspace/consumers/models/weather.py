"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("processing incoming weather data")
        try:
            # TODO: Process incoming weather messages. Set the temperature and status.
            weather = message.value()
            self.temperature = weather['temperature']
            self.status = weather['status']
        except Exception as e:
            logger.error(f"weather data is not processed: {str(e)}")
