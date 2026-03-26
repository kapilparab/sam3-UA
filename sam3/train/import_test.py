# Copyright (c) Meta Platforms, Inc. and affiliates. All Rights Reserved

# pyre-unsafe

import logging
import os
import random
import sys
import traceback
from argparse import ArgumentParser
from copy import deepcopy

import submitit
import torch
from hydra import compose, initialize_config_module
from hydra.utils import instantiate
from iopath.common.file_io import g_pathmgr
from omegaconf import OmegaConf
from sam3.train.utils.train_utils import makedir, register_omegaconf_resolvers
from tqdm import tqdm


os.environ["HYDRA_FULL_ERROR"] = "1"

print("All packages imported")
