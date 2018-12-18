[![pyversions](https://img.shields.io/pypi/pyversions/omega_index.svg)](https://badge.fury.io/py/omega_index)
[![Updates](https://pyup.io/repos/github/isaranto/omega_index/shield.svg)](https://pyup.io/repos/github/isaranto/omega_index/)
[![PyPI version](https://badge.fury.io/py/omega_index.svg)](https://badge.fury.io/py/omega_index)


# omega_index
Omega Index for evaluation of overlapping community structure

Implemented the omega index for ovelapping clusters as described in the reference below.

> Gabriel Murray, Giuseppe Carenini, and Raymond Ng. 2012. Using the omega index for evaluating abstractive community detection. In Proceedings of Workshop on Evaluation Metrics and System Comparison for Automatic Summarization. Association for Computational Linguistics, Stroudsburg, PA, USA, 10-18.


## Installation

You can simply use `pip` for installation:

    $ pip install omega_index

or, if you prefer a local user installation:

    $ pip install --user omega_index
    
## Usage

To evaluate a specific clustering output **ground-truth data** .
The input (for both the clustering assignment and the ground truth) is a dictionary in the following form:

```python
communities = {
    "com1": ["item1", "item2"],
    "com2": ["item3", "item4"],
    "com3": ["item5", "item6", "item9"],
    "com4": ["item7", "item8"],
    "com5": ["item9", "item10", "item4"],
    "com6": ["item11", "item12"],
    "com7": ["item13", "item14"]
}
```
In the above example we have ovelapping clusters, as item4 is both in the 2nd as well as the 5th community.
Note that cluster/community names/IDS between the two dictionaries do not need to be the same, because
algorithm examines the number of co occurrence of nodes in clusters rather than try to solve the cluster
correspondence problem.

```python
from omega_index import Omega

omega = Omega(communities, ground_truth_communities)
print(omega.omega_score)

```
