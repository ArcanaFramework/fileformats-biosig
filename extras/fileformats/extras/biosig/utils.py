import json
import typing as ty

import mne
import mne.io


def mne_deidentify(
    raw: mne.io.BaseRaw,
    spec: ty.Any = None,
) -> tuple[mne.Info, dict[str, ty.Any]]:
    """Anonymize an MNE Raw object and return the deidentified Info alongside
    a dict of the original values that were stripped or changed."""
    orig_info_dict = raw.info.to_json_dict()
    kwargs = json.load(open(spec)) if spec is not None else {}
    deidentified_info = mne.io.anonymize_info(raw.info, verbose=None, **kwargs)
    reid = dict_diff(orig_info_dict, deidentified_info.to_json_dict())
    return deidentified_info, reid


def dict_diff(
    orig: ty.Mapping[str, ty.Any], new: ty.Mapping[str, ty.Any]
) -> dict[str, ty.Any]:
    """Get a dict of all fields in orig that are not present or differ in new.
    For nested dicts, the diff is applied recursively.
    """
    result = {}
    for k, v in orig.items():
        if k not in new:
            result[k] = v
        elif isinstance(v, dict) and isinstance(new[k], dict):
            nested = dict_diff(v, new[k])
            if nested:
                result[k] = nested
        elif v != new[k]:
            result[k] = v
    return result
