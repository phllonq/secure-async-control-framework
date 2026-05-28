````markdown id="m7jlwm"
# Certificate Directory

This directory is used for local TLS certificate generation during development and testing.

Private certificates and keys should never be committed to the repository.

## Development Certificates

Generate local development certificates using:

```bash
chmod +x generate_certs.sh
./generate_certs.sh
````

Generated files:

* server.pem
* server.key

These files are ignored through `.gitignore`.

```
```

