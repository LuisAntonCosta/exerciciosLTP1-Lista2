class Motor:
    def status(self):
        return "Motor: sem danos"

class Pneu:
    def status(self):
        return "Pneu: ponto para partir"

class Veiculo(Motor, Pneu):
    def status(self):
        motor_status = super().status()
        pneu_status = Pneu.status(self)
        return f"{motor_status}\n{pneu_status}"

if _name_ == "_main_":
    veiculo = Veiculo()
    print(veiculo.status())
