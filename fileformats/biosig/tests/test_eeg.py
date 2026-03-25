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
    BrainVisionHeader,
    BrainVisionMarker,
    Edf,
    Fif,
)

# ------------------------------
# EEG: FIF
# ------------------------------


def test_fif_instantiate(fif_path):
    Fif(fif_path)


# ------------------------------
# EEG: EDF
# ------------------------------


def test_edf_instantiate(edf_path):
    Edf(edf_path)


# ------------------------------
# EEG: BrainVision
# ------------------------------


def test_brainvision_header_instantiate(bv_vhdr_path):
    BrainVisionHeader(bv_vhdr_path)


def test_brainvision_marker_instantiate(bv_vhdr_path):
    BrainVisionMarker(bv_vhdr_path.with_suffix(".vmrk"))


def test_brainvision_data_instantiate(bv_vhdr_path):
    BrainVision(bv_vhdr_path.with_suffix(".eeg"))
