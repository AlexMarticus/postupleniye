
# print(allabits)
# abiturients = []
# for abit in allabits[4]:
#     abit = abit.find('div', class_='RatingPage_table__item__qMY0F')
#     color = abit.get('class')
#     if len(color) == 2:
#         if color[1][-5:] == 'QR1Ww':
#             color = 'сер'
#         elif color[1][-5:] == 'InEVk':
#             color = 'зел'
#         else:
#             color = 'жел'
#     else:
#         color = 'нет'
#     num_v_list, snils = abit.find('p', class_='RatingPage_table__position__uYWvi').text.split()
#     num_v_list, snils = int(num_v_list), snils[1:]
#     snils = f'{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:]}'
#     print(color, num_v_list, snils)
