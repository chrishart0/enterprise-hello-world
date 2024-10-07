from typing import List, Optional
import sys
from pydantic import ValidationError
from enterprise_hello_world.settings import Settings
from enterprise_hello_world.logger import get_logger

# Obtain the logger from the logger configuration module
logger = get_logger("EnterpriseHelloWorldLogger")

class HelloWorldWriter:
    def __init__(self, count: Optional[int] = None):
        settings = Settings()
        self.count = count if count is not None else settings.hello_world_count
        self.validate_count()
        logger.info(f"Initialized HelloWorldWriter with count: {self.count}")

    def validate_count(self):
        if not isinstance(self.count, int) or self.count <= 0:
            logger.error("Invalid count provided. Must be a positive integer.")
            raise ValueError("Count must be a positive integer.")
        logger.debug("Count validated successfully.")

    def generate_messages(self) -> List[str]:
        logger.debug("Generating 'Hello, World!' messages.")
        messages = [self.construct_message(index) for index in range(self.count)]
        logger.debug(f"Generated {len(messages)} messages.")
        return messages

    @staticmethod
    def construct_message(index: int) -> str:
        logger.debug(f"Constructing message for index {index + 1}.")
        return f"Hello, World! - Instance {index + 1}"

    def write_messages(self):
        logger.info("Writing messages...")
        messages = self.generate_messages()
        for index, message in enumerate(messages):
            self.write_message(index, message)
        logger.info("Finished writing messages.")

    @staticmethod
    def write_message(index: int, message: str):
        # Simulating complex message writing logic
        try:
            logger.debug(f"Writing message {index + 1}: {message}")
            # Placeholder for a more sophisticated writing operation
            sys.stdout.write(f"{message}\n")
        except Exception as e:
            logger.error(f"Failed to write message {index + 1}: {e}")
            raise

if __name__ == "__main__":
    try:
        logger.info("Starting the enterprise 'Hello, World!' writer application.")
        writer = HelloWorldWriter()
        writer.write_messages()
        logger.info("Application finished successfully.")
    except (ValueError, ValidationError) as ve:
        logger.critical(f"Application terminated due to invalid input: {ve}")
        sys.exit(2)
    except Exception as e:
        logger.critical(f"Application terminated with an unexpected error: {e}")
        sys.exit(1)