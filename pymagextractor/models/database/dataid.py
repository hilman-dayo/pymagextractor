from pymagextractor.models.annotations import Annotations
from pymagextractor.models.utils import create_dirs
import pathlib


class DataID:
    def __init__(self, data_id: str):
        self._data_id_dir = pathlib.Path(data_id)
        dirs = []

        self._data_dir = self._data_id_dir / "data"
        dirs.append(self._data_dir)
        self._anns_dir = self._data_id_dir / "annotations"
        dirs.append(self._anns_dir)

        create_dirs(dirs)

    def set_and_get_annotations(self, name, annotations_setting):
        return Annotations(name, annotations_setting, self._anns_dir)

    @property
    def buffer(self):
        """Return path to video or file of images within the DataID."""
        try:
            buffer = str(next(self._data_dir.glob("*.mp4")))
        except StopIteration:
             buffer = None
        return buffer