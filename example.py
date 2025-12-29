#!/usr/bin/env python3
"""Example script demonstrating PeakFinder usage."""

import numpy as np
from peakfinder import PeakDetector

def main():
    print("PeakFinder Example")
    print("=" * 50)
    
    # 1D Example
    print("\n1D Peak Detection:")
    arr = np.array([1, 3, 2, 5, 4])
    print(f"Array: {arr}")
    detector = PeakDetector(arr)
    peak = detector.find_any_peak()
    print(f"Peak at index {peak}, value {arr[peak]}")
    
    # Find all peaks
    all_peaks = detector.find_all_peaks()
    print(f"All peaks at indices: {all_peaks}")
    
    # Count peaks
    count = detector.count_peaks()
    print(f"Total peaks: {count}")
    
    # 2D Example
    print("\n2D Peak Detection:")
    matrix = np.array([[1, 2, 3], [4, 9, 5], [6, 7, 8]])
    print(f"Matrix:\n{matrix}")
    detector_2d = PeakDetector(matrix)
    row, col = detector_2d.find_peak_2d()
    print(f"Peak at row {row}, column {col}, value {matrix[row, col]}")
    
    # Different modes
    print("\nAlgorithm Modes:")
    arr = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
    for mode in ["auto", "brute", "binary", "hybrid"]:
        detector = PeakDetector(arr, mode=mode)
        peak = detector.find_any_peak()
        print(f"  {mode:6s}: Peak at index {peak}")
    
    print("\nExample completed successfully!")

if __name__ == "__main__":
    main()

