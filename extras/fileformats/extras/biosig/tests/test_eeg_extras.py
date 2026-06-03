"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.biosig import (
    BrainVision,
    EdfPlus,
)

# ------------------------------
# EEG: EDF
# ------------------------------


def test_edf_plus_read_metadata(edf_plus_path):
    metadata = EdfPlus(edf_plus_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
    assert "edf_patient_code" in metadata


# ------------------------------
# EEG: BrainVision
# ------------------------------


def test_brainvision_read_metadata(bv_vhdr_path):
    metadata = BrainVision(bv_vhdr_path.with_suffix(".eeg")).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
    assert "bv_n_channels" in metadata
