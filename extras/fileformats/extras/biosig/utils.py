import json
import typing as ty

import mne
import mne.io


def mne_deidentify(
    raw: mne.io.BaseRaw,
    spec: ty.Any = None,
) -> mne.Info:
    """Anonymize an MNE Raw object and return the deidentified Info.

    Callers that need to know what was changed (e.g. for a re-identification audit
    trail) should diff `metadata` before and after instead of relying on this
    function to report it, since that works uniformly across formats.
    """
    kwargs = json.load(open(spec)) if spec is not None else {}
    return mne.io.anonymize_info(raw.info, verbose=None, **kwargs)
