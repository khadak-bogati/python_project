genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
C_tuple=(-5,1,-3)
C_tuple1=sorted(C_tuple)
print(C_tuple)
print(C_tuple1)
print(genres_tuple)
print(genres_tuple[3])
print(genres_tuple[3:6])
print(genres_tuple[0:2])
print(genres_tuple.index("disco"))



output
...................
(-5, 1, -3)
[-5, -3, 1]
('pop', 'rock', 'soul', 'hard rock', 'soft rock', 'R&B', 'progressive rock', 'disco')
hard rock
('hard rock', 'soft rock', 'R&B')
('pop', 'rock')
7
