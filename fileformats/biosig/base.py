import typing as ty
import os
from fileformats.core import FileSet, extra


class Biosig(FileSet):
    """Base class for biophysical time-series recordings"""

    @extra
    def deidentify(
        self,
        spec: ty.Any = None,
        out_dir: os.PathLike[str] | None = None,
    ) -> tuple[ty.Self, dict[str, ty.Any]]:
        """
        Deidentifies the dataset by stripping any subject-identifying information from the
        image header. The exact implementation of this method will depend on the
        specific image format and the type of identifying information that is present.

        Parameters
        ----------
        spec: Any, optional
            A specification for the deidentification process, which may include details on
            which fields to remove or how to handle certain types of data. The exact
            structure of this specification will depend on the specific image format and the
            requirements of the deidentification process.

        Returns
        -------
        Self
            A new instance of the image with any subject-identifying information stripped from
            the image header.
        dict[str, Any]
            A JSON-like nested dictionary containing the original values from the header that
            were stripped/modified during the deidentification process.
        """
        raise NotImplementedError
