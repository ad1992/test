from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, c_string_sg_1: str="test", **kwargs):
        self.c_string_sg_1 = c_string_sg_1
        pass

    def update(self, updated_config):
        self.c_string_sg_1 = updated_config.c_string_sg_1
        pass

Config = SubgraphConfig()
