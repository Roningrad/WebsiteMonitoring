from selenium import webdriver
import time

# устанавливаем драйвер браузера, например, Firefox
driver = webdriver.Firefox(executable_path=r'C:\Python34\geckodriver.exe')

# 10 секунд в качестве максимального таймаута для выполнения методов
driver.implicitly_wait(10)

# создаём беспрерывный цикл
while True:

	# открываем список тестируемых сайтов 
	configfile = "config.txt"	
	config = open(configfile, 'r')
		
	# открываем файл с результатами в режим записи
	resultfile = "result.txt"	
	result = open(resultfile, 'r')

	# сохраняем файл с ранее полученными результатами построчно в список (если результатов ещё нет - список останется пустым)
	result_list = []
	result_list = result.read().splitlines()

	# извлекаем адреса сайтов из файла, замеряем время отклика, сохраняем его в список результатов
	for line in config.readlines():
		if line[-1:] == '\n': line = line[:-1]
		start_time = time.time()
		driver.get(line)
		end_time = time.time()
		result_time = end_time - start_time
		time.sleep(3)
		for i in range(len(result_list)):
			# если сайт уже есть в списке результатов - добавляем к нему новое значение
			if line in result_list[i]:
				result_list[i] = result_list[i] + '; ' + str(round(result_time, 2)) + '\n'
	
		# если сайта ещё нет в списке результатов - заносим сайт в список
		if line not in str(result_list):
			result_list.append(line + ': ' + str(round(result_time, 2)) + '\n')
		driver.refresh()

	# перезаписываем файл с результатами
	open(resultfile, 'w').write('')
	for item in result_list:
		open(resultfile, 'a').write(item)
	
# обычно выход из браузера осуществляется так, но программа не дойдёт до этой части ввиду беспрерывного цикла
driver.quit()