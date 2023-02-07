import uuid


class Tasks:
    '''Class that keeps user choice'''

    def __init__(self):
        self.show_tasks = 1


class ShowTasks(Tasks):

    '''Class that reads todo_list'''

    def read_todo_list(self):
        '''This method opens todo_list.txt file'''
        try:
            stream = open('todo_list.txt', encoding="utf-8")
            counter = 0
            for line in stream:
                counter +=1
                print(line, end='')
            if counter == 0:
                print('Empty list\n')
            if self == 3 and counter == 0:
                print('No tasks to complete')
            print('\n')
        except Exception as e_error:
            print('An error occurred: ', e_error)


  


class AddTask(Tasks):
    '''Class that adds tasks to todo_list'''

    def add_task(self):
        '''This method adds tasks to todo_list.txt file'''

        what_task = input('What is the task?: ')
        what_deadline = input('When is the deadline?: ')
        add_uuid = uuid.uuid4()
        try:
            stream = open('todo_list.txt', 'a', encoding="utf-8")
            stream.write(
                f'{str(add_uuid)} | {what_task} | {what_deadline} |\n')
            stream.close()
            print('\n')
        except Exception as e_error:
            print('An error occurred: ', e_error)


class CompleteTask(Tasks):
    '''Class that adds tasks to todo_list'''

    def empty_list_checker(self):
        '''This method checks if todo_list.txt file is empty before proceeding with complete method'''
        try:
            stream = open('todo_list.txt', encoding="utf-8")
            empty_counter = 0
            for line in stream:
                empty_counter +=1
            if self == 3 and empty_counter == 0:
                return 'Do not proceed'
        except Exception as e_error:
            print('An error occurred: ', e_error)

    def complete_task():
        '''This method adds tasks to todo_list.txt file'''

    
        remove_task = input('Enter id to complete: ')

        try:
            with open("todo_list.txt", "r+") as f:
                file_read = f.readlines()
                f.seek(0)
                for line in file_read:
                    if remove_task not in line:
                        f.write(line)
                f.truncate() #truncate to remove everything after the last write.

        except Exception as e_error:
            print('An error occurred: ', e_error)




if __name__ == '__main__':
    while True:
        try:
            print('== TODO LIST ==')
            print("[1] show tasks")
            print("[2] add task")
            print("[3] complete task")
            print("[4] exit")
            user_choice = int(input('Your choice: '))
            if user_choice == 1:
                print('\n[YOUR TASKS]')
                ShowTasks.read_todo_list(user_choice)
                continue
            if user_choice == 2:
                print('\n[ADD TASK]')
                AddTask.add_task(user_choice)
                continue
            if user_choice == 3:
                print('\n[COMPLETE TASKS]\n')
                print('[YOUR TASKS]')
                ShowTasks.read_todo_list(user_choice)
                empty_check = CompleteTask.empty_list_checker(user_choice)
                if not empty_check:
                    CompleteTask.complete_task()
                continue
            if user_choice == 4:
                print('\nBye! <3 \n')
                break
        # except ValueError:
        #     print('\nError: Type a number from the list above to proceed\n')
        except ValueError:
            print('\nError: Type a number from the list above to proceed\n')
        continue
