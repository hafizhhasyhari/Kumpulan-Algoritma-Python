def main():
    bahasa = 'Python'
    versi = 3
    
    print(bahasa, versi)             # tidak membutuhkan spasi
    print(bahasa + ' ' + str(versi)) # membutuhkan spasi
    print('%s %d' % (bahasa, versi))
    print('{} {}'.format(bahasa, versi))
    print(f'{bahasa} {versi}')
    
if __name__ == '__main__':
        main()

// by hafizhhasyhari //
