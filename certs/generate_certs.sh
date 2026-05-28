```bash id="i5mjlwm"
#!/bin/bash

mkdir -p certs

openssl req -x509 -newkey rsa:4096 \
-keyout certs/server.key \
-out certs/server.pem \
-sha256 \
-days 365 \
-nodes \
-subj "/CN=localhost"

echo "Development certificates generated."
```

