# -*- coding: utf-8 -*-
#
# Carl is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Distributions.

Note: This module is only meant to be a minimally working prototype for
      composing and fitting distributions. It is not meant to be a full fledged
      replacement of RooFit or alikes.
"""

from .base import DistributionMixin
from .base import LikelihoodFreeMixin

from .normal import Normal
from .exponential import Exponential
from .uniform import Uniform
from .mixture import Mixture

from .histogram import Histogram
from .kde import KernelDensity

__all__ = ("DistributionMixin",
           "LikelihoodFreeMixin"
           "Normal",
           "Exponential",
           "Uniform",
           "Mixture",
           "Histogram",
           "KernelDensity")
