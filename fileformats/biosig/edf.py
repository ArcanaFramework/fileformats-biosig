"""
EEG file formats for XNAT Ingest workflows.
Defines and validates common EEG file formats (FIF, EDF, BrainVision) for use in XNAT Ingest pipelines.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.core import validated_property, mtime_cached_property
from fileformats.core.exceptions import FormatMismatchError
from fileformats.generic import BinaryFile
from fileformats.core.mixin import WithMagicNumber
from .base import Biosig


class Edf(WithMagicNumber, BinaryFile, Biosig):
    """
    EDF format EEG (European Data Format) — binary file with fixed-width ASCII
    header followed by binary signal data.
    """

    extensions = ".edf"
    # First 8 bytes are "0       " (version field)
    magic_number = b"\x30\x20\x20\x20\x20\x20\x20\x20"

    @mtime_cached_property
    def header(self) -> str:
        with open(self, "rb") as f:
            header = f.read(256)
        return header.decode("ascii", errors="replace")

    @validated_property
    def local_recording_identification(self) -> list[str]:
        parts: list[str] = self.header[88:168].split()
        if len(parts) != 5:
            raise FormatMismatchError(
                'Unrecognised "local recording identification" string, '
                f"should have 5 parts, found: {parts}"
            )
        return parts

    @validated_property
    def local_patient_identification(self) -> list[str]:
        parts: list[str] = self.header[8:88].split()
        if len(parts) != 4:
            raise FormatMismatchError(
                'Unrecognised "local patient identification" string, '
                f"should have 4 parts, found: {parts}"
            )
        return parts

    @property
    def _edf_type(self) -> str:
        edf_type: str = self.header[192:236].strip()
        return edf_type

    @validated_property
    def edf_type(self) -> str:
        if self._edf_type != "":
            raise FormatMismatchError(
                'EDF type field ("reserved") should be blank for plain EDF '
                "(i.e. not EDF+)"
            )
        return ""


class EdfPlus(Edf):
    """
    EDF+ format — extension of EDF supporting discontinuous recordings and
    additional annotation channels. Distinguished by "EDF+C" or "EDF+D" in
    the reserved header field.
    """

    extensions = ".edf+"

    valid_edf_types = ["EDF+C", "EDF+D"]

    @validated_property
    def edf_type(self) -> str:
        if self._edf_type not in self.valid_edf_types:
            raise FormatMismatchError(
                f'EDF type field ("reserved") should be in {self.valid_edf_types} '
                f"for EDF+, found: {self._edf_type!r}"
            )
        return self._edf_type
