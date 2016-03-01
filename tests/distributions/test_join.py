# -*- coding: utf-8 -*-
#
# Carl is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

import numpy as np

from numpy.testing import assert_array_equal
from sklearn.utils import check_random_state

from carl.distributions import Join
from carl.distributions import Normal


def test_join():
    p = Join(components=[Normal(mu=0, random_state=0),
                         Normal(mu=1, random_state=1),
                         Normal(mu=2, random_state=2)], random_state=0)
    assert p.ndim == 3
    assert len(p.parameters_) == 6

    X = p.rvs(10000)
    assert X.shape == (10000, 3)
    assert np.abs(np.mean(X[:, 0]) - p.components[0].mu.eval()) < 0.05
    assert np.abs(np.mean(X[:, 1]) - p.components[1].mu.eval()) < 0.05
    assert np.abs(np.mean(X[:, 2]) - p.components[2].mu.eval()) < 0.05