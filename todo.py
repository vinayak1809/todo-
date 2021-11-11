
done = False


class create_task:
    li = []
    di = {}
    task = False

    def do():

        print("\n if done with entering task : type \"exit\"")
        while not create_task.task:
            en = input(" enter the task : ").lower()

            if en == "exit":
                create_task.task = True
            elif en:
                create_task.li.append(en)

            for i, m in enumerate(create_task.li, 1):
                create_task.di.update({i: m})

            for key, val in create_task.di.items():
                print(str(key) + ") " + val)
            print("")
#            print(create_task.di)


class task_done:

    def done():
        en = int(input("\n enter the integer of the task which is done : "))

        create_task.di.pop(en)

        for key, val in create_task.di.items():
            print(str(key) + ") " + val)


while not done:

    en = input(
        "\n if you want to enter the task : type \"task\" \n if you remove/done with the task : type \"done\" : ").lower()

    if en == "task":
        obj = create_task
        obj.do()

    elif en == "done":
        obj = task_done
        obj.done()
