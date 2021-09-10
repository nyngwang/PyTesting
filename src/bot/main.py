from . import sib1
from ..mod import module1


def hello():
    sib1.f_sib1()
    module1.hello()

    # for k, v in sys.modules.items():
    #     print(f'{k}: {v.__name__}')
    # print()

