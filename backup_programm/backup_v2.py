import os, time
source = ["/Users/galstanarutun/Documents/Python/First/backup_programm/"]

target_dir = '/Users/galstanarutun/Documents/Python/backup_code'

today = target_dir + os.sep + time.strftime('%d-%m-%Y')
now = time.strftime('%H-%M-%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')