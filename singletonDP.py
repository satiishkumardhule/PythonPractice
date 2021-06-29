class Borg:
    _shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state

    def __str__(self) -> str:
        return str(self.__dict__)

class Singleton(Borg):
    def __init__(self,**kwargs) -> None:
        super().__init__()
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        return super().__str__()


x = Singleton(HTTP="Hypertext Transfer Protocal")

print(x)

y = Singleton(SNMP= "Sinple Network Management Protocal")

print(y)