import time
import numpy as np

from iquestion import IQuestion, IMultiChoiceQuestion
        

class Text(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'whsOnd', 'KHxj8b')
    

    def answer(self, *answers):
        for ans in answers:
            self.answer_field.send_keys(ans)
            
            
class LinearScale(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'N9Qcwe')
        self.answer_options = self.elements(self.answer_field, 'T5pZmf')
        self.answer_labels = self.all_elements_text(self.answer_options, 'Zki2Ve')
    

    def answer(self, *answers):
        answer_d = self.answer_dict(self.answer_labels, self.answer_options)
        for ans in answers:
            answer_d.get(ans).click() 
        
class MultipleChoice(IMultiChoiceQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'oyXaNc', 
                         options='nWQGrd', labels='aDTYNe', text_holder='pIDwKe', text='Hvn9fb')
        

class CheckBoxes(IMultiChoiceQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'Y6Myld', 
                         options='eBFwI', labels='aDTYNe', text_holder='xVfcde', text='Hvn9fb')
        

class DropDown(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'vQES8d')
        self.hidden_answers = self.element(self.answer_field, 'ry3kXd')
        self.expanded_answers = self.element(self.answer_field, 'OA0qNb')

    def expand(self):
        self.hidden_answers.click()
        time.sleep(0.3)
        self.answer_options = self.elements(self.expanded_answers, 'MocG8c')
        self.answer_labels = self.all_elements_text(self.answer_options, 'vRMGwf')


    def answer(self, *answers):
        self.expand()
        answer_d = self.answer_dict(self.answer_labels, self.answer_options)
        for ans in answers:
            answer_d.get(ans).click()
        time.sleep(0.3)
        


class Grid(IQuestion):
    ''' Handle Multiple choice grid and Tick box grid questions'''
    def __init__(self, question_window):
        super().__init__(question_window, 'gTGYUd')        
        self.grid = self.get_grid()
        self.column_labels = self.elements_text(self.grid[0,1:])
        self.row_labels = self.elements_text(self.grid[1:,0])
        self.answer_options = self.grid[1:,1:]
        
    def get_rows(self, holder):
        row_types = ['EzyPc', 'lLfZXe']
        for row_type in row_types:
            out = self.elements(holder, row_type)
            if len(out)>0:
                return out
                break    

    def get_grid(self):
        grid = []
        header = self.element(self.answer_field, 'ssX1Bd')
        rows = self.get_rows(self.answer_field)
        header_elements = self.elements(header, 'V4d7Ke')
        
        grid.append(header_elements)
        for row in rows:
            row_elements = self.elements(row, 'V4d7Ke')
            grid.append(row_elements)
        return np.array(grid)
    

    def answer(self, *answers):
        r_coords = {self.row_labels[r]: r for r in range(len(self.row_labels))}
        c_coords = {self.column_labels[c]: c for c in range(len(self.column_labels))}
        
        for ans in answers:
            row, column = ans
            r_c = r_coords.get(row)
            c_c = c_coords.get(column)
            self.answer_options[r_c, c_c].click()


       
class Time(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'ocBCTb')
        self.time_options = self.set_options(self.answer_field, 'vEXS5c')
    
    def set_options(self, holder, c_name):
        answer_fields = self.elements(holder, c_name)
        answer_holders = self.all_elements(answer_fields, 'rFrNMe')
        answer_options = self.all_elements(answer_holders, 'whsOnd')
        return answer_options
    

    def answer(self, *answers):
        for ans in answers: 
            time_answers = ans.split(':')
            
            for field, answer in zip(self.time_options, time_answers):
                field.send_keys(answer)
