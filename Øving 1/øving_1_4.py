user_input = float(input('Skriv inn et desimaltall: '))
print ('Konvertert med int() ble tallet', int(user_input))
print ('Konvertert tilbake blir tallet', float(int(user_input)))

print ('Denne verdien er etter round(): ', round(user_input))
antall_desimaler = int(input('Hvor mange desimaltall vil du runde til? '))
print ('Rundet til', antall_desimaler, 'desimaler, blir tallet:', round(user_input, antall_desimaler))
