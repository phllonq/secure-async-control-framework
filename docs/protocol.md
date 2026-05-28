````markdown id="x5s0h2"
# Protocol Specification

## Packet Structure

Each packet contains metadata required for validation and sequencing.

Example packet:

```json
{
  "version": 1,
  "packet_id": "a1b2c3",
  "packet_type": "heartbeat",
  "sequence": 10,
  "timestamp": 1750000000,
  "nonce": "ff91aa",
  "data": {}
}
````

---

## Fields

| Field       | Purpose                  |
| ----------- | ------------------------ |
| version     | Protocol version         |
| packet_id   | Unique packet identifier |
| packet_type | Packet category          |
| sequence    | Packet ordering          |
| timestamp   | Replay validation        |
| nonce       | Uniqueness verification  |
| data        | Payload content          |

---

## Validation Rules

Packets are rejected if:

* timestamps exceed allowed drift
* nonce values are reused
* packet ordering is invalid
* packet size exceeds limits

```
```

