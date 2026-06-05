"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.biosig import (
    EdfPlus,
)

# ------------------------------
# EEG: EDF
# ------------------------------


def test_edf_plus_instantiate(edf_plus_path):
    EdfPlus(edf_plus_path)
