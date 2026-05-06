server = {
    "cliente" : {
        "telefono" : 3208776408,
        "mascotas" : {
            "firulais" : {
                "especie" : "pastor",
                "peso" : "10"
            }
        }

    }
}

detalles = server["cliente"]["mascotas"]["firulais"]

print(f" la mascota firulais tiene {detalles["peso"]}Kg ")