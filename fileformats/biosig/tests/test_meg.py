"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.biosig import Ctf, CtfInfo, CtfMeg4, CtfRes4, Kit

# ------------------------------
# MEG: CTF
# ------------------------------


def test_ctf_instantiate(ctf_ds_path):
    Ctf(ctf_ds_path)


def test_ctf_meg4_instantiate(ctf_ds_path):
    meg4_files = list(ctf_ds_path.glob("*.meg4"))
    assert meg4_files, "No .meg4 file found in CTF .ds directory"
    CtfMeg4(meg4_files[0])


def test_ctf_res4_instantiate(ctf_ds_path):
    res4_files = list(ctf_ds_path.glob("*.res4"))
    assert res4_files, "No .res4 file found in CTF .ds directory"
    CtfRes4(res4_files[0])


def test_ctf_infods_instantiate(ctf_ds_path):
    infods_files = list(ctf_ds_path.glob("*.infods"))
    assert infods_files, "No .infods file found in CTF .ds directory"
    CtfInfo(infods_files[0])


# ------------------------------
# MEG: KIT
# ------------------------------


def test_kit_instantiate(kit_sqd_path):
    Kit(kit_sqd_path)
