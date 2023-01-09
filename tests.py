"""
Unit tests
"""
from main import MORSE_CODES, MORSE_CODES_REVERSED, MorseDecoder, MorseEncoder


def test_1() -> None:
    """Dummy test to prevent exit code 5"""
    to_encode = "hello world"

    encoder = MorseEncoder(MORSE_CODES)
    encoded = encoder.encode(to_encode)

    assert encoded == ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."


def test_decode1() -> None:
    to_decode = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."

    decoder = MorseDecoder(MORSE_CODES_REVERSED)
    decoded = decoder.decode(to_decode)

    assert decoded == "H E L L O  W O R L D"
