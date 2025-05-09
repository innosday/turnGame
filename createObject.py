import tkinter as tk
from tkinter import *
from UntilFileJson import WriteJson
import random

root = tk.Tk()

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

center_width = int((window_width / 2) - 100)
center_height = int((window_height /2) - 40)

root.title("create_Object")
root.geometry(f"400x300+{center_width}+{center_height}")
root.resizable(False,False)

# Player class selection variables
player_class_var = StringVar()
player_name_var = StringVar()

# Class skills mapping
class_skills = {
    "용사": {
        "skills": {
            "Slash": "강력한 일격을 가합니다",
            "Shield Bash": "방패로 적을 밀쳐냅니다",
            "Battle Cry": "전투의식을 고취시킵니다",
            "Whirlwind": "회전하며 주변의 적을 공격합니다"
        }
    },
    "마법사": {
        "skills": {
            "Fireball": "불덩이를 발사합니다",
            "Ice Spike": "얼음 창을 발사합니다",
            "Lightning Bolt": "번개를 발사합니다",
            "Arcane Missile": "마법 화살을 발사합니다"
        }
    },
    "도적": {
        "skills": {
            "Backstab": "적의 뒤를 찌릅니다",
            "Stealth": "은신 상태가 됩니다",
            "Poison Strike": "독이 묻은 공격을 합니다",
            "Smoke Bomb": "연막을 치고 도망칩니다"
        }
    },
    "힐러": {
        "skills": {
            "Heal": "체력을 회복합니다",
            "Bless": "아군을 강화합니다",
            "Purify": "상태이상을 제거합니다",
            "Resurrection": "사망한 아군을 부활시킵니다"
        }
    },
    "궁수": {
        "skills": {
            "Precise Shot": "정확한 화살을 발사합니다",
            "Multi Shot": "여러 화살을 동시에 발사합니다",
            "Rain of Arrows": "화살비를 내립니다",
            "Eagle Eye": "시야를 확장합니다"
        }
    }
}

# Mob skills mapping
mob_skills = {
    "스켈레톤": {
        "skills": {
            "Bone Throw": "뼈를 던져 공격합니다",
            "Shield Up": "방패로 방어합니다",
            "Bone Crash": "뼈로 강하게 내려칩니다",
            "Undead Roar": "언데드의 포효로 위협합니다"
        }
    },
    "좀비": {
        "skills": {
            "Bite": "물어뜯습니다",
            "Rotten Touch": "썩은 손으로 만집니다",
            "Regenerate": "체력을 회복합니다",
            "Infect": "감염시킵니다"
        }
    },
    "슬라임": {
        "skills": {
            "Acid Splash": "산성 액체를 뿌립니다",
            "Split": "몸을 분열합니다",
            "Absorb": "적의 공격을 흡수합니다",
            "Bounce": "튀어오르며 공격합니다"
        }
    }
}

def generate_random_stats():
    return {
        "STR": random.randint(1, 10),  # 힘
        "INT": random.randint(1, 10),  # 지능
        "HP": random.randint(1, 10),   # 체력
        "END": random.randint(1, 10)   # 지구력
    }

def get_random_skills(player_class):
    skills = class_skills[player_class]["skills"]
    skill_list = list(skills.items())
    selected_skills = random.sample(skill_list, 2)
    return {name: desc for name, desc in selected_skills}

def get_random_mob_skills(monster):
    skills = mob_skills[monster]["skills"]
    skill_list = list(skills.items())
    selected_skills = random.sample(skill_list, 2)
    return {name: desc for name, desc in selected_skills}

def save():
    selected_type = var.get()
    data = {}
    filename = ""
    
    if selected_type == 1:  # Player
        name = player_name_var.get()
        player_class = player_class_var.get()
        if not name or not player_class:
            return
        
        # Generate random stats and skills
        stats = generate_random_stats()
        skills = get_random_skills(player_class)
        
        data = {
            "type": "Player",
            "name": name,
            "class": player_class,
            "stats": stats,
            "skills": skills
        }
        filename = f"player/Player_{player_class}_{name}.json"
    elif selected_type == 2:  # Mob
        monsters = ["스켈레톤", "좀비", "슬라임"]
        monster = random.choice(monsters)
        
        # Generate random stats and skills
        stats = generate_random_stats()
        skills = get_random_mob_skills(monster)
        
        data = {
            "type": "Mob",
            "name": monster,
            "stats": stats,
            "skills": skills
        }
        filename = f"mob/Mob_{monster}.json"
    elif selected_type == 3:  # Object
        data = {
            "type": "Object"
        }
        filename = "object/Object.json"
    
    WriteJson(filename, data)
    root.destroy()

def status():
    selected_var = var.get()
    if selected_var == 1:  # Player
        player_frame.pack(fill=BOTH, expand=True)
        mob_frame.pack_forget()
    elif selected_var == 2:  # Mob
        player_frame.pack_forget()
        mob_frame.pack(fill=BOTH, expand=True)
    else:  # Object
        player_frame.pack_forget()
        mob_frame.pack_forget()

# Object type selection
label_ObjectType = LabelFrame(root, text="오브젝트 타입")
label_ObjectType.pack(fill=BOTH, expand=True)

var = IntVar()
c1 = Radiobutton(label_ObjectType, text="Player", variable=var, value=1, command=status)
c2 = Radiobutton(label_ObjectType, text="Mob", variable=var, value=2, command=status)
c3 = Radiobutton(label_ObjectType, text="Object", variable=var, value=3, command=status)

c1.grid(row=1, column=1)
c2.grid(row=1, column=2)
c3.grid(row=1, column=3)

# Player selection frame
player_frame = LabelFrame(root, text="플레이어 정보")

# Create a frame for name input
name_frame = Frame(player_frame)
name_frame.pack(pady=5)

player_name_label = Label(name_frame, text="이름:")
player_name_label.pack(side=LEFT, padx=5)
player_name_entry = Entry(name_frame, textvariable=player_name_var)
player_name_entry.pack(side=LEFT)

player_class_label = Label(player_frame, text="직업:")
player_class_label.pack()

# Create a frame for horizontal arrangement of class radio buttons
class_frame = Frame(player_frame)
class_frame.pack()

# Korean to English class mapping
class_mapping = {
    "용사": "Warrior",
    "마법사": "Mage",
    "도적": "Rogue",
    "힐러": "Healer",
    "궁수": "Archer"
}

player_classes = ["용사", "마법사", "도적", "힐러", "궁수"]
for i, class_name in enumerate(player_classes):
    Radiobutton(class_frame, text=class_name, variable=player_class_var, value=class_name).grid(row=0, column=i, padx=5)

# Mob frame
mob_frame = LabelFrame(root, text="몬스터 정보")
mob_label = Label(mob_frame, text="몬스터는 자동으로 선택됩니다.")
mob_label.pack()

# Create a frame for the bottom button
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X, pady=10)

b1 = Button(bottom_frame, text="확인", width=10, bg="yellow", command=save)
b1.pack()

root.mainloop()