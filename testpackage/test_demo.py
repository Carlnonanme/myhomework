import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env',yaml.safe_load(open('./env.yml')))
    def test_demo(self,env):
        if 'test' in env:
            print("which is test env")
            print(env['test'])
        elif 'dev' in env:
            print('this is programmer env')
            print(env)
    # def test_yaml(self):
    #     print(yaml.safe_load(open('./')))