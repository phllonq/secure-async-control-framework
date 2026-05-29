import hashlib
import hmac
import secrets


class CryptoUtils:
    @staticmethod
    def generate_nonce() -> str:
        return secrets.token_hex(12)

    @staticmethod
    def sha256(
        data: bytes
    ) -> str:
        return hashlib.sha256(
            data
        ).hexdigest()

    @staticmethod
    def hmac_sha256(
        key: bytes,
        data: bytes
    ) -> str:
        return hmac.new(
            key,
            data,
            hashlib.sha256
        ).hexdigest()


