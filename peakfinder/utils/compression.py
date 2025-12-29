"""Compression utilities for handling duplicate values in peak detection."""

from typing import List, Tuple

import numpy as np


def compress_duplicates(arr: np.ndarray) -> Tuple[np.ndarray, List[int]]:
    """
    Compress consecutive duplicate values in an array.

    For peak detection, we only need to consider unique consecutive values.
    This function reduces the array size while preserving peak information.

    Parameters
    ----------
    arr : np.ndarray
        Input 1D array that may contain duplicates.

    Returns
    -------
    compressed : np.ndarray
        Array with consecutive duplicates removed.
    indices : List[int]
        Original indices corresponding to each compressed value.
        The last index in each group of duplicates is kept.

    Examples
    --------
    >>> arr = np.array([1, 2, 2, 2, 3, 3, 4])
    >>> compressed, indices = compress_duplicates(arr)
    >>> compressed
    array([1, 2, 3, 4])
    >>> indices
    [0, 3, 5, 6]
    """
    if len(arr) == 0:
        return np.array([]), []

    compressed: List[float] = []
    indices: List[int] = []

    compressed.append(arr[0])
    indices.append(0)

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            compressed.append(arr[i])
            indices.append(i)

    return np.array(compressed), indices


def expand_peak_indices(
    peak_indices: List[int], original_indices: List[int]
) -> List[int]:
    """
    Expand compressed peak indices back to original array indices.

    Parameters
    ----------
    peak_indices : List[int]
        Peak indices in the compressed array.
    original_indices : List[int]
        Mapping from compressed indices to original indices.

    Returns
    -------
    List[int]
        Peak indices in the original array.

    Examples
    --------
    >>> original_indices = [0, 3, 5, 6]
    >>> peak_indices = [1, 3]  # peaks at positions 1 and 3 in compressed array
    >>> expand_peak_indices(peak_indices, original_indices)
    [3, 6]
    """
    return [original_indices[idx] for idx in peak_indices if idx < len(original_indices)]

