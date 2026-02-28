from typing import List

class CanalNotificacion:
    def __init__(self, nombre_canal:str, destinatario: str) -> None:
        self.nombre_canal: str = nombre_canal
        self.destinatario: str = destinatario

    def enviar(self, mensaje:str) -> str:
        raise NotImplementedError(f"La clase '{type(self).__name__}' debe implementar el método enviar()")
    

    def calcular_costo(self) -> float:
        raise NotImplementedError(f"La clase '{type(self).__name__}' debe implementar el método calcular_costo()")
    
    def __str__(self) -> str:
        return f"Canal de Notificación: {self.nombre_canal}, Destinatario: {self.destinatario}"
    

class NotificacionEmail(CanalNotificacion):
    def __init__(self, destinatario:str, direccion_email:str, tiene_adjunto:bool) -> None:
        super().__init__(nombre_canal="Email", destinatario=destinatario)
        # Atributo especifico de la clase NotificacionEmail
        self.direccion_email: str = direccion_email
        self.tiene_adjunto: bool = tiene_adjunto

    def enviar(self, mensaje: str) -> str:
        adjunto:str = "con adjunto" if self.tiene_adjunto else "sin adjunto"
        return f"Enviando email a {self.destinatario} ({self.direccion_email}) {adjunto}: {mensaje}"
    
    def calcular_costo(self) -> float:
        costo_base: float = 0.05 # tarifa fija por email
        costo_adjunto: float = 0.10 if self.tiene_adjunto else 0.0
        return costo_base + costo_adjunto


def demostrar_polimorfismo_con_tipos() -> None:
    print("Demostración de Polimorfismo con Herencia")
    email_sofia: NotificacionEmail = NotificacionEmail(destinatario="Sofía", direccion_email="sofia@example.com", tiene_adjunto=True)
    demostrar_not_implement_error(email_sofia)

def demostrar_not_implement_error(canal: CanalNotificacion) -> None:
    try:
        canal.enviar("Mensaje de prueba")
        canal.calcular_costo()
    except NotImplementedError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    demostrar_polimorfismo_con_tipos()
    