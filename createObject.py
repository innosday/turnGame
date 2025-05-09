import tkinter as tk
from tkinter import *
from UntilFileJson import WriteJson
import random
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Stats:
    STR: int
    INT: int
    HP: int
    END: int

class GameData:
    def __init__(self):
        self.class_skills: Dict[str, Dict[str, str]] = {
            "용사": {
                "Slash": "강력한 일격을 가합니다",
                "Shield Bash": "방패로 적을 밀쳐냅니다",
                "Battle Cry": "전투의식을 고취시킵니다",
                "Whirlwind": "회전하며 주변의 적을 공격합니다"
            },
            "마법사": {
                "Fireball": "불덩이를 발사합니다",
                "Ice Spike": "얼음 창을 발사합니다",
                "Lightning Bolt": "번개를 발사합니다",
                "Arcane Missile": "마법 화살을 발사합니다"
            },
            "도적": {
                "Backstab": "적의 뒤를 찌릅니다",
                "Stealth": "은신 상태가 됩니다",
                "Poison Strike": "독이 묻은 공격을 합니다",
                "Smoke Bomb": "연막을 치고 도망칩니다"
            },
            "힐러": {
                "Heal": "체력을 회복합니다",
                "Bless": "아군을 강화합니다",
                "Purify": "상태이상을 제거합니다",
                "Resurrection": "사망한 아군을 부활시킵니다"
            },
            "궁수": {
                "Precise Shot": "정확한 화살을 발사합니다",
                "Multi Shot": "여러 화살을 동시에 발사합니다",
                "Rain of Arrows": "화살비를 내립니다",
                "Eagle Eye": "시야를 확장합니다"
            }
        }
        
        self.mob_skills: Dict[str, Dict[str, str]] = {
            "스켈레톤": {
                "Bone Throw": "뼈를 던져 공격합니다",
                "Shield Up": "방패로 방어합니다",
                "Bone Crash": "뼈로 강하게 내려칩니다",
                "Undead Roar": "언데드의 포효로 위협합니다"
            },
            "좀비": {
                "Bite": "물어뜯습니다",
                "Rotten Touch": "썩은 손으로 만집니다",
                "Regenerate": "체력을 회복합니다",
                "Infect": "감염시킵니다"
            },
            "슬라임": {
                "Acid Splash": "산성 액체를 뿌립니다",
                "Split": "몸을 분열합니다",
                "Absorb": "적의 공격을 흡수합니다",
                "Bounce": "튀어오르며 공격합니다"
            }
        }
        
        self.monsters: List[str] = list(self.mob_skills.keys())
        self.player_classes: List[str] = list(self.class_skills.keys())

    def generate_stats(self) -> Stats:
        return Stats(
            STR=random.randint(1, 10),
            INT=random.randint(1, 10),
            HP=random.randint(1, 10),
            END=random.randint(1, 10)
        )

    def get_random_skills(self, character_type: str, name: str) -> Dict[str, str]:
        skills = self.class_skills.get(name, self.mob_skills.get(name, {}))
        skill_list = list(skills.items())
        selected_skills = random.sample(skill_list, 2)
        return dict(selected_skills)

class ObjectCreator:
    def __init__(self):
        self.root = tk.Tk()
        self.game_data = GameData()
        self.setup_window()
        self.setup_variables()
        self.create_widgets()

    def setup_window(self):
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        center_width = int((window_width / 2) - 100)
        center_height = int((window_height / 2) - 40)
        
        self.root.title("create_Object")
        self.root.geometry(f"400x300+{center_width}+{center_height}")
        self.root.resizable(False, False)

    def setup_variables(self):
        self.player_class_var = StringVar()
        self.player_name_var = StringVar()
        self.object_type_var = IntVar()

    def create_widgets(self):
        # Object type selection
        self.create_object_type_frame()
        self.create_player_frame()
        self.create_mob_frame()
        self.create_bottom_button()

    def create_object_type_frame(self):
        label_ObjectType = LabelFrame(self.root, text="오브젝트 타입")
        label_ObjectType.pack(fill=BOTH, expand=True)

        for i, text in enumerate(["Player", "Mob", "Object"]):
            Radiobutton(
                label_ObjectType,
                text=text,
                variable=self.object_type_var,
                value=i + 1,
                command=self.update_frames
            ).grid(row=1, column=i + 1)

    def create_player_frame(self):
        self.player_frame = LabelFrame(self.root, text="플레이어 정보")
        
        # Name input
        name_frame = Frame(self.player_frame)
        name_frame.pack(pady=5)
        Label(name_frame, text="이름:").pack(side=LEFT, padx=5)
        Entry(name_frame, textvariable=self.player_name_var).pack(side=LEFT)

        # Class selection
        Label(self.player_frame, text="직업:").pack()
        class_frame = Frame(self.player_frame)
        class_frame.pack()
        
        for i, class_name in enumerate(self.game_data.player_classes):
            Radiobutton(
                class_frame,
                text=class_name,
                variable=self.player_class_var,
                value=class_name
            ).grid(row=0, column=i, padx=5)

    def create_mob_frame(self):
        self.mob_frame = LabelFrame(self.root, text="몬스터 정보")
        Label(self.mob_frame, text="몬스터는 자동으로 선택됩니다.").pack()

    def create_bottom_button(self):
        bottom_frame = Frame(self.root)
        bottom_frame.pack(side=BOTTOM, fill=X, pady=10)
        Button(
            bottom_frame,
            text="확인",
            width=10,
            bg="yellow",
            command=self.save
        ).pack()

    def update_frames(self):
        selected_type = self.object_type_var.get()
        if selected_type == 1:  # Player
            self.player_frame.pack(fill=BOTH, expand=True)
            self.mob_frame.pack_forget()
        elif selected_type == 2:  # Mob
            self.player_frame.pack_forget()
            self.mob_frame.pack(fill=BOTH, expand=True)
        else:  # Object
            self.player_frame.pack_forget()
            self.mob_frame.pack_forget()

    def save(self):
        selected_type = self.object_type_var.get()
        data = {}
        filename = ""

        if selected_type == 1:  # Player
            name = self.player_name_var.get()
            player_class = self.player_class_var.get()
            if not name or not player_class:
                return

            stats = self.game_data.generate_stats()
            skills = self.game_data.get_random_skills("player", player_class)

            data = {
                "type": "Player",
                "name": name,
                "class": player_class,
                "stats": vars(stats),
                "skills": skills
            }
            filename = f"player/Player_{player_class}_{name}.json"

        elif selected_type == 2:  # Mob
            monster = random.choice(self.game_data.monsters)
            stats = self.game_data.generate_stats()
            skills = self.game_data.get_random_skills("mob", monster)

            data = {
                "type": "Mob",
                "name": monster,
                "stats": vars(stats),
                "skills": skills
            }
            filename = f"mob/Mob_{monster}.json"

        else:  # Object
            data = {"type": "Object"}
            filename = "object/Object.json"

        WriteJson(filename, data)
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ObjectCreator()
    app.run()