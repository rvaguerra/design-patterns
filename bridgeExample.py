from __future__ import annotations
from abc import ABC


class Device(ABC):

    STARTING_VOLUME = 50
    STARTING_CHANNEL = 3

    def __init__(self) -> None:
        """Create a device instance."""
        self.volume = Device.STARTING_VOLUME
        self.channel = Device.STARTING_CHANNEL

    @property
    def volume(self) -> float:
        """Get volume.

        Returns:
            float: The volume.
        """
        return self._volume

    @volume.setter
    def volume(self, volume: float) -> None:
        """Set volume.

        Args:
            volume (float): The volume.
        """
        self._volume = max(0, min(volume, 100))

    @property
    def channel(self) -> int:
        """Get channel.

        Returns:
            int: The channel.
        """
        return self._channel

    @channel.setter
    def channel(self, channel: int) -> None:
        """Set channel.

        Args:
            channel (int): The channel.
        """
        self._channel = channel


class TV(Device):
    pass


class Radio(Device):
    pass


class Remote:

    def __init__(self, device: Device) -> None:
        """Create a remote instance.

        Args:
            device (Device): The remote controlled device.
        """
        self.device = device

    @property
    def device(self) -> Device:
        """Get device.

        Returns:
            Device: The device.
        """
        return self._device

    @device.setter
    def device(self, device: Device) -> None:
        """Set device.

        Args:
            device (Device): The device.
        """
        self._device = device

    def channelUp(self) -> None:
        """Increase channel."""
        self.device.channel = self.device.channel + 1

    def channelDown(self) -> None:
        """Decrease channel."""
        self.device.channel = self.device.channel - 1

    def volumeUp(self) -> None:
        """Increase volume."""
        self.device.volume = self.device.volume + 1

    def volumeDown(self) -> None:
        """Decrease volume."""
        self.device.volume = self.device.volume - 1


class AdvancedRemote(Remote):

    def mute(self) -> None:
        """Set device volume to 0."""
        self.device.volume = 0


device = TV()
simpleRemote = Remote(device)

simpleRemote.channelUp()

print(device.channel == 4)
print(device.volume == 50)

advancedRemote = AdvancedRemote(device)
advancedRemote.mute()

print(device.volume == 0)
