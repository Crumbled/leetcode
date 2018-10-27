def generate_user(txt):
	pattern1 = re.compile(r"[0-9]+%(user)|(user) [0-9]+%")
	pattern2 = re.compile(r'\d+')
	string = pattern1.search(txt)
	if string==None:
		res = ['0']
	else:
		res = pattern2.findall(string.group())
		# res = int(res)
	return res
def loginfo_feature(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = open(path + "/" + file, 'r', encoding='UTF-8')  # 打开文件
            data = f.read()
            txt = data.lower()
            res = generate_info(txt)
            res = np.tile(res, (50, 1))
            s.append(res)
    s = np.array(s)
    return s/100