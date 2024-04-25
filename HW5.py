my_list = ['apple', 'peach','blueberry','watermelon','orange']
print('List:', my_list)
print('First element:', my_list[0])    #Спросонья плохо запоминается, приходилось часто обращаться к материалу, мы ведь закрепим все все материалы пройденные к концу курса?
print('Last element:', my_list[-1])
print('Sublist:', my_list[2:5])
my_list[2] = 'limon'
print('Modified list:', my_list)

my_dict = {'apple': 'яблоко', 'blueberry':  'черника', 'peach': 'персик', "watermelon": 'арбуз,', 'orange': 'апельсин'}
print('Dictionary:', my_dict)
print('Translate:', my_dict['apple']), print('Translate:', my_dict['peach']), print('Translate:', my_dict['orange'])
my_dict['apple'] = 'ЯбЛоКо'; my_dict['monkey'] = 'обезьяна'
print('Modified dictionary:', my_dict)