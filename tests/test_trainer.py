import pytest

from pl_cross.trainer import KFoldLoop, Trainer


def test_trainer_initialization():
    with pytest.raises(ValueError):
        Trainer(num_folds=2.5)

    with pytest.raises(ValueError):
        Trainer(num_folds=1)

    with pytest.raises(ValueError):
        Trainer(shuffle=2)

    with pytest.raises(ValueError):
        Trainer(stratified=2)
