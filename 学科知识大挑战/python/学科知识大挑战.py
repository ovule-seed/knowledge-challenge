from tkinter import Tk
import random
import time
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import threading
from playsound import playsound
import os


# 选择的题库
subject = []

# 历史题库
subject_history = [['中国现代史开始于（  ）', '中华人民共和国成立', '第一届中国人民政治协商会议召开', '辛亥革命', '鸦片战争'],
                   ['中国第一部社会主义类型的宪法颁布于（  ）', '1954', '1949', '1982', '2018'],
                   ['土地改革运动和抗美援朝战争相同作用是（  ）', '巩固人民政权',
                       '探索社会主义道路', '推翻封建制度', '实现社会主义现代化'],
                   ['“文革十年动乱”是指（  ）', '1966年-1976年', '1956年-1966年',
                    '1965年-1966年', '1967年-1977年'],
                   ['20世纪90年代，我国改革开放进一步深化和取得显著成就的重要标志是（  ）',
                    '浦东开发区', '珠海经济特区', '汕头经济特区', '厦门经济特区'],
                   ['我国的经济体制改革先从哪里开始 （  ）', '农村', '城市', '国企', '中央'],
                   ['（  ）被称作是70年代中国外交史上最伟大的胜利', '中美两国正式建立了外交关系',
                    '中国恢复联合国的合法席位', '中美两国将世世代代友好下去', '中日两国关系的坚冰开始融化'],
                   ['“一五”计划的基本任务是（ ）', '集中主要力量发展重工业',
                       '加速实现手工业的合作化', '逐步改造资本主义工商业', '大力发展轻工业'],
                   ['中共十一届三中全会的意义说法错误的是它完成了关于什么的拨乱反正（  ）',
                       '经济路线', '思想路线', '政治路线', '组织路线'],
                   ['1992年对于推动中国改革开放能够站在新的历史起点上再出发，具有承先启后、继往开来的作用。\n1992年被称为中国30年改革进程标志性的分水岭的主要依据是（  ）',
                    '确立了市场经济的改革目标', '制定了改革开放的基本国策', '形成了立体全面的开放格局', '作出国有企业改革的决定'],
                   ['邓小平被称为中国改革开放和社会主义现代化建设的总设计师，主要因为（ ）', '提出社会主义初级阶段理论',
                    '提出解决台湾问题的伟大构想', '在全国开展平反冤假错案工作', '解决了中国如何建设社会主义的问题'],
                   ['新中国建立后的外交方针是（ ）', '和平共处五项原则', '求同存异', '独立自主', '一国两制'],
                   ['“一国两制”构想的最初提出是为了解决（　）', '台湾问题', '统一问题', '香港问题', '澳门问题'],
                   ['“文化大革命”中形成的两个反革命集团的核心人物分别是（　）',
                       '林彪、江青', '林彪、王洪文', '王洪文、姚文元', '江青、姚文元'],
                   ['我国第一艘航空母舰是（　）', '辽宁舰', '上海舰', '青岛舰', '大连舰'],
                   ['我国第一颗原子爆炸的时间是', '1964年10月16日', '1966年10月16日',
                    '1966年11月16日', '1964年11月16日'],
                   ['2003年10月我国飞天第一人是', '杨利伟', '翟志刚', '袁隆平', '刘洋'],
                   ['新中国成立后土地改革的根本意义在', '消灭地主阶级，解放农村生产力',
                    '废除土地私有制', '实现社会主义土地公有制', '满足农民土地要求'],
                   ['能说明新中国的社会性质的是\n①《共同纲领》对中华人民共和国性质的规定②西藏和平解放③1950年开始的土地改革④抗美援朝',
                    '①③', '③④', '②④', '①②'],
                   ['为了维护国家领土完整和主权独立，新中国 ①召开了中国人民政治协商会议\n②新政协第一届全体会议任命周恩来为政务院总理③1951年和平解放西藏④1950年中国人民志愿军抗美援朝',
                    '③④', '①③', '②④', '①②'],
                   ['解决台湾问题的前提是', '一个中国的原则', '和平统一', '一国两制', '加强经济合作'],
                   ['从1949年召开人民政协第一届会议，到1954年召开第一届全国人大第一次会议，说明新中国', '政治建设逐渐步入法制化轨道',
                    '开始进行社会主义“三大改造”', '经济结构已发生重大变化', '土地改革已经发生重大变化']
                   ]
# 地理题库
subject_geography = [
    ['正确反映我国自然环境差异显著的是', '海南岛长夏无冬，黑龙江省长冬无夏', '东南沿海山清水秀，西北内陆沙漠、戈壁广布',
        '我国地势东高西低，呈阶梯状分布', '东北平原一年一熟，珠江三角洲两年三熟'],
    ['人类活动也呈现明显的差异。下列叙述不正确的是', '农作物具有南麦北稻、南甘北甜的分布特点', '人口、交通线表现为东密西疏的特点',
        '经济发展水平东部高、西部低', '农业具有西牧东耕的分布特点'],
    ['我国的港、澳、台地区，在经济发展上的相同特点是', '都有发达的旅游业',
        '都以博彩业为主', '都以钢铁、机械等重工业为主', '都以农业和农产品加工业为主'],
    ['下列地形区全位于南方地区的是', '四川盆地、东南丘陵', '黄土高原、东南丘陵', '长江中下游平原、东北平原', '华北平原、云贵高原'],
    ['黄土高原在独特的自然环境影响下，创造的独特黄土高原文化有\n①信天游 ②安塞腰鼓 ③永定土楼 ④窑洞', '①②④', '①③④', '①②③', '②③④'],
    ['关于北方地区自然地理特征的描述正确的是', '"北风卷地白草折，胡天八月即飞雪"是对该地区冬季景观的描述', '地跨中温带、暖温带，全部属于半湿润区',
        '地形以平原和高原为主', '该地区降水较少，春旱严重'],
    ['我国"南船北马"传统交通特点的主要成因是', '南北降水及河流特点的不同', '南北人口分布的差异', '南北植被类型不同', '南北气温高低的差异'],
    ['导致我国南、北方农耕制度不同的主要自然因素是', '气候', '地形', '技术', '土壤'],
    ['为实现可持续发展，“西气东输”工程建设时需要注意的是', '生态的保护', '资金的运用', '技术的革新', '人才的培养'],
    ['下列地理事物中，与青藏铁路沿线看到的景观特征不相符的是', '经济发达，人口稠密',
        '雪山连绵，冰川纵横', '藏民欢歌，青稞片片', '许多铁路高架，列车供氧'],
    ['以下是某同学赞美家乡的散文诗：“挽黄河臂膀，依太行身躯，踏千里黄土，采万年‘乌金’，揽五台佛光……”他赞美的是',
        '山西省', '陕西省', '山东省', '河南省'],
    ['关于我国重大工程建设的说法正确的是', '南水北调是把长江的水调入华北西北缓解那里的水资源不足的状况', '西气东输工程对缓解我国华北地区电力紧张的状况起重要作用',
        '我国四川云南贵州等地开发水电主要为满足本地的电力需求', '青藏铁路的修建将会给西部脆弱的生态环境带来不利影响'],
    ['某旅行社为了吸引游客特地推出了四条旅游线路，不属于西部的是', '红壤茶园', '丝路驼铃', '苗寨风情', '雪域高原']
]
# 道德与法治题库
subject_ethics_law = [
    ['我国的宪法原则是', '尊重和保障人权', '一切权利属于公民', '依法治国首先是依宪治国', '宪法是国家的根本大法'],
    ['2017年7月17日上午，228名身着检服、胸戴检章\n的最高人民检察院首批入额检察官，在最高人民检察院检察长曹建明的率领下，\n进行了庄严的宪法宣誓。你认为检察官为什么要向宪法宣誓？',
        '宪法是一切组织和个人的根本活动准则', '人民检察院坚持依法行政', '人民检察院独立行使检察权', '人民检察院是国家的法律监督机关'],
    ['中国的人权事业取得了巨大成就，但前进的路上仍困难重重，其中最大的障碍是', '贫穷', '不尊重人权', '法治观念淡薄', '教育水平不高'],
    ['十九大报告强调，要在发展中补齐民生短板、促进社会公平正义，在幼有所育、学有所教、劳有所得、\n病有所医、老有所养、住有所居、弱有所扶上不断取得新进展，深入开展脱贫攻坚，\n保证全体人民在共建共享发展中有更多获得感。这体现了',
        '增进民生福祉是发展的根本目的', '党和国家加强依法行政，保障和改善民生', '人民将享有更为广泛的民主权利和自由', '我国坚决维护公平正义，防止出现收入差距'],
    ['38岁的高红升，是安徽省黄山王村镇的副镇长，五月中旬，身处困境的他在滴滴网络约车平台\n上班时间接单被查，同时被当地的士司机举报至纪委。你认为这是该地的士司机在行使自己的',
        '监督权', '重大事项决定权', '政治权利', '文化权利'],
    ['我国各级政府工作部门正在全面推行清单制度， 推进政府机构、 职能、 权限、 程序和责任法定化， 厘清权力的边界。 这一措施（ ）',
     '说明依法治国首先是依法行政',
     '有利于推进依法行政',
     '有利于人民直接管理国家大事',
     '各级政府部门是国家最高的权力机关'
     ],
    ['中国特色社会主义最本质的特征是（ ）',
     '中国共产党领导',
     '公有制为主体、 多种所有制经济共同发展',
     '人民代表大会制度',
     '中国共产党领导的多党合作和政治协商制度'
     ],
    ['中国人民政治协商会议， 简称人民政协。 人民政协围绕团结和民主两大主题履行以下职能（ ）',
     '政治协商',
     '民主决策',
     '民主监督',
     '参政议政'
     ],
    ['公平是人类历史上的一个永恒话题。你认为下列对公平的理解中， 正确的是（ ）',
     '处理事情合情合理、不偏不倚的行为方式',
     '每个人都享受权利和义务',
     '公平就是做到权利运用公平',
     '做到了公平，社会上的一切事情也都迎刃而解了'
     ],
    ["人社部调整基本养老金水平的决定反映了哪些情况？",
     "体现了党和政府在致力于维护社会的公平正义",
     "说明社会主义制度具有无比的优越性",
     "说明我们已经不存在贫富差距",
     "说明我们的政府在坚持依法行政"],
    ["开展“晨读宪法”活动的目的是什么？",
     "是增强宪法意识，全面推进依法治国的需要",
     "体现了宪法制定和修改的程序比普通法律更严格",
     "是公民依法行使政治权利的体现",
     "体现了宪法是普通法律的立法基础"],
    ["我国的国家权力机关是什么？",
     "人民代表大会",
     "全国人民代表大会",
     "地方各级人民代表大会",
     "国务院"],
    ["下列哪项行为既正确行使了公民权利又履行了公民义务？",
     "李红同学提醒开公司的父亲要缴纳税款",
     "八年级学生小明，品学兼优，被评为“学习标兵”",
     "小赵同学在旅游景区刻上自己的名字",
     "李涛同学向同学借钱购买手机，却一直未归还"]
]




# 读取历史最高得分和上次得分
if not os.path.exists('score_record.txt'):
    with open('score_record.txt', 'w') as f:
        f.write('0 0 0')
try:
    with open('score_record.txt', 'r') as f:
        scores = f.read().split()
        if len(scores) == 0:
            high_score = 0
            last_score = 0
            last_played = "无记录"
        elif len(scores) == 1:
            high_score = int(scores[0])
            last_score = 0
            last_played = "无记录"
        else:
            high_score = int(scores[0])
            last_score = int(scores[1])
            last_played = scores[2]
except FileNotFoundError:
    high_score = 0
    last_score = 0
    last_played = "无记录"

# 创建标签并将历史最高分和上次得分添加到标签中

#点击音效
def play_click_sound():
    threading.Thread(target=lambda: playsound('sound/click.mp3')).start()

# 判断选择题库

def choose_subject(history, geography, ethics_law):
    global subject
    if history:
        subject = subject_history
        root.destroy()
    elif geography:
        subject = subject_geography
        root.destroy()
    elif ethics_law:
        subject = subject_ethics_law
        root.destroy()

#-----------------------选择题库-----------------------------
# 创建GUI
root = tk.Tk()
root.title("选择题库")
root.geometry('1000x700')
root.resizable(False, False)
root.configure(bg='#FFFFFF')
root.bind('<Button-1>', lambda event: play_click_sound())
# 加载图片文件
image_file = Image.open("image/cover.jpg")
image = ImageTk.PhotoImage(image_file)

# 创建标签并将图片添加到标签中
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

# 创建按钮
subject_label = tk.Label(root, text='选择题库', font=('微软雅黑', 20), bg='#FFFFFF')
subject_label.pack(pady=50)

score_label = tk.Label(root, text='历史最高分：{} \n上次得分：{} \n上次游玩时间：{}'.format(
    high_score, last_score, last_played), font=('微软雅黑', 14), bg='#FFFFFF')
score_label.pack(pady=20)

history_btn = tk.Button(
    root, text="             历史             ", font=('微软雅黑', 16), bg='#63B8FF', fg='#FFFFFF',
    command=lambda: choose_subject(True, False, False))
history_btn.place(relx=0.5, rely=0.4, anchor='center')
history_btn.bind("<Enter>", lambda event: history_btn.config(bg='#4D7DAA'))
history_btn.bind("<Leave>", lambda event: history_btn.config(bg='#63B8FF'))

geography_btn = tk.Button(
    root, text="             地理             ", font=('微软雅黑', 16), bg='#63B8FF', fg='#FFFFFF',
    command=lambda: choose_subject(False, True, False))
geography_btn.place(relx=0.5, rely=0.5, anchor='center')
geography_btn.bind("<Enter>", lambda event: geography_btn.config(bg='#4D7DAA'))
geography_btn.bind("<Leave>", lambda event: geography_btn.config(bg='#63B8FF'))

ethics_law_btn = tk.Button(
    root, text="             社会             ", font=('微软雅黑', 16), bg='#63B8FF', fg='#FFFFFF',
    command=lambda: choose_subject(False, False, True),)
ethics_law_btn.place(relx=0.5, rely=0.6, anchor='center')
ethics_law_btn.bind(
    "<Enter>", lambda event: ethics_law_btn.config(bg='#4D7DAA'))
ethics_law_btn.bind(
    "<Leave>", lambda event: ethics_law_btn.config(bg='#63B8FF'))

root.mainloop()

# ----------答题界面----------------
# 创建窗口
window = tk.Tk()
window.title('中国现代史学习软件')
window.geometry('1000x700')
window.resizable(False,False)
image_background = Image.open("image\\background.jpg")
image = ImageTk.PhotoImage(image_background)
window.bind('<Button-1>', lambda event: play_click_sound())

background2_label = tk.Label(window, image=image)
background2_label.place(relwidth=1, relheight=1)

# 创建控件
title_label = tk.Label(window, text='选择正确的选项', font=(
    '微软雅黑', 16), highlightthickness=0, foreground='white', background='red')
title_label.pack(pady=20)

subject_label = tk.Label(window, text=subject[0][0], font=(
    '微软雅黑', 14), foreground='white', background='red')
subject_label.pack(pady=10)

button1 = tk.Button(window, text=subject[0][1], font=('微软雅黑', 12, 'bold'), foreground='white', background='red',
                    command=lambda: handle_choice(subject[0][1]))
button1.pack(pady=10)
button1.bind("<Enter>", lambda event,
             h=button1: h.config(background='darkred'))
button1.bind("<Leave>", lambda event, h=button1: h.config(background='red'))

button2 = tk.Button(window, text=subject[0][2], font=('微软雅黑', 12, 'bold'), foreground='white', background='red',
                    command=lambda: handle_choice(subject[0][2]))
button2.pack(pady=10)
button2.bind("<Enter>", lambda event,
             h=button2: h.config(background='darkred'))
button2.bind("<Leave>", lambda event, h=button2: h.config(background='red'))

button3 = tk.Button(window, text=subject[0][3], font=('微软雅黑', 12, 'bold'), foreground='white', background='red',
                    command=lambda: handle_choice(subject[0][3]))
button3.pack(pady=10)
button3.bind("<Enter>", lambda event,
             h=button3: h.config(background='darkred'))
button3.bind("<Leave>", lambda event, h=button3: h.config(background='red'))

button4 = tk.Button(window, text=subject[0][4], font=('微软雅黑', 12, 'bold'), foreground='white', background='red',
                    command=lambda: handle_choice(subject[0][4]))
button4.pack(pady=10)
button4.bind("<Enter>", lambda event,
             h=button4: h.config(background='darkred'))
button4.bind("<Leave>", lambda event, h=button4: h.config(background='red'))


score_label = tk.Label(window, text='得分：0', font=(
    '微软雅黑', 14), foreground='white', background='red')
score_label.pack(pady=20)

check_label = tk.Label(window, text='', font=(
    '微软雅黑', 14), foreground='white', background='red')
check_label.pack(pady=20)

timer_label = tk.Label(window, text='计时器：0秒', font=(
    '微软雅黑', 14), foreground='white', background='yellow')
timer_label.pack(side='top', pady=10)


# 处理选择


def handle_choice(choice):
    global score, current_subject, start_time
    while True:
        if choice == subject[current_subject][1]:
            score += 1
            score_label.config(text=f'得分：{score}')
            check_label.config(text = '正确')
            current_subject += 1
            current_subject = random.randint(0,len(subject)-1)#保障题目无序给出
            break
        else:
            score -= 1
            score_label.config(text=f'得分：{score}')
            check_label.config(text=f'错误')
            break

    
    while current_subject < len(subject):
        options = [subject[current_subject][1], subject[current_subject]
                   [2], subject[current_subject][3], subject[current_subject][4]]
        if mode.get() == 1:
            random.shuffle(options)
        button1.config(state='normal', text=options[0],
                       command=lambda: handle_choice(options[0]))
        button2.config(state='normal', text=options[1],
                       command=lambda: handle_choice(options[1]))
        button3.config(state='normal', text=options[2],
                       command=lambda: handle_choice(options[2]))
        button4.config(state='normal', text=options[3],
                       command=lambda: handle_choice(options[3]))
        subject_label.config(text=subject[current_subject][0])
        break

    # 更新计时器标签
    end_time = time.time()
    elapsed_time = round(end_time - start_time)
    timer_label.config(text=f'计时器：{elapsed_time}秒')
    


def handle_retry():
    global score, current_subject
    button1.config(state='normal')
    button2.config(state='normal')
    button3.config(state='normal')
    button4.config(state='normal')
    score = max(score, 0)
    score_label.config(text=f'得分：{score}')
    while True:
        if subject[current_subject][1] == button1.cget('text'):
            options = [subject[current_subject][1],
                       subject[current_subject][2], subject[current_subject][3]]
        elif subject[current_subject][2] == button1.cget('text'):
            options = [subject[current_subject][2],
                       subject[current_subject][1], subject[current_subject][3]]
        else:
            options = [subject[current_subject][3],
                       subject[current_subject][1], subject[current_subject][2]]
        if mode.get() == 1:
            random.shuffle(options)
        button1.config(command=lambda: handle_choice(
            options[0]), text=options[0])
        button2.config(command=lambda: handle_choice(
            options[1]), text=options[1])
        button3.config(command=lambda: handle_choice(
            options[2]), text=options[2])
        button4.config(command=lambda: handle_choice(
            options[3]), text=options[3])
        break
    subject_label.config(text=subject[current_subject][0])


def update_timer():
    # 计算已经过去的时间
    elapsed_time = round(time.time() - start_time)
    # 更新计时器标签的文本和样式
    timer_label.config(text=f'计时器：{elapsed_time}秒', fg='#000000')
    # 每隔一秒调用自身更新计时器
    timer_label.after(1000, update_timer)

# 创建模式选择控件和按钮控件
mode = tk.IntVar()
mode.set(1)
mode_frame = tk.Frame(window)
mode_frame.pack(pady=10)

end_button = tk.Button(window, text='结束学习', font=(
    '微软雅黑', 12), command=window.destroy)
end_button.pack(pady=10)
end_button.bind("<Enter>", lambda event,
             h=end_button: h.config(bg='lightgray'))
end_button.bind("<Leave>", lambda event,
             h=end_button: h.config(bg='SystemButtonFace'))

# 初始化游戏
score = 0
current_subject = 0
start_time = time.time()
update_timer()

# 运行窗口
window.mainloop()



#结算界面
root = Tk()
root.title('结算')
root.geometry('1000x700')
root.resizable(width=False, height=True)
root.bind('<Button-1>', lambda event: play_click_sound())

image_account = Image.open("image\\account.jpg")
image = ImageTk.PhotoImage(image_account)

background3_label = tk.Label(root, image=image)
background3_label.place(relwidth=1, relheight=1)

account_label = tk.Label(root, text='恭喜，您一共获得了'+str(score)+'分', font=('微软雅黑', 30))
account_label.place(relx=0.5, rely=0.4, anchor='center')

end_button = tk.Button(root, text='确认', font=(
    '微软雅黑', 12), command=root.destroy)
end_button.place(relx=0.5, rely=0.6, anchor='center')
end_button.bind("<Enter>", lambda event,
             h=end_button: h.config(bg='lightgray'))
end_button.bind("<Leave>", lambda event,
             h=end_button: h.config(bg='SystemButtonFace'))

# 储存分数和时间
score_record = str(score) + ' ' + time.strftime('%Y-%m-%d-%H:%M:%S')
with open('score_record.txt', 'a') as f:
    f.write(score_record + '\n')


# 更新最高得分和上次得分
last_score = score
if last_score > high_score:
    high_score = last_score
with open('score_record.txt', 'w') as f:
    f.write(str(high_score) + ' ' + str(last_score) +
            ' ' + score_record.split()[1])

root.mainloop()
