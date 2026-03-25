import typing as ty

import mne


def _info_to_metadata(info: mne.Info) -> dict[str, ty.Any]:
    """Extract study-sorting fields from an MNE Info object."""
    subj = info.get("subject_info") or {}
    dev = info.get("device_info") or {}
    return {
        # Subject
        "subject_id": subj.get("id"),
        "subject_first_name": subj.get("first_name"),
        "subject_last_name": subj.get("last_name"),
        "subject_birthday": subj.get("birthday"),
        "subject_sex": subj.get("sex"),
        "subject_hand": subj.get("hand"),
        # Study
        "proj_name": info.get("proj_name"),
        "proj_id": info.get("proj_id"),
        "experimenter": info.get("experimenter"),
        "description": info.get("description"),
        # Recording
        "meas_date": info.get("meas_date"),
        "utc_offset": info.get("utc_offset"),
        # Acquisition
        "sfreq": info.get("sfreq"),
        "nchan": info.get("nchan"),
        "highpass": info.get("highpass"),
        "lowpass": info.get("lowpass"),
        # Device
        "device_type": dev.get("type"),
        "device_model": dev.get("model"),
        "device_serial": dev.get("serial"),
        "device_site": dev.get("site"),
    }
