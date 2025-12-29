# Segment Tree Usage

Advanced data structures for efficient range queries.

## Overview

PeakFinder includes data structures for efficient range queries:

- **Segment Tree**: For counting peaks in subarrays
- **RMQ (Range Maximum Query)**: For finding maximum values in ranges

## Segment Tree

### Basic Usage

```python
from peakfinder.structures.segment_tree import SegmentTree
import numpy as np

arr = np.array([1, 5, 2, 6, 3, 4, 2])
tree = SegmentTree(arr)

# Count peaks in the entire array
count = tree.count_peaks_in_range(0, len(arr) - 1)
print(f"Total peaks: {count}")

# Count peaks in a subarray
count_sub = tree.count_peaks_in_range(1, 4)
print(f"Peaks in range [1:4]: {count_sub}")
```

### When to Use Segment Tree

Use segment tree when:
- You need multiple range queries on the same array
- The array is large
- You're doing repeated operations

**Time Complexity**:
- Build: O(n)
- Query: O(log n)

## RMQ (Range Maximum Query)

### Basic Usage

```python
from peakfinder.structures.rmq import RMQ
import numpy as np

arr = np.array([1, 5, 2, 6, 3, 4, 2])
rmq = RMQ(arr)

# Find maximum in range [0, 4]
max_idx = rmq.query(0, 4)
print(f"Maximum at index {max_idx}, value {arr[max_idx]}")

# Get maximum value directly
max_val = rmq.query_value(0, 4)
print(f"Maximum value: {max_val}")
```

### RMQ Use Cases

RMQ is useful for:
- Finding maximum values in ranges
- Optimizing peak detection in specific ranges
- Range-based queries

**Time Complexity**:
- Preprocessing: O(n log n)
- Query: O(1)

## Example: Range-Based Peak Analysis

```python
from peakfinder.structures.rmq import RMQ
import numpy as np

# Signal data
signal = np.array([1, 5, 2, 6, 3, 4, 2, 7, 1, 3, 5, 2])

# Build RMQ structure
rmq = RMQ(signal)

# Analyze different time windows
windows = [(0, 3), (4, 7), (8, 11)]

for start, end in windows:
    max_idx = rmq.query(start, end)
    max_val = rmq.query_value(start, end)
    print(f"Window [{start}:{end}]: max at {max_idx}, value {max_val}")
```

## Example: Sliding Window Peak Counting

```python
from peakfinder.structures.segment_tree import SegmentTree
import numpy as np

arr = np.array([1, 5, 2, 6, 3, 4, 2, 7, 1, 3, 5, 2])
tree = SegmentTree(arr)

# Count peaks in sliding windows
window_size = 5
for i in range(len(arr) - window_size + 1):
    end = i + window_size - 1
    count = tree.count_peaks_in_range(i, end)
    print(f"Window [{i}:{end}]: {count} peaks")
```

## Performance Tips

1. **Preprocessing Cost**: Both structures require preprocessing. Use them when you have multiple queries.

2. **Memory**: Segment tree uses O(n) space, RMQ uses O(n log n) space.

3. **Query Frequency**: If you only need one query, use the simpler linear methods.

## Comparison

| Structure | Preprocessing | Query Time | Space | Best For |
|-----------|--------------|------------|-------|----------|
| Segment Tree | O(n) | O(log n) | O(n) | Peak counting in ranges |
| RMQ | O(n log n) | O(1) | O(n log n) | Maximum value queries |

## Next Steps

- Learn about [Peak Counting](peak_counting.md) for basic counting
- Check out [1D Peak Detection](peak_1d_examples.md) for finding peaks
- Explore the [API Reference](../README.md#api-reference)

