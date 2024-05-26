# Kontrol Program Match

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "Tetap setia!"
        case _:
            return "Something's wrong with the internet"

# Program utama
status = [400,404,418,'_']

for t in status:
    print(http_error(t))      # Mengeksekusi fungsi
