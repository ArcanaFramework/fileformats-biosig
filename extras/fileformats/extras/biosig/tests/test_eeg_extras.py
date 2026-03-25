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
    Edf,
    Fif,
)

# ------------------------------
# EEG: FIF
# ------------------------------


def test_fif_read_metadata(fif_path):
    metadata = Fif(fif_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None


# ------------------------------
# EEG: EDF
# ------------------------------


def test_edf_read_metadata(edf_path):
    metadata = Edf(edf_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
    assert "edf_patient_code" in metadata


# ------------------------------
# EEG: BrainVision
# ------------------------------


def test_brainvision_read_metadata(bv_vhdr_path):
    metadata = BrainVision(bv_vhdr_path.iterdir()).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
    assert "bv_n_channels" in metadata
