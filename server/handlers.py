class PacketHandler:
    async def handle(
        self,
        packet: dict
    ):
        packet_type = packet.get(
            "packet_type"
        )

        return {
            "handled": True,
            "type": packet_type
        }


