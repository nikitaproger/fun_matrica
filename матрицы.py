import random
class matr:
    def __init__ (self, comand):
        self.comand = comand
        self.avto_mat()
    def avto_mat(self):
        match self.comand:
            case 1:
                self.matrica = [[0] * 2 for _ in range(2)]
                for m in range(2):
                    for n in range(2):
                        self.matrica[m][n] = int(input(f'ВВ эл[{m}][{n}] = '))
            case 2:
                self.matrica = [[0]*2 for _ in range(2)]
                for m in range(2):
                    for n in range(2):
                        self.matrica[m][n] = random.randint(0, 99)
        print('='*50,'\n', 'создана Матрица 2х2')
        print(*self.matrica, sep='\n')
        return self.matrica
    def pov_ranga(matrica):
        mat = matrica
        mat.append([1, 1, 1])
        mat[0], mat[1], mat[2] = mat[2], mat[0], mat[1]
        mat[1].append(1)
        mat[2].append(1)
        mat[1][0], mat[1][1], mat[1][2] = mat[1][2], mat[1][0], mat[1][1]
        mat[2][0], mat[2][1], mat[2][2] = mat[2][2], mat[2][0], mat[2][1]
        return mat
    def razmn_matr(self):
        self.min_a = [[self.matrica[1][1],self.matrica[1][2]],[self.matrica[2][1],self.matrica[2][2]]]
        matr.pov_ranga(self.min_a)
        self.min_b = [[self.matrica[1][0], self.matrica[1][2]], [self.matrica[2][0], self.matrica[2][2]]]
        matr.pov_ranga(self.min_b)
        self.min_c = [[self.matrica[1][0], self.matrica[1][1]], [self.matrica[2][0], self.matrica[2][1]]]
        matr.pov_ranga(self.min_c)
        return self.min_a, self.min_b, self.min_c
print('='*60)
print('Программа для различный не класических манипуляций с матрицами')
print('='*50)
print('''выберите команду:
1 задать матрицу 2 x 2
2 создать афтоматически матрицу 2 x 2''')
print('='*60)
a = matr(int(input('Ввод: ')))
print('=' * 60,'\n','''теперь когда матрица создана код выполнит неcколько действий:
1 повысит ранг этой матрицы
2 размножит её из её же миноров 
3 убет её, а имено сделает нулевой''')

print('=' * 60, '\n', '1 действие: повышен ранг матрицы')
izm_izn_mat = a.matrica
pov_mat = matr.pov_ranga(izm_izn_mat)
print(*pov_mat, sep='\n')

print('=' * 60, '\n', '2 действие: размножена матрица\nэто получившиеся матрицы')
ma, mb, mc = a.razmn_matr()
print(*ma,'\t',*mb,'\t',*mc, sep='\n')

zero_matr = [[0]*3 for _ in range(3)]

print('=' * 60, '\n', '3 действие: убем эти мтарицы')
print(*zero_matr,'\t',*zero_matr,'\t',*zero_matr, sep='\n')