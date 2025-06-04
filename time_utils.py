import datetime
from typing import List

def compress_times(timestamps: List[datetime.datetime], factor: float) -> List[datetime.datetime]:
    """Return new timestamps compressed by the given factor.

    Parameters
    ----------
    timestamps : list of datetime.datetime
        Original timeline to compress. The first timestamp acts as the origin.
    factor : float
        Compression factor. Values greater than 1 speed up the timeline.
    """
    if factor <= 0:
        raise ValueError("factor must be positive")
    if not timestamps:
        return []
    base = timestamps[0]
    return [base + (t - base) / factor for t in timestamps]

