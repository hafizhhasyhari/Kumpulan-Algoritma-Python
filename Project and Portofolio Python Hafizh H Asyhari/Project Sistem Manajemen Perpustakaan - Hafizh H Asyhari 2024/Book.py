// Program Buku //
// Sistem Manajemen Perpustakaan //
// Author by Hafizh H Asyhari //
// Date : 2024 //

class Book:
    def __init__(self,Title="",Publisher="",ISBN_10="",ISBN_13="",option="",NUM_of_copies=""):
        self.Title = Title
        self.option = option
        self.Publisher = Publisher
        self.ISBN_10 = ISBN_10
        self.ISBN_13 = ISBN_13
        self.NUM_of_copies = NUM_of_copies

    def increase_copies(self, num):
        self.NUM_of_copies += num

    def decrease_copies(self, num):
        self.NUM_of_copies -= num
