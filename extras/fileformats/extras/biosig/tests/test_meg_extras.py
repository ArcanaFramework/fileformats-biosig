"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.biosig import Ctf, Kit, Fif

# ------------------------------
# MEG: CTF
# ------------------------------


def test_ctf_read_metadata(ctf_ds_path):
    metadata = Ctf(ctf_ds_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None


# ------------------------------
# MEG: FIF
# ------------------------------


def test_fif_read_metadata(fif_path):
    metadata = Fif(fif_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None


def test_fif_deidentify(fif_path, tmp_path):
    fif = Fif(fif_path)
    orig_metadata = fif.metadata

    deid_fif, reid = fif.deidentify(out_dir=tmp_path)

    assert isinstance(deid_fif, Fif)
    assert isinstance(reid, dict)
    assert reid, "expected at least one field to be stripped or changed"

    deid_metadata = deid_fif.metadata

    # Every field recorded in reid should differ between original and deidentified
    for key in reid:
        assert orig_metadata.get(key) != deid_metadata.get(
            key
        ), f"reid claims '{key}' changed but original and deidentified values match"

    # Subject identifying fields should be absent or cleared in the deidentified file
    deid_subject_info = deid_metadata.get("subject_info") or {}
    for pii_field in ("last_name", "first_name", "birthday"):
        assert not deid_subject_info.get(
            pii_field
        ), f"subject_info.{pii_field} was not cleared by deidentification"


# ------------------------------
# MEG: KIT
# ------------------------------


def test_kit_read_metadata(kit_sqd_path):
    metadata = Kit(kit_sqd_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
