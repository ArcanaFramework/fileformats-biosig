import typing as ty
from pathlib import Path
from fileformats.core import FileSet, extra


class Biosig(FileSet):
    """Base class for biophysical time-series recordings"""

    @extra
    def deidentify(
        self,
        out_dir: Path | None = None,
        new_stem: str | None = None,
        copy_mode: FileSet.CopyMode = FileSet.CopyMode.copy,
    ) -> ty.Self:
        """Returns a new copy of the image with any subject-identifying information
        stripped from the from the image header"""
        raise NotImplementedError
