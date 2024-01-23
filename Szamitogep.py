class Szamitogep:
    def __init__(self,sor: str):
        sor = sor.strip().split(";")
        self.op_r = str(sor[0])
        self.ram = int(sor[1])
