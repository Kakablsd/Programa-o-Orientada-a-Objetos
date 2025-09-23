class Celular:
    def mostrar_marca(marca):
        print(f'Sua marca é: {marca}')

    def mostrar_modelo(modelo):
        print(f'seu modelo é: {modelo}')

    def mostrar_tudo(marca, modelo):
        print(f"seu aparelho é o {marca} {modelo}")


marc = "iPhone"
model = "11 Pro Max"

Celular.mostrar_marca(marc)

Celular.mostrar_modelo(model)

Celular.mostrar_tudo(marc,model)
