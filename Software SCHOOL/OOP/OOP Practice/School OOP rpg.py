class Classroom:
    def __init__(self,block_name,room_number:int) -> None:
        block_name = block_name.upper()
        room_number = room_number
        self.room_name = (block_name,room_number)
    def __str__(self) -> str:
        return f"{self.room_name[0]}{self.room_name[1]}"
class Person:
    def __init__(self, name, classroom: Classroom|None = None) -> None:
        self.name = name
        self.classroom = classroom
        self._room_history = [classroom]
    def enter_room(self, room):
        self.classroom = room 
        self._room_history.append(room)
        print(f"{self.name} enters room {room}.")

class Notebook:
    def __init__(self, contents:None|str = None) -> None:
        self.contents = contents if contents is not None else ""
    def write_notes(self, contents:None|str):
        if contents:
            self.contents += contents

class Report:
    def __init__(self, content) -> None:
        self.cotents = content
    def create_report(self):
        
        return self.cotents
class Canvas:
    pass
class Edumate:
    pass

class Teacher(Person):
    pass
class Student(Person):
    pass


room_D7 = Classroom("d",7)
print(room_D7)