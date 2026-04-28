import struct

for x in ['b','h','i','q']:
    paquete = struct.pack('h', 42)
    print(f'El valor 42 empaquetado con el formato {x} es: {paquete}')
    print(len(struct.pack('h', 42)))
    print(struct.pack(x, 42).hex())



for x in ['f','d']:
    paquete = struct.pack(x, 3.14)
    print(f'El valor 3.14 empaquetado con el formato {x} es: {paquete}')
    print(len(struct.pack(x, 3.14)))
    print(struct.pack(x, 3.14).hex())

for x in ['3s','10s','2s']:
    paquete = struct.pack(x, b'Ada')
    print(f'El valor "Ada" empaquetado con el formato {x} es: {paquete}')
    print(len(struct.pack(x, b'Ada')))
    print(struct.pack(x, b'Ada').hex())
    print
