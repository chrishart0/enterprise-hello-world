import pytest
import subprocess
import sys
import os
from enterprise_hello_world import HelloWorldWriter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@pytest.fixture
def writer():
    count = int(os.getenv("HELLO_WORLD_COUNT", 10))
    return HelloWorldWriter(count=count)

def test_default_count_initialization():
    writer = HelloWorldWriter()
    assert writer.count == 10, "Default count should be 10"

def test_custom_count_initialization():
    writer = HelloWorldWriter(count=5)
    assert writer.count == 5, "Custom count should be set correctly"

def test_validate_count_positive():
    writer = HelloWorldWriter(count=1)
    assert writer.count == 1, "Count should be 1 for valid positive input"

def test_validate_count_negative():
    with pytest.raises(ValueError, match="Count must be a positive integer."):
        HelloWorldWriter(count=-5)

def test_validate_count_non_integer():
    with pytest.raises(ValueError, match="Count must be a positive integer."):
        HelloWorldWriter(count="invalid")

def test_generate_messages(writer):
    messages = writer.generate_messages()
    assert len(messages) == 10, "Should generate 10 messages"
    assert messages[0] == "Hello, World! - Instance 1", "First message format is incorrect"

def test_construct_message():
    writer = HelloWorldWriter(count=1)
    message = writer.construct_message(0)
    assert message == "Hello, World! - Instance 1", "Constructed message format is incorrect"

def test_write_messages(capsys, writer):
    writer.write_messages()
    captured = capsys.readouterr()
    assert "Hello, World! - Instance 1" in captured.out, "Output should contain the expected message"
    assert "Hello, World! - Instance 10" in captured.out, "Output should contain the last message"

def test_main_block():
    result = subprocess.run([sys.executable, "-m", "enterprise_hello_world.writer"], capture_output=True, text=True)
    assert result.returncode == 0, f"Main block failed with return code {result.returncode}"
    assert "Hello, World!" in result.stdout, "Expected output not found in main block execution"
