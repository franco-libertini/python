from mi_paquete.Cliente import Cliente, ClientePersonalizado

# Crear una instancia de ClientePersonalizado
cliente1 = ClientePersonalizado("franco", 26, "lincoln3605", "francolibertini1@hotmail.com")

# Enviar un correo electrónico personalizado
mensaje_personalizado = "Gracias por registrarte en nuestra tienda en línea."
cliente1.enviar_mail_personalizado(mensaje_personalizado)

# cliente1 = Cliente("nombre", edad, "direccion", "mail@txt.com")
cliente2 = Cliente("german", 22, "pringles 377", "dayana@gmail.com")

# cliente1.enviar_mail("¡Hola {self.nombre} Gracias por registrarte en nuestra tienda en línea.")
cliente2.realizar_compra("prenda")